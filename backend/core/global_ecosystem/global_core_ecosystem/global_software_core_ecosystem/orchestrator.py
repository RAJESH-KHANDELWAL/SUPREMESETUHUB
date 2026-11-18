"""Build deterministic plans; execution is intentionally outside this core."""

from __future__ import annotations

from .catalog import get_provider


def build_plan(provider_id: str, capability: str, *, tenant_id: str) -> dict:
    if not isinstance(provider_id, str) or not provider_id.strip():
        raise ValueError("provider_id is required")
    normalized_provider_id = provider_id.strip().lower()
    provider = get_provider(normalized_provider_id)
    if provider is None:
        raise KeyError(f"Unknown software provider: {normalized_provider_id}")

    if not isinstance(capability, str) or not capability.strip():
        raise ValueError("capability is required")
    normalized_capability = capability.strip().upper()
    if normalized_capability not in provider["capabilities"]:
        raise ValueError(
            f"Capability {normalized_capability!r} is not registered for {normalized_provider_id!r}"
        )

    if not isinstance(tenant_id, str) or not tenant_id.strip():
        raise ValueError("tenant_id is required")
    normalized_tenant_id = tenant_id.strip()

    return {
        "provider_id": normalized_provider_id,
        "capability": normalized_capability,
        "tenant_id": normalized_tenant_id,
        "status": "PLAN_ONLY",
        "execution_enabled": False,
        "live_connection_verified": False,
    }
