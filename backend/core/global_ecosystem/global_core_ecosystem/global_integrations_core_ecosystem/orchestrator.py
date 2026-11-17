"""Read-only discovery orchestration for integration metadata."""
from .catalog import get_catalog, get_integration, get_integrations_catalog, get_provider_catalog
from .constants import ECOSYSTEM_ID, STATUS

class GlobalIntegrationsCoreOrchestrator:
    def catalog(self):
        return get_catalog()
    def list_integrations(self):
        return get_integrations_catalog()
    def get_integration(self, integration_id: str):
        return get_integration(integration_id)
    def list_providers(self):
        return get_provider_catalog()
    def health(self):
        return {"ecosystem_id":ECOSYSTEM_ID,"status":STATUS,
                "integration_domain_count":len(get_integrations_catalog()),
                "provider_count":len(get_provider_catalog()),
                "execution_enabled":False,"live_connection_verified":False}
