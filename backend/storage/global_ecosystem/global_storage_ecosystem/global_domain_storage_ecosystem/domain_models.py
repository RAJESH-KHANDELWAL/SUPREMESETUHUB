"""Typed provider-neutral domain metadata records."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

def utc_now() -> str:
 return datetime.now(timezone.utc).isoformat()

@dataclass
class DomainRecord:
 domain_id: str
 domain_name: str
 record_type: str = "DOMAIN"
 jurisdiction: str = "GLOBAL"
 lifecycle_state: str = "UNKNOWN"
 provider_id: str | None = None
 metadata: dict[str, Any] = field(default_factory=dict)
 created_at: str = field(default_factory=utc_now)
 updated_at: str = field(default_factory=utc_now)
 def __post_init__(self) -> None:
  self.domain_id = self.domain_id.strip()
  self.domain_name = self.domain_name.strip().lower().rstrip(".")
  if not self.domain_id: raise ValueError("domain_id is required")
  if not self.domain_name or "." not in self.domain_name: raise ValueError("domain_name must be fully qualified")
