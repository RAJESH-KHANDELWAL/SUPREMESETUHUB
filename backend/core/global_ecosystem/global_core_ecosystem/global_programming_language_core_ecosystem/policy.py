"""CORE policy checks; never substitutes for runtime, compiler or package authorization."""
from __future__ import annotations
from collections.abc import Mapping
from copy import deepcopy
from typing import Any

SENSITIVE_KEYS = frozenset({"api_key","access_token","refresh_token","client_secret","token","secret","password","private_key","authorization"})
SENSITIVE_MARKERS = ("ADMIN", "DELETE", "WRITE", "PUBLISH", "INSTALL", "EXECUTE", "DEPLOY", "CREDENTIAL")

class ProgrammingLanguagePolicyError(PermissionError):
    pass

def redact_sensitive_metadata(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(k): redact_sensitive_metadata(v) for k,v in value.items() if str(k).casefold() not in SENSITIVE_KEYS}
    if isinstance(value, list):
        return [redact_sensitive_metadata(v) for v in value]
    if isinstance(value, tuple):
        return tuple(redact_sensitive_metadata(v) for v in value)
    return deepcopy(value)

def require_tenant_context(context: Any) -> None:
    if context is None or not callable(getattr(context, "validate", None)):
        raise ProgrammingLanguagePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
    try:
        context.validate()
    except (TypeError, ValueError) as exc:
        raise ProgrammingLanguagePolicyError(str(exc)) from exc

def validate_capability(module: dict[str, Any], capability: str) -> None:
    if not module.get("enabled", True):
        raise ProgrammingLanguagePolicyError("MODULE_DISABLED")
    if capability not in set(module.get("capabilities", [])):
        raise ProgrammingLanguagePolicyError("CAPABILITY_NOT_REGISTERED")

def classify_capability(capability: str) -> str:
    return ("SENSITIVE_REQUIRES_EXPLICIT_APPLICATION_AUTHORIZATION"
            if any(marker in capability.upper() for marker in SENSITIVE_MARKERS)
            else "STANDARD_REQUIRES_TENANT_AUTHORIZATION")

def safe_module_summary(module: dict[str, Any]) -> dict[str, Any]:
    return redact_sensitive_metadata(module)
