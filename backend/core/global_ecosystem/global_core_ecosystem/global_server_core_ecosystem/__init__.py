"""Public exports for the independent SERVER CORE domain."""
from .constants import LAYER, CATEGORY, ECOSYSTEM_NAME, ECOSYSTEM_ID, CAPABILITIES, PROVIDER_DOMAINS
from .contracts import ServerInventoryContract, ServerLifecycleContract, ServerProviderContract
from .models import ServerIdentity, ServerLifecycleState, ServerResourceDescriptor
from .policy import SUPPORTED_ENVIRONMENTS, SUPPORTED_LIFECYCLE_STATES, SUPPORTED_SERVER_TYPES, ServerPolicy
from .registry import ServerCoreRegistry
from .service import ServerCoreService
from .catalog import get_catalog, get_server_core_catalog
from .provider_catalog import get_provider_catalog, get_provider
from .orchestrator import ServerCoreOrchestrator
from .scope_catalog import (
    get_geographic_scope_catalog,
    get_workload_domain_catalog,
    get_service_tier_catalog,
    get_scope_catalog,
)

__all__ = [
    "LAYER", "CATEGORY", "ECOSYSTEM_NAME", "ECOSYSTEM_ID", "CAPABILITIES", "PROVIDER_DOMAINS",
    "ServerIdentity", "ServerLifecycleState", "ServerResourceDescriptor", "ServerPolicy",
    "ServerCoreRegistry", "ServerCoreService", "ServerProviderContract", "ServerInventoryContract",
    "ServerLifecycleContract", "SUPPORTED_SERVER_TYPES", "SUPPORTED_ENVIRONMENTS",
    "SUPPORTED_LIFECYCLE_STATES", "get_catalog", "get_server_core_catalog",
    "get_provider_catalog", "get_provider", "ServerCoreOrchestrator",
    "get_geographic_scope_catalog", "get_workload_domain_catalog",
    "get_service_tier_catalog", "get_scope_catalog",
]

from .manager import GlobalServerCoreManager, get_manager, manager_status, validate_master_alignment

__all__ = [
    "GlobalServerCoreManager", "get_manager", "manager_status",
    "validate_master_alignment",
]
