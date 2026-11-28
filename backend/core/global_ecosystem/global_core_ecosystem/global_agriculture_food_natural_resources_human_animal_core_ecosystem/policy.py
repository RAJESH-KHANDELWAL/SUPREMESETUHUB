"""Policy guardrails; metadata registration is not operational authorization."""
from __future__ import annotations

SENSITIVE_MARKERS = ("PERSONAL_DATA", "HEALTH", "VETERINARY", "BIOMETRIC", "FINANCE", "LOCATION", "CHILD")

class CorePolicyError(PermissionError):
    pass

def classify_capability(capability: str) -> str:
    key = capability.strip().upper()
    if not key:
        raise ValueError("capability is required")
    return "REQUIRES_EXPLICIT_AUTHORIZATION_AND_COMPLIANCE" if any(x in key for x in SENSITIVE_MARKERS) else "STANDARD_GOVERNED_CAPABILITY"

def safe_metadata(value):
    blocked = {"token", "access_token", "refresh_token", "secret", "client_secret", "api_key", "password"}
    if isinstance(value, dict):
        return {k: ("[REDACTED]" if k.casefold() in blocked else safe_metadata(v)) for k, v in value.items()}
    if isinstance(value, list):
        return [safe_metadata(item) for item in value]
    return value
