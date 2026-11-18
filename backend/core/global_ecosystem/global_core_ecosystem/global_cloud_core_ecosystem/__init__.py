"""Public entry point for GLOBAL CLOUD CORE ECOSYSTEM."""
from .contracts import CloudCoreResult, CloudReadiness, CloudTenantContext
from .service import GlobalCloudCoreService

LAYER = "CORE"
CATEGORY = "CLOUD"
ECOSYSTEM_NAME = "GLOBAL CLOUD CORE ECOSYSTEM"
ECOSYSTEM_ID = "GLOBAL-CLOUD-CORE-ECOSYSTEM"
RUNTIME_ECOSYSTEM = "GLOBAL_CLOUD_ECOSYSTEM"

__all__ = [
    "LAYER", "CATEGORY", "ECOSYSTEM_NAME", "ECOSYSTEM_ID",
    "RUNTIME_ECOSYSTEM", "CloudCoreResult", "CloudReadiness",
    "CloudTenantContext", "GlobalCloudCoreService",
]
