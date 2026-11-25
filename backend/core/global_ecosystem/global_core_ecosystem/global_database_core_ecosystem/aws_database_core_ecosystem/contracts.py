"""Provider-neutral database Core contracts; no driver or API dependency."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ProviderRecord:
    provider_id: str
    provider_name: str
    implementation_status: str = "CATALOG_ONLY"
    live_connection_verified: bool = False

@dataclass(frozen=True)
class DatabaseCapability:
    capability_id: str
    description: str
    enabled: bool = False

@dataclass(frozen=True)
class Readiness:
    ready: bool
    reason: str
    live_connection_verified: bool = False


def safe_metadata(value: dict[str, Any]) -> dict[str, Any]:
    """Return metadata without common secret-bearing keys."""
    blocked = {"password", "secret", "token", "api_key", "private_key", "connection_string"}
    return {k: v for k, v in value.items() if k.casefold() not in blocked}
