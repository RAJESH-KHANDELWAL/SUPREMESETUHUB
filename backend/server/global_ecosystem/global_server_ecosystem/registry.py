"""Compatibility facade; canonical implementation is owned by backend.SERVER."""
from backend.SERVER.GLOBAL_ECOSYSTEM.GLOBAL_SERVER_ECOSYSTEM.registry import (
    PROVIDERS, ROOT_ECOSYSTEM_ID, SERVER_ECOSYSTEM_ID, SERVICE_TYPES,
    ServerRegistrationRegistry, get_provider, get_service_type,
    list_providers, list_service_types,
)

__all__ = [
    "ROOT_ECOSYSTEM_ID", "SERVER_ECOSYSTEM_ID", "PROVIDERS", "SERVICE_TYPES",
    "ServerRegistrationRegistry", "list_providers", "get_provider",
    "list_service_types", "get_service_type",
]
