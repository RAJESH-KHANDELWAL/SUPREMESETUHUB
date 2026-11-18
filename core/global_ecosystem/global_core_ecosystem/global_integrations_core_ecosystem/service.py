"""Read-only facade for the global integrations CORE registry."""
from collections.abc import Mapping
from typing import Any
from .catalog import get_catalog, get_integration, get_integrations_catalog, get_provider_catalog
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, STATUS
from .policy import redact_sensitive_metadata

class GlobalIntegrationsCoreService:
    def describe(self) -> dict[str, Any]:
        return {"layer":"CORE","ecosystem_id":ECOSYSTEM_ID,"ecosystem":ECOSYSTEM_NAME,
                "status":STATUS,"provider_execution_enabled":False,"live_connection_verified":False}
    def health(self) -> dict[str, Any]:
        return {"success":True,"status":STATUS,"integration_domain_count":len(get_integrations_catalog()),
                "provider_count":len(get_provider_catalog()),"live_connections_verified":False}
    def list_integrations(self) -> list[dict[str, Any]]:
        return get_integrations_catalog()
    def get_integration(self, integration_id: str):
        return get_integration(integration_id)
    def catalog(self) -> dict[str, Any]:
        return redact_sensitive_metadata(get_catalog())
    def inspect_metadata(self, metadata: Mapping[str, Any]) -> dict[str, Any]:
        if not isinstance(metadata, Mapping):
            raise TypeError("metadata must be a mapping")
        return redact_sensitive_metadata(metadata)
