"""SECURITY-owned value objects. Never store credentials or secret material here."""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class SecurityAsset:
    security_id: str
    name: str
    asset_type: str
    scope: str = "APPLICATION"
    status: str = "REGISTERED"
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        for field_name in ("security_id", "name", "asset_type", "scope"):
            value = str(getattr(self, field_name) or "").strip()
            if not value:
                raise ValueError(f"{field_name} is required")
            setattr(self, field_name, value)
        self.status = str(self.status or "REGISTERED").strip().upper()
        if not isinstance(self.metadata, dict):
            raise TypeError("metadata must be a dictionary")
        forbidden = {"password", "secret", "token", "api_key", "private_key", "credential"}
        if forbidden.intersection(k.lower() for k in self.metadata):
            raise ValueError("SECURITY_ASSET_METADATA_MUST_NOT_CONTAIN_SECRETS")

@dataclass(frozen=True)
class SecurityHealth:
    status: str
    registered_assets: int
    configured_providers: int
    external_probes: str = "NOT_ATTEMPTED"

__all__ = ["SecurityAsset", "SecurityHealth"]
