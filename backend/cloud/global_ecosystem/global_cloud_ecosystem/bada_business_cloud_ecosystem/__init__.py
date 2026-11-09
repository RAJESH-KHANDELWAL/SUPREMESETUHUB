"""BADA BUSINESS CLOUD ECOSYSTEM — cloud infrastructure integration domain."""
from .catalog import CLOUD_CAPABILITIES, CLOUD_ECOSYSTEM_PROFILE, get_bada_business_cloud_catalog
from .service import BadaBusinessCloudService
from .manager import BadaBusinessCloudManager
LAYER = "CLOUD"
ECOSYSTEM_ID = "BADA_BUSINESS_CLOUD_ECOSYSTEM"
STATUS = "CLOUD_INTEGRATION_FOUNDATION_READY"
__all__ = [
    "CLOUD_CAPABILITIES", "CLOUD_ECOSYSTEM_PROFILE",
    "get_bada_business_cloud_catalog", "BadaBusinessCloudService",
    "BadaBusinessCloudManager", "LAYER", "ECOSYSTEM_ID", "STATUS",
]
