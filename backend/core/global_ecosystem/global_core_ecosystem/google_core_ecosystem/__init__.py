"""Public interface for the Google Core Ecosystem control plane."""
from .catalog import GOOGLE_CORE_ECOSYSTEM, get_google_core_catalog, list_google_core_modules
from .contracts import CoreResult, Readiness, SecretReference, TenantContext
from .domain_catalog import DOMAIN_DEFINITIONS, google_domain_summary, list_google_domain_inventory
from .manager import GoogleCoreManager, get_manager
from .module_service import GoogleProductCoreService
from .orchestrator import GoogleCoreOrchestrator
from .policy import GoogleCorePolicy, GoogleCorePolicyError
from .product_catalog import google_offerings_summary, list_google_offerings
from .service import GoogleCoreEcosystemService

__all__ = [
    "GOOGLE_CORE_ECOSYSTEM", "get_google_core_catalog", "list_google_core_modules",
    "CoreResult", "Readiness", "SecretReference", "TenantContext",
    "DOMAIN_DEFINITIONS", "google_domain_summary", "list_google_domain_inventory",
    "GoogleCoreManager", "get_manager", "GoogleProductCoreService",
    "GoogleCoreOrchestrator", "GoogleCorePolicy", "GoogleCorePolicyError",
    "google_offerings_summary", "list_google_offerings", "GoogleCoreEcosystemService",
]
