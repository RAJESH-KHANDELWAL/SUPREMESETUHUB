"""Public interface for the Global Cloud Core Ecosystem."""
from .domain_catalog import CLOUD_DOMAIN_DEFINITIONS, cloud_domain_summary, list_cloud_domain_inventory
from .domain_runtime import GlobalCloudCoreDomainManager
from .manager import GlobalCloudCoreManager, get_manager
from .service import GlobalCloudCoreService

__all__ = [
    "CLOUD_DOMAIN_DEFINITIONS", "cloud_domain_summary", "list_cloud_domain_inventory",
    "GlobalCloudCoreDomainManager", "GlobalCloudCoreManager", "get_manager",
    "GlobalCloudCoreService",
]
