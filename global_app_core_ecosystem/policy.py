"""Safe metadata projection for Global App Core; no runtime authorization."""
from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

_SECRET_KEY_PARTS = (
    "password", "secret", "token", "apikey", "privatekey",
    "authorization", "credential", "clientsecret",
)
_PROVIDER_FIELDS = (
    "id", "name", "category", "origin", "ecosystem_kind",
    "application_examples", "integration_status", "live_connection_verified",
)


def is_secret_key(key: object) -> bool:
    normalized = re.sub(r"[^a-z0-9]", "", str(key).casefold())
    return any(part in normalized for part in _SECRET_KEY_PARTS)


def redact_secrets(value: Any) -> Any:
    """Return a recursively copied value with secret-bearing keys omitted."""
    if isinstance(value, Mapping):
        return {
            str(key): redact_secrets(item)
            for key, item in value.items()
            if not is_secret_key(key)
        }
    if isinstance(value, tuple):
        return [redact_secrets(item) for item in value]
    if isinstance(value, list):
        return [redact_secrets(item) for item in value]
    return value


def safe_provider_snapshot(provider: Mapping[str, Any]) -> dict[str, Any]:
    """Expose only documented provider catalog fields, then redact recursively."""
    allowed = {key: provider[key] for key in _PROVIDER_FIELDS if key in provider}
    return redact_secrets(allowed)


def readiness_for_provider(provider: Mapping[str, Any]) -> str:
    status = provider.get("integration_status")
    verified = provider.get("live_connection_verified") is True
    if status == "live_verified" and verified:
        return "LIVE_VERIFIED"
    if status == "configured":
        return "CONFIGURED"
    if status == "scaffold":
        return "SCAFFOLD"
    if status == "integration_in_progress":
        return "DOCUMENTED"
    return "CATALOG_ONLY"


__all__ = [
    "is_secret_key", "redact_secrets", "safe_provider_snapshot",
    "readiness_for_provider",
]
