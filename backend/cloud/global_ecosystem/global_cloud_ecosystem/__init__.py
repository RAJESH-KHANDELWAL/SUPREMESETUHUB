"""GLOBAL CLOUD ECOSYSTEM public interface."""
from .catalog import CLOUD_ECOSYSTEM_PROFILE, CLOUD_PROVIDERS, get_cloud_catalog
from .registry import list_providers, get_provider
from .models import CloudProviderDescriptor, CloudOperationRequest, CloudOperationResult
from .adapters import CloudProviderAdapter, CloudAdapterRegistry
from .service import GlobalCloudEcosystemService
from .manager import GlobalCloudEcosystemManager
from .diagnostics import cloud_diagnostics
from .cultural_knowledge_cloud import CulturalKnowledgeCloudBridge
from .global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_cloud_ecosystem import GlobalCulturalCloud

LAYER = "CLOUD"
ECOSYSTEM_ID = "GLOBAL_CLOUD_ECOSYSTEM"
STATUS = "FOUNDATION_READY"

__all__ = [
    "CLOUD_ECOSYSTEM_PROFILE", "CLOUD_PROVIDERS", "get_cloud_catalog",
    "list_providers", "get_provider", "CloudProviderDescriptor",
    "CloudOperationRequest", "CloudOperationResult", "CloudProviderAdapter",
    "CloudAdapterRegistry", "GlobalCloudEcosystemService",
    "GlobalCloudEcosystemManager", "cloud_diagnostics",
    "LAYER", "ECOSYSTEM_ID", "STATUS", "CulturalKnowledgeCloudBridge", "GlobalCulturalCloud",
]

# Bada Business-specific cloud integration package.
from .bada_business_cloud_ecosystem import (
    BadaBusinessCloudManager,
    BadaBusinessCloudService,
    get_bada_business_cloud_catalog,
)
__all__ += [
    "BadaBusinessCloudManager",
    "BadaBusinessCloudService",
    "get_bada_business_cloud_catalog",
]
