"""Compatibility imports for the canonical SERVER ecosystem."""
from backend.SERVER.GLOBAL_ECOSYSTEM.GLOBAL_SERVER_ECOSYSTEM import (
    EcosystemService,
    ServerRegistrationRegistry,
    get_provider,
    get_service_type,
    list_providers,
    list_service_types,
)

__all__ = [
    "EcosystemService",
    "ServerRegistrationRegistry",
    "list_providers",
    "get_provider",
    "list_service_types",
    "get_service_type",
]
