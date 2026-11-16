"""Safe metadata projection and readiness policy for Global Cloud Core."""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

_SECRET_KEY_PARTS = (
    "password", "secret", "token", "api_key", "apikey", "private_key",
    "authorization", "credential", "access_key", "secret_key",
)
_PROVIDER_FIELDS = (
    "id", "name", "origin", "capabilities", "integration_status",
    "live_connection_verified",
)
_WORKLOAD_FIELDS = (
    "id", "name", "tier", "regions", "workloads", "adult_industry",
    "guardrails", "integration_status", "live_provider_connection_verified",
)


def is_secret_key(key: object) -> bool:
    normalized = str(key).strip().lower().replace("-", "_")
    return any(part in normalized for part in _SECRET_KEY_PARTS)


def redact_secrets(value: Any) -> Any:
    """Recursively copy mappings and sequences while omitting secret keys."""
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
    allowed = {key: provider[key] for key in _PROVIDER_FIELDS if key in provider}
    return redact_secrets(allowed)


def safe_workload_snapshot(workload: Mapping[str, Any]) -> dict[str, Any]:
    allowed = {key: workload[key] for key in _WORKLOAD_FIELDS if key in workload}
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
    "safe_workload_snapshot", "readiness_for_provider",
]
