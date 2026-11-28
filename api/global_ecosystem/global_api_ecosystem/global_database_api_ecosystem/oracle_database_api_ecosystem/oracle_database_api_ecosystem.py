"""Oracle Database category mapping; no database connection is performed here."""

PROVIDER_ID = "oracle"
PROVIDER_NAME = "ORACLE API ECOSYSTEM"
CATEGORY_ID = "DATABASE"
CATEGORY_NAME = "GLOBAL DATABASE API ECOSYSTEM"
PROVIDER_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/oracle_api_ecosystem"
CATEGORY_CATALOG_PATH = "backend/api/global_ecosystem/global_api_ecosystem/global_database_api_ecosystem"
SERVICE_FAMILIES = (
    "ORACLE_AUTONOMOUS_DATABASE",
    "ORACLE_BASE_DATABASE_SERVICE",
    "ORACLE_MYSQL_HEATWAVE",
    "ORACLE_DATABASE_TOOLS",
)
SCOPE = "Oracle database provisioning, lifecycle, backup, configuration and management APIs."
IMPLEMENTATION_STATUS = "CATALOG_ONLY"
OFFICIAL_API_DOCUMENTATION = "https://docs.oracle.com/en-us/iaas/Content/Database/Concepts/databaseoverview.htm"
LIVE_CONNECTION_VERIFIED = False
