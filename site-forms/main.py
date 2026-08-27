"""site-forms — the pilot-application endpoint behind regentprotocol.org.

One job: take the /pilot form's JSON, send it as an email to the team inbox
with Reply-To set to the applicant. No database — the inbox is the CRM at
this stage. Honeypot field + nginx rate limiting keep the bots out.
"""

from __future__ import annotations

import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="site-forms")

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
