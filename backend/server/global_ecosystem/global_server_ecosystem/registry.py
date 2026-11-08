"""Compatibility facade; provider catalog is owned by ENGINE."""
from backend.engine.global_ecosystem.global_engine_ecosystem.global_server_engine_ecosystem.registry import (PROVIDERS, ROOT_ECOSYSTEM_ID, SERVER_ECOSYSTEM_ID, SERVICE_TYPES, ServerRegistrationRegistry, get_provider, get_service_type, list_providers, list_service_types)
__all__ = ["ROOT_ECOSYSTEM_ID", "SERVER_ECOSYSTEM_ID", "PROVIDERS", "SERVICE_TYPES", "ServerRegistrationRegistry", "list_providers", "get_provider", "list_service_types", "get_service_type"]
