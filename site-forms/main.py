"""site-forms — the two forms behind regentprotocol.org.

/pilot: the pilot application. /beta-feedback: a beta tester's report, from the /beta
page or from the console's "Report a problem". Both become an email to the team inbox,
with Reply-To set to the sender when they left an address. No database — the inbox is
the CRM at this stage. Honeypot field + nginx rate limiting keep the bots out.

A report may carry one screenshot. People paste keys into reports and leave them on
screenshots, and this inbox is ordinary mail: anything in the text that looks like a
key is cut to its prefix before it is sent, and the form tells the person to hide keys
in the picture (we cannot read a picture).
"""

from __future__ import annotations

import base64
import binascii
import os
import re
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.utils import formataddr
from typing import Literal

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field, field_validator

app = FastAPI(title="site-forms")

# The console is another origin (web.regentprotocol.org) and posts its "Report a problem"
# here. Nothing else is let in: the /beta page and /pilot are same-origin and need no CORS.
FEEDBACK_ORIGINS = [o.strip() for o in os.environ.get(
    "FEEDBACK_ORIGINS", "https://web.regentprotocol.org"
).split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware, allow_origins=FEEDBACK_ORIGINS, allow_credentials=False,
    allow_methods=["POST"], allow_headers=["content-type"], max_age=600,
)

SMTP_HOST = os.environ.get("SMTP_HOST", "smtppro.zoho.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "465"))
SMTP_USERNAME = os.environ.get("SMTP_USERNAME", "info@regentprotocol.org")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
# CEO + CTO inboxes (comma-separated, overridable via env)
TO_EMAILS = [e.strip() for e in os.environ.get(
    "TO_EMAILS", "ae.aubakirov@gmail.com,prosayat@gmail.com"
).split(",") if e.strip()]


class PilotApplication(BaseModel):
    email: EmailStr
    company: str = Field(min_length=2, max_length=200)
    role: str = Field(min_length=2, max_length=200)
    act_for: str = Field(max_length=100)
    stage: str = Field(max_length=100)
    volume: str = Field(default="", max_length=100)
    workflow: str = Field(min_length=10, max_length=4000)
    # honeypot: real users never fill this hidden field
    website: str = Field(default="", max_length=200)


@app.get("/healthz")
async def healthz() -> dict:
    return {"ok": True, "service": "site-forms"}


@app.post("/pilot")
async def pilot(body: PilotApplication) -> dict:
    if body.website:  # bot filled the honeypot — accept silently, send nothing
        return {"status": "received"}
    if not SMTP_PASSWORD:
        raise HTTPException(status_code=503, detail={
            "code": "FORMS_DISABLED", "message": "Applications are temporarily unavailable — email info@regentprotocol.org."})

    text = (
        "Pilot application — regentprotocol.org/pilot\n\n"
        f"Email:     {body.email}\n"
        f"Company:   {body.company}\n"
        f"Role:      {body.role}\n"
        f"Agents act for:      {body.act_for}\n"
        f"Stage today:         {body.stage}\n"
        f"Est. financial actions/mo: {body.volume or '—'}\n\n"
        f"Workflow:\n{body.workflow}\n"
    )
    msg = MIMEText(text)
    msg["Subject"] = f"Pilot application — {body.company}"
    msg["From"] = formataddr(("Regent Protocol site", SMTP_USERNAME))
    msg["To"] = ", ".join(TO_EMAILS)
    msg["Reply-To"] = body.email
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15) as smtp:
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
            smtp.send_message(msg)
    except Exception as exc:
        raise HTTPException(status_code=502, detail={
            "code": "SEND_FAILED", "message": "Could not submit right now — email info@regentprotocol.org."}) from exc
    return {"status": "received"}


# ── Beta feedback ──────────────────────────────────────────────────────────────

MAX_SCREENSHOT_BYTES = 2 * 1024 * 1024
# What the bytes are, by their own first bytes: the name and type the browser sent are
# not trusted, and nothing but a picture is forwarded to a mailbox.
_IMAGE_MAGIC = (
    (b"\x89PNG\r\n\x1a\n", "png"),
    (b"\xff\xd8\xff", "jpeg"),
)
# Credentials people paste by mistake: Regent keys, Stripe keys and webhook secrets.
_SECRET_RE = re.compile(
    r"\b(rgnt_(?:[a-z]{2,6}_)?|[rs]k_(?:live|test)_|whsec_|pk_(?:live|test)_)[A-Za-z0-9_\-]{6,}"
)


def image_kind(data: bytes) -> str | None:
    for magic, kind in _IMAGE_MAGIC:
        if data.startswith(magic):
            return kind
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    return None


def redact_secrets(text: str) -> tuple[str, int]:
    """The text with every key-looking string cut to its prefix, and how many were cut."""
    return _SECRET_RE.subn(lambda m: m.group(1) + "[removed]", text)


class Screenshot(BaseModel):
    # base64 of at most MAX_SCREENSHOT_BYTES (4 characters per 3 bytes, plus padding)
    data: str = Field(min_length=16, max_length=MAX_SCREENSHOT_BYTES * 4 // 3 + 8)


class BetaFeedback(BaseModel):
    report: str = Field(min_length=10, max_length=6000)
    email: EmailStr | None = None
    source: Literal["beta_page", "console"] = "beta_page"
    # filled by the console, never asked of a person: where they were when it broke
    org_id: str = Field(default="", max_length=64)
    page: str = Field(default="", max_length=200)
    screenshot: Screenshot | None = None
    # honeypot: real users never fill this hidden field
    website: str = Field(default="", max_length=200)

    @field_validator("email", mode="before")
    @classmethod
    def _blank_is_none(cls, v):
        return None if isinstance(v, str) and not v.strip() else v


def _one_line(value: str) -> str:
    return " ".join(value.split())


@app.post("/beta-feedback")
async def beta_feedback(body: BetaFeedback) -> dict:
    if body.website:  # bot filled the honeypot — accept silently, send nothing
        return {"status": "received"}
    if not SMTP_PASSWORD:
        raise HTTPException(status_code=503, detail={
            "code": "FORMS_DISABLED", "message": "Reports are temporarily unavailable — email info@regentprotocol.org."})

    picture: tuple[bytes, str] | None = None
    if body.screenshot is not None:
        try:
            raw = base64.b64decode(body.screenshot.data, validate=True)
        except (binascii.Error, ValueError) as exc:
            raise HTTPException(status_code=422, detail={
                "code": "SCREENSHOT_UNREADABLE", "message": "The screenshot could not be read. Attach a PNG, JPEG or WebP."}) from exc
        if len(raw) > MAX_SCREENSHOT_BYTES:
            raise HTTPException(status_code=413, detail={
                "code": "SCREENSHOT_TOO_LARGE", "message": "The screenshot is over 2 MB. Crop it or send it by email."})
        kind = image_kind(raw)
        if kind is None:
            raise HTTPException(status_code=422, detail={
                "code": "SCREENSHOT_NOT_AN_IMAGE", "message": "Attach a PNG, JPEG or WebP picture."})
        picture = (raw, kind)

    report, removed = redact_secrets(body.report)
    where = "the console" if body.source == "console" else "regentprotocol.org/beta"
    lines = [f"Beta report — from {where}", ""]
    lines.append(f"Reply to:  {body.email or '— (no address left)'}")
    if body.org_id:
        lines.append(f"Org:       {_one_line(body.org_id)}")
    if body.page:
        lines.append(f"Page:      {_one_line(body.page)}")
    lines.append(f"Screenshot: {'attached (' + picture[1] + ', ' + str(len(picture[0]) // 1024) + ' KB)' if picture else 'none'}")
    if removed:
        lines.append(f"Removed:   {removed} string(s) that looked like a key; tell the sender to rotate it")
    lines += ["", report, ""]

    msg = EmailMessage()
    msg["Subject"] = "Beta report — " + ("console" if body.source == "console" else "beta page")
    msg["From"] = formataddr(("Regent Protocol site", SMTP_USERNAME))
    msg["To"] = ", ".join(TO_EMAILS)
    if body.email:
        msg["Reply-To"] = body.email
    msg.set_content("\n".join(lines))
    if picture:
        msg.add_attachment(picture[0], maintype="image", subtype=picture[1], filename=f"screenshot.{picture[1]}")
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, timeout=15) as smtp:
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
            smtp.send_message(msg)
    except Exception as exc:
        raise HTTPException(status_code=502, detail={
            "code": "SEND_FAILED", "message": "Could not send right now — email info@regentprotocol.org."}) from exc
    return {"status": "received", "redacted": removed}
