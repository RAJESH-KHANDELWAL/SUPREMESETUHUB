"""Bada Business CRM scope and capabilities."""

ECOSYSTEM_ID = "BADA-BUSINESS-CRM-ECOSYSTEM"
ECOSYSTEM_NAME = "BADA BUSINESS CRM ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "GLOBAL-CRM-ECOSYSTEM"
LAYER = "CRM"
STATUS = "DOMAIN_ADAPTER"
CAPABILITIES = (
    "BUSINESS_LEAD_MANAGEMENT",
    "ENTREPRENEUR_AND_CUSTOMER_CONTACTS",
    "BUSINESS_FOLLOW_UPS",
    "PROGRAM_INTEREST_TRACKING",
    "CONSENT_AWARE_COMMUNICATION",
)
CANONICAL_CRM_MODULE = "backend.crm"
CANONICAL_BUSINESS_RESOURCE_CATALOG = "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog"
PROVIDER_API_CONNECTED = False
AUTOMATIC_OUTREACH_ENABLED = False


def get_bada_business_crm_catalog():
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "ecosystem_name": ECOSYSTEM_NAME,
        "parent_ecosystem_id": PARENT_ECOSYSTEM_ID,
        "layer": LAYER,
        "status": STATUS,
        "capabilities": list(CAPABILITIES),
        "canonical_crm_module": CANONICAL_CRM_MODULE,
        "canonical_business_resource_catalog": CANONICAL_BUSINESS_RESOURCE_CATALOG,
        "provider_api_connected": PROVIDER_API_CONNECTED,
        "automatic_outreach_enabled": AUTOMATIC_OUTREACH_ENABLED,
    }
