"""Global CRM capability registry; implementation remains in backend.crm."""

ECOSYSTEM_ID = "GLOBAL-CRM-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL CRM ECOSYSTEM"
LAYER = "CRM"
STATUS = "DOMAIN_FACADE"
CAPABILITIES = (
    "CONTACT_MANAGEMENT",
    "OWNER_SCOPED_PERSISTENCE",
    "CONTACT_QUALITY",
    "DUPLICATE_DETECTION",
    "CONSENT_AWARE_FOLLOW_UP",
    "DAILY_WORK_MANAGEMENT",
    "IMPORT_PREVIEW_AND_APPROVAL",
    "AUDIT_TRAIL",
)
CANONICAL_IMPLEMENTATION = "backend.crm"
PROVIDER_CONNECTIONS_ENABLED = False
EXTERNAL_AI_ENABLED = False


def get_global_crm_catalog():
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "ecosystem_name": ECOSYSTEM_NAME,
        "layer": LAYER,
        "status": STATUS,
        "capabilities": list(CAPABILITIES),
        "canonical_implementation": CANONICAL_IMPLEMENTATION,
        "provider_connections_enabled": PROVIDER_CONNECTIONS_ENABLED,
        "external_ai_enabled": EXTERNAL_AI_ENABLED,
    }
