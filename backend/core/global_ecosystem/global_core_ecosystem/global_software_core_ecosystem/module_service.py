"""Provider metadata lifecycle service; persistence and network I/O are injected elsewhere."""

from __future__ import annotations

from .catalog import get_provider, list_providers


class SoftwareModuleService:
    def discover(self) -> list[dict]:
        return list_providers()

    def describe(self, provider_id: str) -> dict | None:
        return get_provider(provider_id)

    def lifecycle_status(self, provider_id: str) -> dict:
        provider = get_provider(provider_id)
        if provider is None:
            return {"provider_id": provider_id, "state": "NOT_REGISTERED"}
        return {
            "provider_id": provider_id,
            "state": provider["status"],
            "live_connection_verified": provider["live_connection_verified"],
        }
