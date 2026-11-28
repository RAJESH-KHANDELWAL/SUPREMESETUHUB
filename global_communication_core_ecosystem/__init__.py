"""Global Communication Core Ecosystem metadata package."""
LAYER = "CORE"
CATEGORY = "COMMUNICATION"
ECOSYSTEM_NAME = "GLOBAL COMMUNICATION CORE ECOSYSTEM"
ECOSYSTEM_ID = "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM"
from .catalog import get_communication_core_catalog
from .contracts import CoreResult, Readiness, SecretReference, TenantContext
from .domain_runtime import CommunicationCoreDomainManager
from .manager import CommunicationCoreManager, get_manager
from .module_service import CommunicationProviderCoreService
__all__ = [
    "LAYER", "CATEGORY", "ECOSYSTEM_NAME", "ECOSYSTEM_ID",
    "get_communication_core_catalog", "CoreResult", "Readiness",
    "SecretReference", "TenantContext", "CommunicationCoreDomainManager",
    "CommunicationCoreManager", "CommunicationProviderCoreService", "get_manager",
]
