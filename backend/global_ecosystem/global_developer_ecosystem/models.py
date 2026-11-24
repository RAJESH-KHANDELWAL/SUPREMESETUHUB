"""Typed records for developer capabilities."""
from dataclasses import dataclass, field
from typing import Any
from .catalog import DEVELOPER_DOMAINS, GEOGRAPHIC_SCOPES, MATURITY_LEVELS
@dataclass(frozen=True)
class DeveloperCapability:
    capability_id: str
    domain: str
    name: str
    geographic_scope: str = "global_cross_border"
    maturity: str = "normal"
    adult_only: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)
    def __post_init__(self):
        if not self.capability_id.strip() or not self.name.strip(): raise ValueError("capability_id and name are required")
        if self.domain not in DEVELOPER_DOMAINS: raise ValueError(f"Unknown domain: {self.domain}")
        if self.geographic_scope not in GEOGRAPHIC_SCOPES: raise ValueError("Unsupported geographic scope")
        if self.maturity not in MATURITY_LEVELS: raise ValueError("Unsupported maturity")
        if self.adult_only and self.domain != "adult_only_content_technology": raise ValueError("Adult-only capabilities must use the dedicated adult domain")
