"""Registration input validation and draft creation.

No provider account, payment gateway, external API, or database connection is
assumed. The returned draft is suitable for a separately authorized API/CORE
workflow; it is not a completed registration or proof of payment.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import re
from typing import Any

from ..courses.catalog import get_course

_EMAIL = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
_PHONE = re.compile(r"^\+?[0-9][0-9\s-]{7,17}$")
_PINCODE = re.compile(r"^[0-9]{4,10}$")


@dataclass(frozen=True, slots=True)
class RegistrationDraft:
    registration_id: str
    program_id: str
    full_name: str
    mobile_number: str
    email: str
    pincode: str
    status: str
    created_at: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def validate_registration(payload: dict[str, Any]) -> dict[str, str]:
    """Return field-level validation errors without retaining submitted data."""
    if not isinstance(payload, dict):
        return {"payload": "Registration payload must be an object."}
    errors: dict[str, str] = {}
    name = str(payload.get("full_name", "")).strip()
    phone = str(payload.get("mobile_number", "")).strip()
    email = str(payload.get("email", "")).strip()
    pincode = str(payload.get("pincode", "")).strip()
    if len(name) < 2 or len(name) > 120:
        errors["full_name"] = "Name must contain 2 to 120 characters."
    if not _PHONE.fullmatch(phone):
        errors["mobile_number"] = "Enter a valid phone number with country code if needed."
    if not _EMAIL.fullmatch(email):
        errors["email"] = "Enter a valid email address."
    if not _PINCODE.fullmatch(pincode):
        errors["pincode"] = "Pincode must contain 4 to 10 digits."
    return errors


def create_registration_draft(program_id: str, payload: dict[str, Any]) -> RegistrationDraft:
    """Validate input and create a non-persistent, unsubmitted registration draft."""
    normalized_id = (program_id or "").strip().lower()
    if get_course(normalized_id) is None:
        raise ValueError("Unknown program_id.")
    errors = validate_registration(payload)
    if errors:
        raise ValueError("; ".join(f"{key}: {value}" for key, value in errors.items()))
    import uuid
    return RegistrationDraft(
        registration_id=f"bbreg_{uuid.uuid4().hex}",
        program_id=normalized_id,
        full_name=str(payload["full_name"]).strip(),
        mobile_number=str(payload["mobile_number"]).strip(),
        email=str(payload["email"]).strip().lower(),
        pincode=str(payload["pincode"]).strip(),
        status="DRAFT_NOT_SUBMITTED",
        created_at=datetime.now(timezone.utc).isoformat(),
    )
