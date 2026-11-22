"""Metadata-only provider resolution; no network or database driver calls."""
from .manager import get_provider


def resolve_provider(provider_id: str):
    provider = get_provider(provider_id)
    if provider is None:
        return {
            "ready": False,
            "reason": "provider_not_registered",
            "provider": None,
            "live_connection_verified": False,
        }
    return {
        "ready": False,
        "reason": "catalog_only_no_runtime_adapter",
        "provider": provider,
        "live_connection_verified": False,
    }
