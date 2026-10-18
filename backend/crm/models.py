"""Canonical contact data model for the CRM module."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class Contact:
    """A normalized contact record; private-owner CRM storage stays separate."""

    contact_id: str
    full_name: str
    email: str = ""
    phone: str = ""
    whatsapp_phone: str = ""
    organization: str = ""
    address: str = ""
    city: str = ""
    pincode: str = ""
    designation: str = ""
    verification_status: str = "UNVERIFIED"
    verification_evidence: str = ""
    verified_at: str | None = None
    source: str = "MANUAL"
    external_id: str = ""
    notes: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)
    consent_to_contact: bool = False
    contact_status: str = "ACTIVE"
    category: str = "UNCATEGORIZED"
    follow_up_at: str | None = None

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["tags"] = list(self.tags)
        return result

    def validate(self) -> "Contact":
        if not self.contact_id.strip():
            raise ValueError("contact_id is required")
        if not self.full_name.strip():
            raise ValueError("full_name is required")
        if self.contact_status not in {"ACTIVE", "DO_NOT_CONTACT", "ARCHIVED"}:
            raise ValueError("Unsupported contact_status")
        if self.verification_status not in {"UNVERIFIED", "PENDING", "VERIFIED", "INVALID", "DO_NOT_USE"}:
            raise ValueError("Unsupported verification_status")
        if self.verification_status == "VERIFIED" and not (self.verification_evidence.strip() and self.verified_at):
            raise ValueError("VERIFIED status requires verification_evidence and verified_at")
        if self.contact_status == "DO_NOT_CONTACT" and self.consent_to_contact:
            raise ValueError("DO_NOT_CONTACT records cannot have contact consent enabled")
        return self
