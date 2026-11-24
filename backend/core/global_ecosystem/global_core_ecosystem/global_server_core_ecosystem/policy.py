"""Provider-neutral server lifecycle and deployment policy contracts."""
from __future__ import annotations
from dataclasses import dataclass

SUPPORTED_ENVIRONMENTS = ("development", "test", "staging", "production")
SUPPORTED_SERVER_TYPES = (
    "vps", "cloud", "web", "cloud_web", "dedicated", "edge",
    "application", "vpn", "database",
)
SUPPORTED_LIFECYCLE_STATES = (
    "REGISTERED", "PENDING", "AUTHORIZED", "PROVISIONING",
    "ACTIVE", "DEGRADED", "DISABLED", "FAILED", "DECOMMISSIONED",
)

@dataclass(frozen=True)
class ServerPolicy:
    require_explicit_authorization: bool = True
    allow_automatic_provisioning: bool = False
    require_region: bool = True
    require_environment: bool = True
    production_requires_approval: bool = True

    def validate(self, *, environment: str, authorized: bool = False) -> None:
        env = str(environment).strip().lower()
        if env not in SUPPORTED_ENVIRONMENTS:
            raise ValueError(f"Unsupported environment: {environment}")
        if self.require_explicit_authorization and not authorized:
            raise PermissionError("Server is not explicitly authorized")
        if env == "production" and self.production_requires_approval and not authorized:
            raise PermissionError("Production server requires explicit approval")
