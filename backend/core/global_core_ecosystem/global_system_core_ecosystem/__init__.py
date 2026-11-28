"""Global System Core Ecosystem public interface."""
from .catalog import SYSTEM_CORE_ECOSYSTEM, get_system_core_catalog, list_system_providers
from .contracts import SystemCoreResult, SystemReadiness, SystemTenantContext, SystemSecretReference
from .domain_catalog import DOMAIN_DEFINITIONS, system_domain_summary, list_system_domain_inventory
from .domain_runtime import SystemCoreDomainManager
from .manager import SystemCoreManager, get_manager
from .module_service import SystemProviderCoreService, SystemProductCoreService
from .orchestrator import SystemCoreOrchestrator
from .policy import SystemCorePolicy, SystemCorePolicyError
from .product_catalog import list_system_products, system_products_summary
from .service import SystemCoreEcosystemService

__all__ = [
    "SYSTEM_CORE_ECOSYSTEM", "get_system_core_catalog", "list_system_providers",
    "SystemCoreResult", "SystemReadiness", "SystemTenantContext", "SystemSecretReference",
    "DOMAIN_DEFINITIONS", "system_domain_summary", "list_system_domain_inventory",
    "SystemCoreDomainManager", "SystemCoreManager", "get_manager",
    "SystemProviderCoreService", "SystemProductCoreService", "SystemCoreOrchestrator",
    "SystemCorePolicy", "SystemCorePolicyError", "list_system_products",
    "system_products_summary", "SystemCoreEcosystemService",
]
