"""Global integrations CORE ecosystem public interface."""
from .catalog import INTEGRATION_CATALOG, PROVIDER_CATALOG, get_integration, get_integrations_catalog, get_provider_catalog
from .constants import CATEGORY, ECOSYSTEM_ID, ECOSYSTEM_NAME, LAYER, STATUS
from .contracts import IntegrationDescriptor, ProviderDescriptor
from .orchestrator import GlobalIntegrationsCoreOrchestrator
from .service import GlobalIntegrationsCoreService

__all__ = [
    "CATEGORY", "ECOSYSTEM_ID", "ECOSYSTEM_NAME", "LAYER", "STATUS",
    "IntegrationDescriptor", "ProviderDescriptor", "INTEGRATION_CATALOG",
    "PROVIDER_CATALOG", "get_integration", "get_integrations_catalog",
    "get_provider_catalog", "GlobalIntegrationsCoreOrchestrator",
    "GlobalIntegrationsCoreService",
]
