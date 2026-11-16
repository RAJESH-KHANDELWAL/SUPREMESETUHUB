"""Public interface for the Global Domain Core Ecosystem."""
from .catalog import DOMAIN_CAPABILITY_DOMAINS, GLOBAL_DOMAIN_CORE_ECOSYSTEM, get_domain_core_catalog, list_domain_capability_domains
from .contracts import DomainCoreResult, DomainReadiness, DomainTenantContext
from .module_service import DomainProviderCoreService
from .orchestrator import GlobalDomainCoreOrchestrator
from .policy import DomainCorePolicy, DomainCorePolicyError
from .provider_catalog import DOMAIN_PROVIDER_CATALOG, domain_provider_summary, get_domain_provider, list_domain_providers
from .service import GlobalDomainCoreEcosystemService

__all__ = [
    "DOMAIN_CAPABILITY_DOMAINS", "GLOBAL_DOMAIN_CORE_ECOSYSTEM",
    "get_domain_core_catalog", "list_domain_capability_domains",
    "DomainCoreResult", "DomainReadiness", "DomainTenantContext",
    "DomainProviderCoreService", "GlobalDomainCoreOrchestrator",
    "DomainCorePolicy", "DomainCorePolicyError", "DOMAIN_PROVIDER_CATALOG",
    "domain_provider_summary", "get_domain_provider", "list_domain_providers",
    "GlobalDomainCoreEcosystemService",
]
