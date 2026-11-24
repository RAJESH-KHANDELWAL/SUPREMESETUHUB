"""Security CORE policy metadata; not a substitute for enforcement."""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import re

SENSITIVE_KEY_PARTS = (
    "apikey", "token", "secret", "password", "privatekey", "authorization",
    "email", "phone", "mobile", "address", "governmentid", "passportnumber",
    "aadhaarnumber", "pannumber",
)
HIGH_RISK = ("ADMIN", "DELETE", "WRITE", "PUBLISH", "KEY_EXPORT", "POLICY_CHANGE", "ROLE_GRANT", "CREDENTIAL")


class SecurityPolicyError(PermissionError):
    """Raised when CORE metadata policy validation fails."""


def _is_sensitive_key(key: object) -> bool:
    normalized = re.sub(r"[^a-z0-9]", "", str(key).casefold())
    return any(part in normalized for part in SENSITIVE_KEY_PARTS)


def redact_sensitive_metadata(value):
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


def require_tenant_context(context):
    # This checks structure only; it does not authenticate the actor or prove authorization.
    if context is None or not callable(getattr(context, "validate", None)):
        raise SecurityPolicyError("TENANT_CONTEXT_REQUIRED")
    try:
        context.validate()
    except (TypeError, ValueError) as exc:
        raise SecurityPolicyError(str(exc)) from exc


def classify_capability(capability):
    return (
        "HIGH_RISK_REQUIRES_EXPLICIT_EXTERNAL_AUTHORIZATION"
        if any(item in capability.upper() for item in HIGH_RISK)
        else "TENANT_AUTHORIZATION_REQUIRED"
    )


def validate_capability(provider, capability):
    if not provider.get("enabled", True):
        raise SecurityPolicyError("PROVIDER_DISABLED")
    if capability not in set(provider.get("capabilities", [])):
        raise SecurityPolicyError("CAPABILITY_NOT_REGISTERED")


def safe_provider_summary(provider):
    return redact_sensitive_metadata(provider)


def security_baseline():
    return {
        "least_privilege": True,
        "tenant_isolation_required": True,
        "mfa_recommended": True,
        "zero_trust_principle": True,
        "secrets_in_core": False,
        "auditability_required": True,
        "independent_runtime_enforcement_required": True,
    }
