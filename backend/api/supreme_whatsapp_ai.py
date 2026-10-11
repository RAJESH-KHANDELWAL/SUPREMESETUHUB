"""Official WhatsApp Business Platform webhook and consent-based messaging.

- Incoming user messages can receive AI-generated replies.
- Proactive outreach is restricted to an approved template and explicit opt-in.
- This module never scrapes phone numbers or bulk-messages prospects.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import logging
import os
import re
import urllib.error
import urllib.request
from typing import Any

from fastapi import APIRouter, Header, HTTPException, Query, Request
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/supreme-ecosystem/whatsapp",
    tags=["SUPREME ECOSYSTEM - WHATSAPP AI"],
)

# Best-effort process-local deduplication. Production deployments should use a
# durable shared store (e.g. Redis/DB) before running multiple instances.
_seen_message_ids: set[str] = set()
_MAX_SEEN_IDS = 2000


def _env(name: str) -> str:
    return os.getenv(name, "").strip()


def _api_url(path: str) -> str:
    version = _env("WHATSAPP_GRAPH_API_VERSION")
    if not version:
        raise RuntimeError("WHATSAPP_GRAPH_API_VERSION is not configured")
    return f"https://graph.facebook.com/{version}/{path.lstrip('/')}"


def _request_json(url: str, payload: dict[str, Any], token: str) -> dict[str, Any]:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")[:1200]
        logger.warning("External messaging API returned %s: %s", exc.code, details)
        raise RuntimeError(f"External messaging API returned HTTP {exc.code}") from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        logger.warning("External messaging API request failed: %s", exc)
        raise RuntimeError("External messaging API request failed") from exc


def _send_text(recipient: str, text: str) -> dict[str, Any]:
    token = _env("WHATSAPP_ACCESS_TOKEN")
    phone_id = _env("WHATSAPP_PHONE_NUMBER_ID")
    if not token or not phone_id:
        raise RuntimeError("WhatsApp access token/phone number ID is not configured")
    return _request_json(
        _api_url(f"{phone_id}/messages"),
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text[:4000]},
        },
        token,
    )


def _send_approved_template(
    recipient: str,
    template_name: str,
    language: str,
    parameters: list[str],
) -> dict[str, Any]:
    token = _env("WHATSAPP_ACCESS_TOKEN")
    phone_id = _env("WHATSAPP_PHONE_NUMBER_ID")
    approved_name = _env("WHATSAPP_OUTREACH_TEMPLATE_NAME")
    if not token or not phone_id or not approved_name:
        raise RuntimeError(
            "WhatsApp credentials and WHATSAPP_OUTREACH_TEMPLATE_NAME are required"
        )
    # Do not allow callers to substitute arbitrary templates.
    if template_name != approved_name:
        raise ValueError("TEMPLATE_NAME_MUST_MATCH_CONFIGURED_APPROVED_TEMPLATE")
    components = []
    if parameters:
        components.append({
            "type": "body",
            "parameters": [
                {"type": "text", "text": value[:500]}
                for value in parameters[:10]
            ],
        })
    payload: dict[str, Any] = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient,
        "type": "template",
        "template": {
            "name": approved_name,
            "language": {"code": language},
        },
    }
    if components:
        payload["template"]["components"] = components
    return _request_json(_api_url(f"{phone_id}/messages"), payload, token)


def _ai_reply(incoming_text: str) -> str:
    api_key = _env("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured")
    model = _env("OPENAI_MODEL") or "gpt-4.1-mini"
    payload = {
        "model": model,
        "instructions": (
            "You are the WhatsApp assistant for DR RAJESH KHANDELWAL IBC. "
            "Be warm, concise, honest, and professional. Help qualify legitimate "
            "freelance projects in WordPress, website fixes, SEO/blog writing, "
            "copywriting, and social media content. Ask one useful question at a "
            "time about the project scope, deadline, budget, and payment terms. "
            "If the person wants to collaborate, you may ask for their full name "
            "and city/state. Explain politely that they can save the business "
            "number as DR RAJESH KHANDELWAL IBC and voluntarily share a cropped "
            "contact screenshot, but never claim that you saved their contact or "
            "that a screenshot proves it. Never promise work, income, or a client. "
            "Never ask for OTPs, passwords, card details, or fees. Do not pressure "
            "people or send unsolicited follow-ups. For pricing, disputes, legal "
            "matters, or unclear commitments, say Rajesh will confirm personally. "
            "Reply in the language used by the sender where practical."
        ),
        "input": incoming_text[:6000],
        "max_output_tokens": 350,
    }
    result = _request_json(
        "https://api.openai.com/v1/responses",
        payload,
        api_key,
    )
    # _request_json is shared with Meta and sends the token as Bearer auth.
    # Responses API uses the same Authorization scheme.
    output_text = result.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()[:3500]
    chunks: list[str] = []
    for item in result.get("output", []):
        for part in item.get("content", []):
            if part.get("type") == "output_text" and part.get("text"):
                chunks.append(str(part["text"]))
    reply = "\n".join(chunks).strip()
    if not reply:
        raise RuntimeError("AI provider returned no text")
    return reply[:3500]


class OutreachTemplateRequest(BaseModel):
    recipient: str = Field(min_length=8, max_length=20, description="Country code plus digits")
    opt_in_confirmed: bool = Field(
        description="Must be true only when the recipient has explicitly agreed to receive WhatsApp messages"
    )
    template_name: str = Field(min_length=1, max_length=100)
    language: str = Field(default="en", min_length=2, max_length=12)
    parameters: list[str] = Field(default_factory=list, max_length=10)


def _normalize_phone(value: str) -> str:
    digits = re.sub(r"\D", "", value)
    if not 8 <= len(digits) <= 15:
        raise HTTPException(status_code=422, detail="INVALID_RECIPIENT_PHONE")
    return digits


@router.get("/webhook")
def verify_webhook(
    mode: str | None = Query(default=None, alias="hub.mode"),
    verify_token: str | None = Query(default=None, alias="hub.verify_token"),
    challenge: str | None = Query(default=None, alias="hub.challenge"),
):
    expected = _env("WHATSAPP_VERIFY_TOKEN")
    if mode == "subscribe" and expected and verify_token and hmac.compare_digest(
        verify_token, expected
    ):
        return PlainTextResponse(challenge or "")
    raise HTTPException(status_code=403, detail="WHATSAPP_WEBHOOK_VERIFICATION_FAILED")


@router.post("/webhook")
async def receive_webhook(
    request: Request,
    x_hub_signature_256: str | None = Header(default=None),
):
    raw_body = await request.body()
    app_secret = _env("WHATSAPP_APP_SECRET")
    if not app_secret or not x_hub_signature_256:
        raise HTTPException(status_code=401, detail="WEBHOOK_SIGNATURE_REQUIRED")
    digest = hmac.new(app_secret.encode("utf-8"), raw_body, hashlib.sha256).hexdigest()
    expected_signature = f"sha256={digest}"
    if not hmac.compare_digest(expected_signature, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="INVALID_WEBHOOK_SIGNATURE")

    try:
        payload = json.loads(raw_body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=400, detail="INVALID_WEBHOOK_JSON") from exc

    handled = 0
    for entry in payload.get("entry", []):
        for change in entry.get("changes", []):
            value = change.get("value", {})
            for message in value.get("messages", []) or []:
                message_id = str(message.get("id", ""))
                if not message_id or message_id in _seen_message_ids:
                    continue
                _seen_message_ids.add(message_id)
                if len(_seen_message_ids) > _MAX_SEEN_IDS:
                    _seen_message_ids.clear()
                    _seen_message_ids.add(message_id)

                # Only reply to incoming text messages. Ignore media/status events.
                if message.get("type") != "text":
                    continue
                sender = _normalize_phone(str(message.get("from", "")))
                incoming_text = str(message.get("text", {}).get("body", "")).strip()
                if not incoming_text:
                    continue
                try:
                    reply = _ai_reply(incoming_text)
                    _send_text(sender, reply)
                    handled += 1
                except Exception:
                    logger.exception("WhatsApp AI auto-reply failed for inbound message")
                    # Do not leak provider errors or tokens in the webhook response.
    return {"success": True, "received": True, "auto_replies_sent": handled}


@router.post("/send-approved-template")
def send_approved_outreach_template(payload: OutreachTemplateRequest):
    """Send one approved template to one explicitly opted-in recipient.

    Callers must have authenticated via the app's private-by-default middleware.
    This is deliberately not a bulk-send endpoint.
    """
    if payload.opt_in_confirmed is not True:
        raise HTTPException(
            status_code=403,
            detail="RECIPIENT_OPT_IN_REQUIRED",
        )
    recipient = _normalize_phone(payload.recipient)
    try:
        result = _send_approved_template(
            recipient=recipient,
            template_name=payload.template_name,
            language=payload.language,
            parameters=payload.parameters,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return {
        "success": True,
        "recipient": recipient,
        "status": "SUBMITTED_TO_WHATSAPP",
        "provider_response": result,
        "note": "Provider acceptance is not proof of delivery; check WhatsApp message-status webhooks.",
    }


@router.get("/status")
def whatsapp_ai_status():
    required = [
        "WHATSAPP_ACCESS_TOKEN",
        "WHATSAPP_PHONE_NUMBER_ID",
        "WHATSAPP_APP_SECRET",
        "WHATSAPP_VERIFY_TOKEN",
        "WHATSAPP_GRAPH_API_VERSION",
        "OPENAI_API_KEY",
        "WHATSAPP_OUTREACH_TEMPLATE_NAME",
    ]
    configured = [name for name in required if _env(name)]
    missing = [name for name in required if not _env(name)]
    return {
        "success": True,
        "module": "SUPREME ECOSYSTEM WHATSAPP AI",
        "status": "CONFIGURED_NOT_END_TO_END_TESTED" if not missing else "SETUP_REQUIRED",
        "configured_variables": configured,
        "missing_variables": missing,
        "incoming_ai_replies": not any(
            not _env(name) for name in [
                "WHATSAPP_ACCESS_TOKEN",
                "WHATSAPP_PHONE_NUMBER_ID",
                "WHATSAPP_APP_SECRET",
                "WHATSAPP_VERIFY_TOKEN",
                "WHATSAPP_GRAPH_API_VERSION",
                "OPENAI_API_KEY",
            ]
        ),
        "outbound_mode": "SINGLE_APPROVED_TEMPLATE_TO_EXPLICIT_OPT_IN_ONLY",
        "bulk_messaging": False,
        "automatic_contact_saving": False,
    }
}
