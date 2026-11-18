"""Stable identity and capability constants for SERVER CORE."""

LAYER = "CORE"
CATEGORY = "SERVER"
ECOSYSTEM_NAME = "GLOBAL SERVER CORE ECOSYSTEM"
ECOSYSTEM_ID = "GLOBAL-SERVER-CORE-ECOSYSTEM"

CAPABILITIES = (
    "SERVER_RESOURCE_IDENTITY",
    "SERVER_LIFECYCLE_CONTRACTS",
    "PROVIDER_NEUTRAL_CONFIGURATION",
    "DEPLOYMENT_POLICY_METADATA",
    "HEALTH_STATE_CONTRACTS",
    "REGION_AND_ENVIRONMENT_TAXONOMY",
    "ACCESS_POLICY_METADATA",
    "INVENTORY_VALIDATION_RULES",
)

PROVIDER_DOMAINS = (
    "aws_server_core_ecosystem",
    "google_server_core_ecosystem",
    "microsoft_server_core_ecosystem",
    "cloudflare_server_core_ecosystem",
    "digitalocean_server_core_ecosystem",
    "abelohost_server_core_ecosystem",
    "vicetemple_server_core_ecosystem",
)
