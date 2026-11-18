"""Public entry point for GLOBAL APP CORE ECOSYSTEM."""
from .contracts import AppCoreResult, AppReadiness, AppTenantContext
from .service import GlobalAppCoreService

LAYER = "CORE"
ECOSYSTEM_ID = "GLOBAL-APP-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL APP CORE ECOSYSTEM"
RUNTIME_ECOSYSTEM = "GLOBAL_APP_ECOSYSTEM"

__all__ = [
    "LAYER",
    "ECOSYSTEM_ID",
    "ECOSYSTEM_NAME",
    "RUNTIME_ECOSYSTEM",
    "AppCoreResult",
    "AppReadiness",
    "AppTenantContext",
    "GlobalAppCoreService",
]
