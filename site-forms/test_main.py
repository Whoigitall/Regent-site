"""site-forms: the beta report endpoint. Run: python -m pytest test_main.py"""

import base64

import pytest
from fastapi.testclient import TestClient

import main

PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 64
JPEG = b"\xff\xd8\xff\xe0" + b"\x00" * 64
WEBP = b"RIFF\x24\x00\x00\x00WEBPVP8 " + b"\x00" * 32


class FakeSMTP:
    sent: list = []

    def __init__(self, *a, **k):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def login(self, *a):
        pass

    def send_message(self, msg):
        FakeSMTP.sent.append(msg)


@pytest.fixture
def client(monkeypatch):
    FakeSMTP.sent = []
    main._sent.update(day="", count=0)
    monkeypatch.setattr(main.smtplib, "SMTP_SSL", FakeSMTP)
    monkeypatch.setattr(main, "SMTP_PASSWORD", "x")
    return TestClient(main.app)


def b64(data: bytes) -> str:
    return base64.b64encode(data).decode()


def test_a_report_becomes_one_mail_with_the_senders_address(client):
    r = client.post("/beta-feedback", json={"report": "Instinct paid 7 USD and got ESCALATION_REQUIRED, dec_82c44e343894",
                                            "email": "tester@example.com"})
    assert r.status_code == 200 and r.json() == {"status": "received", "redacted": 0}
    (msg,) = FakeSMTP.sent
    assert msg["Reply-To"] == "tester@example.com" and msg["Subject"] == "Beta report — beta page"
    assert "dec_82c44e343894" in msg.get_content()


def test_the_address_is_optional_and_a_blank_one_is_no_address(client):
    r = client.post("/beta-feedback", json={"report": "The approve button did nothing.", "email": "  "})
    assert r.status_code == 200
    assert FakeSMTP.sent[0]["Reply-To"] is None and "no address left" in FakeSMTP.sent[0].get_content()


def test_a_key_pasted_into_the_report_never_reaches_the_inbox(client):
    report = ("I pasted rk_test_51UOwEuKD5a0avNQfabcdefgh and the agent used rgnt_agt_Zk3_9aQx77Lm; "
              "webhook whsec_abcdef123456 too. Decision dec_5c1dea206840 stays readable.")
    r = client.post("/beta-feedback", json={"report": report})
    assert r.json()["redacted"] == 3
    text = FakeSMTP.sent[0].get_content()
    assert "51UOwEuKD5a0avNQf" not in text and "Zk3_9aQx77Lm" not in text and "abcdef123456" not in text
    assert "rk_test_[removed]" in text and "rgnt_agt_[removed]" in text and "whsec_[removed]" in text
    assert "dec_5c1dea206840" in text and "rotate" in text


@pytest.mark.parametrize("data,kind", [(PNG, "png"), (JPEG, "jpeg"), (WEBP, "webp")])
def test_a_picture_is_attached_under_the_type_its_bytes_say(client, data, kind):
    r = client.post("/beta-feedback", json={"report": "See the screenshot please.", "screenshot": {"data": b64(data)}})
    assert r.status_code == 200
    (part,) = list(FakeSMTP.sent[0].iter_attachments())
    assert part.get_content_type() == f"image/{kind}" and part.get_filename() == f"screenshot.{kind}"
    assert part.get_content() == data


def test_anything_that_is_not_a_picture_is_refused_and_nothing_is_sent(client):
    for payload in (b"<html><script>alert(1)</script></html>" * 2, b"%PDF-1.7 " + b"0" * 40, b"MZ" + b"\x00" * 60):
        r = client.post("/beta-feedback", json={"report": "Here is my file.", "screenshot": {"data": b64(payload)}})
        assert r.status_code == 422 and r.json()["detail"]["code"] == "SCREENSHOT_NOT_AN_IMAGE"
    r = client.post("/beta-feedback", json={"report": "Here is my file.", "screenshot": {"data": "not base64 at all!!"}})
    assert r.status_code == 422 and r.json()["detail"]["code"] == "SCREENSHOT_UNREADABLE"
    assert FakeSMTP.sent == []


def test_a_picture_over_two_megabytes_is_refused(client):
    big = PNG + b"\x00" * main.MAX_SCREENSHOT_BYTES
    r = client.post("/beta-feedback", json={"report": "A very large screenshot.", "screenshot": {"data": b64(big)}})
    assert r.status_code in (413, 422) and FakeSMTP.sent == []
    just_under = PNG + b"\x00" * (main.MAX_SCREENSHOT_BYTES - len(PNG))
    r = client.post("/beta-feedback", json={"report": "A large but allowed screenshot.", "screenshot": {"data": b64(just_under)}})
    assert r.status_code == 200 and len(FakeSMTP.sent) == 1


def test_the_console_names_the_organization_and_the_page(client):
    r = client.post("/beta-feedback", json={"report": "Go live button spins forever.", "source": "console",
                                            "org_id": "ac94f7c8-8683-4624-a5c5-ab2b13a0fcb0", "page": "/kyc"})
    assert r.status_code == 200
    msg = FakeSMTP.sent[0]
    assert msg["Subject"] == "Beta report — console"
    assert "ac94f7c8-8683-4624-a5c5-ab2b13a0fcb0" in msg.get_content() and "/kyc" in msg.get_content()


def test_a_line_break_in_a_console_field_cannot_forge_a_mail_header_or_a_line(client):
    r = client.post("/beta-feedback", json={"report": "Something broke here.", "source": "console",
                                            "org_id": "org\nBcc: evil@example.com", "page": "/x\r\nReply to: evil@example.com"})
    assert r.status_code == 200
    msg = FakeSMTP.sent[0]
    assert msg["Bcc"] is None and msg["Reply-To"] is None
    assert "\nBcc:" not in msg.get_content() and "\nReply to: evil" not in msg.get_content()


def test_a_bot_that_fills_the_hidden_field_is_thanked_and_ignored(client):
    r = client.post("/beta-feedback", json={"report": "Buy cheap watches now!!", "website": "http://spam.example"})
    assert r.status_code == 200 and FakeSMTP.sent == []


def test_too_short_a_report_and_a_bad_address_are_refused(client):
    assert client.post("/beta-feedback", json={"report": "bad"}).status_code == 422
    assert client.post("/beta-feedback", json={"report": "A real report text.", "email": "not-an-address"}).status_code == 422
    assert client.post("/beta-feedback", json={"report": "A real report text.", "source": "elsewhere"}).status_code == 422


def test_only_the_console_origin_may_post_from_another_site(client):
    ok = client.options("/beta-feedback", headers={"Origin": "https://web.regentprotocol.org",
                                                   "Access-Control-Request-Method": "POST",
                                                   "Access-Control-Request-Headers": "content-type"})
    assert ok.status_code == 200 and ok.headers["access-control-allow-origin"] == "https://web.regentprotocol.org"
    no = client.options("/beta-feedback", headers={"Origin": "https://evil.example",
                                                   "Access-Control-Request-Method": "POST"})
    assert "access-control-allow-origin" not in no.headers


def test_the_pilot_form_still_works(client):
    r = client.post("/pilot", json={"email": "a@b.co", "company": "Acme", "role": "CTO", "act_for": "customers",
                                    "stage": "pilot", "workflow": "Refund agent on Stripe, 200 actions a month."})
    assert r.status_code == 200 and FakeSMTP.sent[0]["Subject"] == "Pilot application — Acme"


# ── a public form: links broken on purpose, a ceiling on mails a day ──────────────

PILOT = {"email": "cto@example.com", "company": "Acme", "role": "CTO", "act_for": "customers",
         "stage": "pilot", "workflow": "Agents refund customers within limits."}


def test_a_link_in_a_report_arrives_broken_and_the_mail_says_who_wrote_it(client):
    r = client.post("/beta-feedback", json={
        "report": "Urgent, your key leaked: log in at https://regent-protocol.evil.example/login or www.evil.example now"})
    assert r.status_code == 200
    text = FakeSMTP.sent[0].get_content()
    assert text.splitlines()[1] == main.UNVERIFIED_NOTE
    assert "://" not in text.replace("[://]", "") and "https[://]regent-protocol[.]evil[.]example/login" in text
    assert "www[.]evil[.]example" in text and "evil.example" not in text


@pytest.mark.parametrize("plain", [
    "regent-control 0.14.0 answered ESCALATION_REQUIRED for dec_82c44e343894 at 14:05.",
    "Paid $7.50, e.g. twice. Then it stopped",
])
def test_ordinary_report_text_is_left_as_written(plain):
    assert main.defang(plain) == plain


def test_defang_breaks_every_form_a_mail_client_would_link():
    assert main.defang("http://1.2.3.4/x") == "http[://]1[.]2[.]3[.]4/x"
    assert main.defang("see evil.com/login and main.py") == "see evil[.]com/login and main[.]py"
    assert main.defang("write to boss@evil.com") == "write to boss@evil[.]com"


def test_a_key_is_still_removed_when_it_sits_inside_a_link(client):
    r = client.post("/beta-feedback", json={"report": "it called https://x.example/?k=sk_live_51abcDEF123456 and failed"})
    assert r.json()["redacted"] == 1
    text = FakeSMTP.sent[0].get_content()
    assert "51abcDEF123456" not in text and "sk_live_[removed]" in text


def test_the_day_has_a_ceiling_shared_by_both_forms_and_it_lifts_the_next_day(client, monkeypatch):
    monkeypatch.setattr(main, "DAILY_MAIL_CAP", 2)
    assert client.post("/beta-feedback", json={"report": "First report of the day."}).status_code == 200
    assert client.post("/pilot", json=PILOT).status_code == 200
    r = client.post("/beta-feedback", json={"report": "Third mail of the day."})
    assert r.status_code == 503 and r.json()["detail"]["code"] == "FORMS_BUSY"
    assert "info@regentprotocol.org" in r.json()["detail"]["message"]
    assert client.post("/pilot", json=PILOT).status_code == 503
    assert len(FakeSMTP.sent) == 2
    main._sent["day"] = "2000-01-01"          # yesterday's count does not carry over
    assert client.post("/beta-feedback", json={"report": "A report the next day."}).status_code == 200
    assert len(FakeSMTP.sent) == 3


def test_what_sends_no_mail_uses_none_of_the_days_ceiling(client, monkeypatch):
    monkeypatch.setattr(main, "DAILY_MAIL_CAP", 1)
    client.post("/beta-feedback", json={"report": "A bot wrote this one.", "website": "http://spam"})
    client.post("/beta-feedback", json={"report": "Not a picture attached.", "screenshot": {"data": b64(b"%PDF-1.7" + b"0" * 64)}})
    client.post("/beta-feedback", json={"report": "short"})
    assert main._sent["count"] == 0
    assert client.post("/beta-feedback", json={"report": "The one real report."}).status_code == 200


def test_the_pilot_mail_carries_the_note_and_no_live_link_even_in_its_subject(client):
    r = client.post("/pilot", json=dict(PILOT, company="Acme http://evil.example", workflow="See evil.example/deck for our flow."))
    assert r.status_code == 200
    (msg,) = FakeSMTP.sent
    assert "evil.example" not in msg["Subject"] and "://" not in msg["Subject"].replace("[://]", "")
    body = msg.get_payload(decode=True).decode()
    assert main.UNVERIFIED_NOTE in body and "evil.example" not in body

