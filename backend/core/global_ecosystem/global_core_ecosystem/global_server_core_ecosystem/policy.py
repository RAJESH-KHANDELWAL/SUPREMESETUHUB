"""Server Core policy checks; not a substitute for API authentication or authorization."""
from __future__ import annotations
from typing import Any

SUPPORTED_ENVIRONMENTS = ("development", "test", "staging", "production")
SUPPORTED_SERVER_TYPES = (
    "vps", "cloud", "web", "cloud_web", "dedicated", "edge",
    "application", "vpn", "database",
)
SUPPORTED_LIFECYCLE_STATES = (
    "REGISTERED", "PENDING", "AUTHORIZED", "PROVISIONING",
    "ACTIVE", "DEGRADED", "DISABLED", "FAILED", "DECOMMISSIONED",
)

SENSITIVE_CAPABILITY_MARKERS = ("ADMIN","DELETE","WRITE","PROVISION","DEPLOY","DESTROY","BACKUP","RESTORE","NETWORK_CHANGE","FIREWALL","IAM","PERMISSION","SECRET","KEY","BILLING","PRODUCTION")
BLOCKED_KEYS = {"token","access_token","refresh_token","client_secret","api_key","secret","password","private_key","credential"}

class ServerCorePolicyError(PermissionError):
    """Raised when a Server Core metadata policy is violated."""

class ServerCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None:
            raise ServerCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        validator = getattr(context, "validate", None)
        if not callable(validator):
            raise ServerCorePolicyError("INVALID_TENANT_CONTEXT")
        validator()

    @staticmethod
    def validate_capability(provider: dict[str, Any], capability: str) -> None:
        if not provider.get("enabled", True):
            raise ServerCorePolicyError("PROVIDER_MODULE_DISABLED")
        if capability not in set(provider.get("capabilities", [])):
            raise ServerCorePolicyError("CAPABILITY_NOT_REGISTERED")

    @staticmethod
    def classify_capability(capability: str) -> str:
        upper = str(capability).upper()
        return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(marker in upper for marker in SENSITIVE_CAPABILITY_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"

    @staticmethod
    def redact(value: Any) -> Any:
        if isinstance(value, dict):
            return {key: ServerCorePolicy.redact(item) for key,item in value.items()
                    if str(key).casefold() not in BLOCKED_KEYS and not any(x in str(key).casefold() for x in ("secret","token","password","credential","private_key"))}
        if isinstance(value, list):
            return [ServerCorePolicy.redact(item) for item in value]
        if isinstance(value, tuple):
            return [ServerCorePolicy.redact(item) for item in value]
        return value

    @staticmethod
    def safe_summary(item: dict[str, Any]) -> dict[str, Any]:
        return ServerCorePolicy.redact(item)

# Backward-compatible policy facade retained for existing Server Core consumers.
from dataclasses import dataclass

@dataclass(frozen=True)
class ServerPolicy:
    require_explicit_authorization: bool = True
    allow_automatic_provisioning: bool = False
    require_region: bool = True
    require_environment: bool = True
    production_requires_approval: bool = True

    def validate(self, *, environment: str, authorized: bool = False) -> None:
        env = str(environment).strip().lower()
        if self.require_environment and env not in SUPPORTED_ENVIRONMENTS:
            raise ValueError(f"Unsupported environment: {environment}")
        if self.require_explicit_authorization and not authorized:
            raise PermissionError("Server is not explicitly authorized")
        if env == "production" and self.production_requires_approval and not authorized:
            raise PermissionError("Production server requires explicit approval")
