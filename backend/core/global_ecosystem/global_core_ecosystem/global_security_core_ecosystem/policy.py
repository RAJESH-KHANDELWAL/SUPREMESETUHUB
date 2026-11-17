"""Global Security Core policy metadata and redaction guardrails.

These checks classify metadata and validate request shape only. They do not
authenticate actors, grant permissions, enforce controls or certify compliance.
"""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import re
from typing import Any


SENSITIVE_KEY_PARTS = (
    "apikey",
    "token",
    "secret",
    "password",
    "privatekey",
    "authorization",
    "email",
    "phone",
    "mobile",
    "address",
    "governmentid",
    "passportnumber",
    "aadhaarnumber",
    "pannumber",
)
HIGH_RISK = (
    "ADMIN",
    "DELETE",
    "WRITE",
    "PUBLISH",
    "KEY_EXPORT",
    "POLICY_CHANGE",
    "ROLE_GRANT",
    "CREDENTIAL",
)


class SecurityPolicyError(PermissionError):
    """Raised when a Core metadata policy check fails."""


def _is_sensitive_key(key: object) -> bool:
    normalized = re.sub(r"[^a-z0-9]", "", str(key).casefold())
    return any(part in normalized for part in SENSITIVE_KEY_PARTS)


def redact_sensitive_metadata(value: Any) -> Any:
    """Return a defensive copy without common secret or personal-data fields."""
    if isinstance(value, Mapping):
        return {
            str(key): redact_sensitive_metadata(item)
            for key, item in value.items()
            if not _is_sensitive_key(key)
        }
    if isinstance(value, list):
        return [redact_sensitive_metadata(item) for item in value]
    if isinstance(value, tuple):
        return tuple(redact_sensitive_metadata(item) for item in value)
    return deepcopy(value)


def require_tenant_context(context: Any) -> None:
    """Validate required context fields; do not treat this as authentication."""
    if context is None or not callable(getattr(context, "validate", None)):
        raise SecurityPolicyError("TENANT_CONTEXT_REQUIRED")
    try:
        context.validate()
    except (TypeError, ValueError) as exc:
        raise SecurityPolicyError(str(exc)) from exc


def classify_capability(capability: str) -> str:
    """Classify capability risk for downstream authorization layers."""
    upper = capability.upper()
    return (
        "HIGH_RISK_REQUIRES_EXPLICIT_EXTERNAL_AUTHORIZATION"
        if any(marker in upper for marker in HIGH_RISK)
        else "TENANT_AUTHORIZATION_REQUIRED"
    )


def validate_capability(provider: dict[str, Any], capability: str) -> None:
    """Check registration metadata, not the caller's actual permission."""
    if not provider.get("enabled", True):
        raise SecurityPolicyError("PROVIDER_DISABLED")
    if capability not in set(provider.get("capabilities", [])):
        raise SecurityPolicyError("CAPABILITY_NOT_REGISTERED")


def safe_provider_summary(provider: dict[str, Any]) -> dict[str, Any]:
    """Return provider metadata after recursive sensitive-field redaction."""
    return redact_sensitive_metadata(provider)


def security_baseline() -> dict[str, bool]:
    """Return declared baseline requirements, not verified control status."""
    return {
        "least_privilege": True,
        "tenant_isolation_required": True,
        "mfa_recommended": True,
        "zero_trust_principle": True,
        "secrets_in_core": False,
        "auditability_required": True,
        "independent_runtime_enforcement_required": True,
    }
