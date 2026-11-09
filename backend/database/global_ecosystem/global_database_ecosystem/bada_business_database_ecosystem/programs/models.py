"""Data contract for persisted Bada Business program snapshots."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any
import json


VALID_PROGRAM_STATUSES = frozenset({
    "AVAILABLE", "UPCOMING", "PAST_EVENT_DATE", "UNCONFIRMED", "UNKNOWN"
})


@dataclass(frozen=True)
class BadaBusinessProgramRecord:
    owner_user_id: str
    program_id: str
    program_name: str
    program_status: str = "UNCONFIRMED"
    provider_id: str = "bada_business"
    source_catalog: str = "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog"
    source_version: str = ""
    snapshot: dict[str, Any] = field(default_factory=dict)

    def validate(self):
        for field_name in ("owner_user_id", "program_id", "program_name", "provider_id"):
            value = getattr(self, field_name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field_name} is required")
        if self.program_status not in VALID_PROGRAM_STATUSES:
            raise ValueError("Unsupported program_status")
        if not isinstance(self.snapshot, dict):
            raise ValueError("snapshot must be a mapping")
        # Ensure payload is JSON serializable before it reaches the repository.
        json.dumps(self.snapshot, ensure_ascii=False)
        return self

    def to_dict(self):
        return asdict(self)
