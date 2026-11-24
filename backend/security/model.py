"""Typed models for security policy records and runtime security state."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class SecurityInfo:
    """Persisted security policy metadata.

    Fields retain defaults for compatibility with earlier SecurityInfo callers.
    """

    security_name: str = "SUPREMESETUHUB SECURITY"
    version: str = "1.0.0"
    status: str = "CONFIGURATION_REQUIRED"
    security_id: str = ""
    name: str = ""
    security_type: str = ""
    resource_type: str = ""
    resource_id: str = ""
    provider: str = ""
    enabled: bool = False
    description: str = ""
    created_at: str = ""
    updated_at: str = ""

    @classmethod
    def from_record(cls, record: Any) -> "SecurityInfo":
        data = dict(record)
        if "enabled" in data:
            data["enabled"] = bool(data["enabled"])
        allowed = cls.__dataclass_fields__.keys()
        return cls(**{key: value for key, value in data.items() if key in allowed})


@dataclass(frozen=True, slots=True)
class SecurityCheck:
    """Result of a non-invasive security configuration check."""

    name: str
    status: str
    detail: str = ""

    def as_dict(self) -> dict[str, str]:
        return {"name": self.name, "status": self.status, "detail": self.detail}


@dataclass(frozen=True, slots=True)
class SecurityHealth:
    """Aggregate security readiness report; never implies certification."""

    status: str
    checks: tuple[SecurityCheck, ...]
    checked_at: datetime

    def as_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "checked_at": self.checked_at.isoformat(),
            "checks": [check.as_dict() for check in self.checks],
        }
