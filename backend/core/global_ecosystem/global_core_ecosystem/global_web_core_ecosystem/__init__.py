"""Public interface for GLOBAL WEB CORE ECOSYSTEM."""
from .constants import LAYER, CATEGORY, ECOSYSTEM_NAME, ECOSYSTEM_ID, CAPABILITIES
from .contracts import CoreResult, Readiness, SecretReference, TenantContext
from .domain_catalog import DOMAIN_DEFINITIONS, domain_summary, get_domain, list_domain_inventory
from .domain_runtime import WebCoreDomainManager
from .manager import GlobalWebCoreManager, get_manager
from .module_service import WebProviderCoreService
from .orchestrator import WebCoreOrchestrator
from .policy import WebCorePolicy
from .product_catalog import get_product_family, list_product_families
from .provider_catalog import get_provider, list_providers
from .service import WebCoreEcosystemService

__all__ = [
    "LAYER", "CATEGORY", "ECOSYSTEM_NAME", "ECOSYSTEM_ID", "CAPABILITIES",
    "CoreResult", "Readiness", "SecretReference", "TenantContext",
    "DOMAIN_DEFINITIONS", "domain_summary", "get_domain", "list_domain_inventory",
    "WebCoreDomainManager", "GlobalWebCoreManager", "get_manager",
    "WebProviderCoreService", "WebCoreOrchestrator", "WebCorePolicy",
    "get_product_family", "list_product_families", "get_provider",
    "list_providers", "WebCoreEcosystemService",
]
