"""Public emergency communication templates and channel metadata."""
from __future__ import annotations

CHANNELS = ("public_alert", "sms", "radio", "official_website",
            "verified_social_channel", "community_contact", "accessible_format")

def communication_channels() -> tuple[str, ...]:
    return CHANNELS

def build_message_record(message: str, language: str, issuing_authority: str) -> dict[str, str]:
    values = (message.strip(), language.strip(), issuing_authority.strip())
    if not all(values):
        raise ValueError("message, language and issuing_authority are required")
    return {
        "message": values[0],
        "language": values[1],
        "issuing_authority": values[2],
        "status": "DRAFT_REQUIRES_AUTHORIZATION",
    }
