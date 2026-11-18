"""Provider-neutral contracts; never hold credentials or provider payloads."""
from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(frozen=True)
class ProviderDescriptor:
    provider_id: str
    display_name: str
    category: str = "GENERAL"
    status: str = "CATALOG_ONLY"
    live_connection_verified: bool = False

    def __post_init__(self) -> None:
        if not self.provider_id.strip() or not self.display_name.strip():
            raise ValueError("provider_id and display_name must be non-empty")

@dataclass(frozen=True)
class IntegrationDescriptor:
    integration_id: str
    display_name: str
    domain_id: str
    capabilities: tuple[str, ...] = field(default_factory=tuple)
    sensitivity: str = "STANDARD"
    age_restricted: bool = False
    consent_required: bool = False
    status: str = "CORE_CATALOG_ONLY"

    def __post_init__(self) -> None:
        for name in ("integration_id", "display_name", "domain_id"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must be a non-empty string")
        if self.age_restricted and not self.consent_required:
            raise ValueError("age-restricted integration domains must require consent")
