"""Public interface for the Global Software Core Ecosystem."""
from .catalog import SOFTWARE_CORE_CATALOG, get_software_core_catalog, list_software_providers
from .contracts import CoreResult, Readiness, TenantContext, SoftwareReference
from .domain_catalog import DOMAIN_DEFINITIONS, list_software_domain_inventory, software_domain_summary
from .domain_runtime import SoftwareCoreDomainManager
from .manager import GlobalSoftwareCoreManager, get_manager
from .module_service import SoftwareProviderCoreService
from .orchestrator import GlobalSoftwareCoreOrchestrator
from .policy import SoftwareCorePolicy
from .service import GlobalSoftwareCoreService

__all__ = ["SOFTWARE_CORE_CATALOG", "get_software_core_catalog", "list_software_providers", "CoreResult", "Readiness", "TenantContext", "SoftwareReference", "DOMAIN_DEFINITIONS", "list_software_domain_inventory", "software_domain_summary", "SoftwareCoreDomainManager", "GlobalSoftwareCoreManager", "get_manager", "SoftwareProviderCoreService", "GlobalSoftwareCoreOrchestrator", "SoftwareCorePolicy", "GlobalSoftwareCoreService"]
