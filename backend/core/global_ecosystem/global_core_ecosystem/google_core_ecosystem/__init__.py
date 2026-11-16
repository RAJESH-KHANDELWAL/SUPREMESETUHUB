"""Public interface for the Google Core Ecosystem control plane."""
from .catalog import GOOGLE_CORE_ECOSYSTEM, get_google_core_catalog, list_google_core_modules
from .contracts import CoreResult, Readiness, SecretReference, TenantContext
from .orchestrator import GoogleCoreOrchestrator
from .policy import GoogleCorePolicy, GoogleCorePolicyError
from .service import GoogleCoreEcosystemService

__all__ = [
    "GOOGLE_CORE_ECOSYSTEM",
    "get_google_core_catalog",
    "list_google_core_modules",
    "CoreResult",
    "Readiness",
    "SecretReference",
    "TenantContext",
    "GoogleCoreOrchestrator",
    "GoogleCorePolicy",
    "GoogleCorePolicyError",
    "GoogleCoreEcosystemService",
]
