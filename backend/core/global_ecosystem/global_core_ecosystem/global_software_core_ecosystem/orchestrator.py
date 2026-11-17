"""Build deterministic plans; execution is intentionally outside this core."""

from __future__ import annotations

from .catalog import get_provider


def build_plan(provider_id: str, capability: str, *, tenant_id: str) -> dict:
    provider = get_provider(provider_id)
    if provider is None:
        raise KeyError(f"Unknown software provider: {provider_id}")
    if capability not in provider["capabilities"]:
        raise ValueError(f"Capability {capability!r} is not registered for {provider_id!r}")
    if not tenant_id.strip():
        raise ValueError("tenant_id is required")
    return {
        "provider_id": provider_id,
        "capability": capability,
        "tenant_id": tenant_id,
        "status": "PLAN_ONLY",
        "execution_enabled": False,
        "live_connection_verified": False,
    }
