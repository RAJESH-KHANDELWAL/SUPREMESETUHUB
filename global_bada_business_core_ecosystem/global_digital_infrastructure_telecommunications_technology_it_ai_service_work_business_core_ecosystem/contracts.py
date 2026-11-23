"""Business context and service/work engagement contracts."""
from dataclasses import dataclass, field
@dataclass(frozen=True)
class TechnologyBusinessContext:
    tenant_id: str
    actor_id: str
    jurisdiction: str
    def validate(self) -> None:
        if not self.tenant_id.strip(): raise ValueError("TENANT_ID_REQUIRED")
        if not self.actor_id.strip(): raise ValueError("ACTOR_ID_REQUIRED")
        if not self.jurisdiction.strip(): raise ValueError("JURISDICTION_REQUIRED")
@dataclass(frozen=True)
class ServiceWorkEngagement:
    record_id: str
    domain_id: str
    service_type: str
    description: str
    jurisdiction: str
    provider_id: str | None = None
    lifecycle_status: str = "DRAFT"
    evidence_references: tuple[str, ...] = field(default_factory=tuple)
    approval_reference: str | None = None
    risk_level: str = "UNASSESSED"
