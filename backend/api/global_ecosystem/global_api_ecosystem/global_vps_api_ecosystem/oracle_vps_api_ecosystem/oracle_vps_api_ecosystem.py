"""Oracle Cloud compute/VPS category mapping; no instance operations are performed."""

PROVIDER_ID = "oracle"
PROVIDER_NAME = "ORACLE API ECOSYSTEM"
CATEGORY_ID = "VPS"
CATEGORY_NAME = "GLOBAL VPS API ECOSYSTEM"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/oracle_api_ecosystem"
CATEGORY_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem"
SERVICE_FAMILIES = (
    "OCI_COMPUTE_INSTANCES",
    "OCI_BLOCK_VOLUMES",
    "OCI_VIRTUAL_CLOUD_NETWORKS",
    "OCI_INSTANCE_CONFIGURATIONS",
)
SCOPE = "OCI compute instances and supporting storage/network resources; VPS is a project category, not an Oracle product name."
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
OFFICIAL_API_DOCUMENTATION = "https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm"
LIVE_CONNECTION_VERIFIED = False
