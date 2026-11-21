"""Public interface for Global Storage Core Ecosystem."""
from .catalog import GLOBAL_STORAGE_CORE_ECOSYSTEM,get_storage_core_catalog,list_storage_providers,get_storage_provider
from .product_catalog import list_storage_products,get_storage_product,storage_product_summary
from .contracts import CoreResult,Readiness,StorageProvider,StorageProductReference,TenantContext
from .domain_catalog import DOMAIN_DEFINITIONS,list_storage_domain_inventory,storage_domain_summary
from .domain_runtime import StorageCoreDomainManager
from .manager import GlobalStorageCoreManager,get_manager
from .module_service import StorageProviderCoreService
from .orchestrator import GlobalStorageCoreOrchestrator
from .policy import StorageCorePolicy,StorageCorePolicyError
from .service import GlobalStorageCoreEcosystemService
__all__=["GLOBAL_STORAGE_CORE_ECOSYSTEM","get_storage_core_catalog","list_storage_providers","get_storage_provider","list_storage_products","get_storage_product","storage_product_summary","CoreResult","Readiness","StorageProvider","StorageProductReference","TenantContext","DOMAIN_DEFINITIONS","list_storage_domain_inventory","storage_domain_summary","StorageCoreDomainManager","GlobalStorageCoreManager","get_manager","StorageProviderCoreService","GlobalStorageCoreOrchestrator","StorageCorePolicy","StorageCorePolicyError","GlobalStorageCoreEcosystemService"]
