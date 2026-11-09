"""Defensive, fail-closed SECURITY operation dispatch."""
from typing import Any
from .catalog import get_capability, list_capabilities

class SecurityOperationError(RuntimeError):
    pass
class SecurityCapabilityNotConfigured(SecurityOperationError):
    pass
class SecurityAuthorizationRequired(SecurityOperationError):
    pass

class SecurityOperationService:
    domain = "SECURITY"
    ecosystem = "GLOBAL_SECURITY_ECOSYSTEM"

    def __init__(self, providers, *, authorizer=None):
        self.providers = providers
        self.authorizer = authorizer

    def execute(self, provider_id: str, capability: str, operation: str, payload: dict[str, Any] | None = None, *, principal=None):
        descriptor = get_capability(capability)
        if descriptor is None:
            raise ValueError(f"Unknown SECURITY capability: {capability}")
        if descriptor.access != "READ_ONLY":
            raise SecurityAuthorizationRequired("Only catalogued read-only capabilities are enabled by default")
        if not callable(self.authorizer):
            raise SecurityAuthorizationRequired("SECURITY authorizer is not configured; operation denied")
        if self.authorizer(principal, descriptor.key, provider_id) is not True:
            raise SecurityAuthorizationRequired("SECURITY authorization denied")
        adapter = self.providers.get(provider_id)
        if adapter is None:
            raise SecurityCapabilityNotConfigured(f"{provider_id} provider is not configured")
        operation_name = str(operation or "").strip()
        if not operation_name:
            raise ValueError("operation is required")
        result = adapter.execute(operation_name, dict(payload or {}))
        return {"domain": self.domain, "ecosystem": self.ecosystem, "provider_id": provider_id, "capability": descriptor.key, "operation": operation_name, "access": descriptor.access, "status": "COMPLETED", "result": result}

    def status(self):
        return {"domain": self.domain, "capabilities": [{"key": x.key, "description": x.description, "access": x.access} for x in list_capabilities()], "authorization_configured": callable(self.authorizer)}

__all__ = ["SecurityOperationService", "SecurityOperationError", "SecurityCapabilityNotConfigured", "SecurityAuthorizationRequired"]
