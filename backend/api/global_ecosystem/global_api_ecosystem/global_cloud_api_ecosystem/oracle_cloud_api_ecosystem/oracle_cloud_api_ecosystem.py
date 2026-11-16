"""Oracle Cloud category mapping; no live OCI operation is performed here."""

PROVIDER_ID = "oracle"
PROVIDER_NAME = "ORACLE API ECOSYSTEM"
CATEGORY_ID = "CLOUD"
CATEGORY_NAME = "GLOBAL CLOUD API ECOSYSTEM"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/oracle_api_ecosystem"
CATEGORY_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_cloud_api_ecosystem"
SERVICE_FAMILIES = (
    "OCI_COMPUTE",
    "OCI_NETWORKING",
    "OCI_OBJECT_STORAGE",
    "OCI_IAM",
    "OCI_OBSERVABILITY",
    "OCI_LOAD_BALANCING",
    "OCI_CONTAINER_ENGINE_FOR_KUBERNETES",
)
SCOPE = "OCI cloud infrastructure, networking, storage, identity and operations APIs."
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
OFFICIAL_API_DOCUMENTATION = "https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm"
LIVE_CONNECTION_VERIFIED = False
