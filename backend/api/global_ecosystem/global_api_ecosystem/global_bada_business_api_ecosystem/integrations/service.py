"""Service layer for the Bada Business provider integration registry."""
from .registry import get_integration, list_integrations, validate_integration_registry

def list_entries() -> list[dict[str, object]]:
    return list_integrations()

def get_entry(integration_id: str) -> dict[str, object] | None:
    return get_integration(integration_id)

def get_status() -> dict[str, object]:
    integrity = validate_integration_registry()
    return {
        "success": integrity["structurally_valid"],
        **integrity,
        "note": "This registry lists provider references only. No live API connection, credentials, partnership, or provider API support is implied.",
    }
