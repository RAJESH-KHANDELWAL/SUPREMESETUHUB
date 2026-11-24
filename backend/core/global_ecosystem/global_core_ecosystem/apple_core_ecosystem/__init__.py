"""Public interface for Apple Core Ecosystem."""
from .catalog import APPLE_CORE_ECOSYSTEM, get_apple_core_catalog, list_apple_core_modules
from .contracts import CoreResult, Readiness, SecretReference, TenantContext
from .domain_catalog import DOMAIN_DEFINITIONS, apple_domain_summary, list_apple_domain_inventory
from .orchestrator import AppleCoreOrchestrator
from .policy import AppleCorePolicy, AppleCorePolicyError
from .product_catalog import apple_offerings_summary, list_apple_offerings
from .service import AppleCoreEcosystemService
from .domain_runtime import AppleCoreDomainManager
from .manager import AppleCoreManager, get_manager
__all__ = ["APPLE_CORE_ECOSYSTEM", "get_apple_core_catalog", "list_apple_core_modules",
"CoreResult", "Readiness", "SecretReference", "TenantContext", "DOMAIN_DEFINITIONS",
"apple_domain_summary", "list_apple_domain_inventory", "AppleCoreOrchestrator",
"AppleCorePolicy", "AppleCorePolicyError", "apple_offerings_summary", "list_apple_offerings",
"AppleCoreEcosystemService", "AppleCoreDomainManager", "AppleCoreManager", "get_manager"]
