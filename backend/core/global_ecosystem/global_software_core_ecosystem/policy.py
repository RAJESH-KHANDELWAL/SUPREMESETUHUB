"""Software Core policy guardrails; not an OS or SaaS authorization engine."""
from __future__ import annotations
from typing import Any
SENSITIVE_MARKERS=("ADMIN","DELETE","WRITE","PUBLISH","INSTALL","UNINSTALL","LICENSE","BILLING","KEY","SECRET","DEPLOY")
class SoftwareCorePolicy:
    @staticmethod
    def require_tenant_context(context: Any) -> None:
        if context is None or not callable(getattr(context,"validate",None)): raise PermissionError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
        context.validate()
    @staticmethod
    def classify_capability(capability: str) -> str:
        return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION" if any(marker in capability.upper() for marker in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AUTHORIZATION"
    @staticmethod
    def safe_provider_summary(provider: dict[str, Any]) -> dict[str, Any]:
        blocked={"token","access_token","refresh_token","client_secret","api_key","secret","password"}
        return {k:v for k,v in provider.items() if k.casefold() not in blocked}
