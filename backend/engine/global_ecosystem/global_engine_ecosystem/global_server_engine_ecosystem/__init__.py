"""ENGINE-owned provider catalog and server inventory adapter."""
from .registry import ROOT_ECOSYSTEM_ID, SERVER_ECOSYSTEM_ID, ServerRegistrationRegistry, get_provider, get_service_type, list_providers, list_service_types
from .service import EcosystemService
__all__ = ["EcosystemService", "ServerRegistrationRegistry", "ROOT_ECOSYSTEM_ID", "SERVER_ECOSYSTEM_ID", "get_provider", "get_service_type", "list_providers", "list_service_types"]
