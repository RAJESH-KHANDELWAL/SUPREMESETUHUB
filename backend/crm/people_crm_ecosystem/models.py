"""Normalized contact record for the people-facing CRM ecosystem."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class PeopleContact:
    """A normalized people record, independent of any external provider schema."""

    contact_id: str
    full_name: str
    email: str = ""
    phone: str = ""
    organization: str = ""
    source: str = "MANUAL"
    external_id: str = ""
    notes: str = ""
    tags: tuple[str, ...] = field(default_factory=tuple)
    consent_to_contact: bool = False
    contact_status: str = "ACTIVE"

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-friendly representation."""
        result = asdict(self)
        result["tags"] = list(self.tags)
        return result

    def validate(self) -> "PeopleContact":
        if not self.contact_id.strip():
            raise ValueError("contact_id is required")
        if not self.full_name.strip():
            raise ValueError("full_name is required")
        if self.contact_status not in {"ACTIVE", "DO_NOT_CONTACT", "ARCHIVED"}:
            raise ValueError("Unsupported contact_status")
        if self.contact_status == "DO_NOT_CONTACT" and self.consent_to_contact:
            raise ValueError("DO_NOT_CONTACT records cannot have contact consent enabled")
        return self
