"""Read-only provider and integration capability catalogs."""
from copy import deepcopy
from .constants import STATUS
from .contracts import IntegrationDescriptor, ProviderDescriptor

_DOMAIN_ROWS = [{"id":"ADULT_AGE_VERIFICATION_CONSENT","name":"ADULT AGE VERIFICATION CONSENT","folder":"adult_age_verification_consent_integrations_core_ecosystem"},{"id":"ADULT_CONTENT_DISTRIBUTION_LICENSING","name":"ADULT CONTENT DISTRIBUTION LICENSING","folder":"adult_content_distribution_licensing_integrations_core_ecosystem"},{"id":"ADULT_CONTENT_PRODUCTION_STUDIO","name":"ADULT CONTENT PRODUCTION STUDIO","folder":"adult_content_production_studio_integrations_core_ecosystem"},{"id":"ADULT_CREATOR_BUSINESS","name":"ADULT CREATOR BUSINESS","folder":"adult_creator_business_integrations_core_ecosystem"},{"id":"ADULT_ENTERTAINMENT_PLATFORM","name":"ADULT ENTERTAINMENT PLATFORM","folder":"adult_entertainment_platform_integrations_core_ecosystem"},{"id":"ADULT_LEGAL_REGIONAL_COMPLIANCE","name":"ADULT LEGAL REGIONAL COMPLIANCE","folder":"adult_legal_regional_compliance_integrations_core_ecosystem"},{"id":"ADULT_LIVE_STREAMING","name":"ADULT LIVE STREAMING","folder":"adult_live_streaming_integrations_core_ecosystem"},{"id":"ADULT_MODERATION_SAFETY_TAKEDOWN","name":"ADULT MODERATION SAFETY TAKEDOWN","folder":"adult_moderation_safety_takedown_integrations_core_ecosystem"},{"id":"ADULT_PAYMENTS_PAYOUTS","name":"ADULT PAYMENTS PAYOUTS","folder":"adult_payments_payouts_integrations_core_ecosystem"},{"id":"ADULT_PRIVACY_SECURITY","name":"ADULT PRIVACY SECURITY","folder":"adult_privacy_security_integrations_core_ecosystem"},{"id":"AI_ML_DATA","name":"AI ML DATA","folder":"ai_ml_data_integrations_core_ecosystem"},{"id":"APPLE","name":"APPLE","folder":"apple_integrations_core_ecosystem"},{"id":"AUTOMATION_WORKFLOW","name":"AUTOMATION WORKFLOW","folder":"automation_workflow_integrations_core_ecosystem"},{"id":"AWS","name":"AWS","folder":"aws_integrations_core_ecosystem"},{"id":"BUSINESS_ENTERPRISE","name":"BUSINESS ENTERPRISE","folder":"business_enterprise_integrations_core_ecosystem"},{"id":"COMMERCE_MARKETPLACE","name":"COMMERCE MARKETPLACE","folder":"commerce_marketplace_integrations_core_ecosystem"},{"id":"COMMUNICATION_SOCIAL_MEDIA","name":"COMMUNICATION SOCIAL MEDIA","folder":"communication_social_media_integrations_core_ecosystem"},{"id":"DATABASE_STORAGE","name":"DATABASE STORAGE","folder":"database_storage_integrations_core_ecosystem"},{"id":"DATING_RELATIONSHIPS","name":"DATING RELATIONSHIPS","folder":"dating_relationships_integrations_core_ecosystem"},{"id":"DEVELOPER_API","name":"DEVELOPER API","folder":"developer_api_integrations_core_ecosystem"},{"id":"GLOBAL_CLOUD","name":"GLOBAL CLOUD","folder":"global_cloud_integrations_core_ecosystem"},{"id":"GLOBAL_INTEGRATIONS","name":"GLOBAL INTEGRATIONS","folder":"global_integrations_core_ecosystem"},{"id":"GOOGLE","name":"GOOGLE","folder":"google_integrations_core_ecosystem"},{"id":"IDENTITY_AUTHENTICATION","name":"IDENTITY AUTHENTICATION","folder":"identity_authentication_integrations_core_ecosystem"},{"id":"INDIA","name":"INDIA","folder":"india_integrations_core_ecosystem"},{"id":"INDIVIDUAL_PERSONAL","name":"INDIVIDUAL PERSONAL","folder":"individual_personal_integrations_core_ecosystem"},{"id":"INTEGRATION_TIERS_NORMAL_TO_SUPREME","name":"INTEGRATION TIERS NORMAL TO SUPREME","folder":"integration_tiers_normal_to_supreme_core_ecosystem"},{"id":"MICROSOFT","name":"MICROSOFT","folder":"microsoft_integrations_core_ecosystem"},{"id":"PAYMENTS_BANKING_FINANCE","name":"PAYMENTS BANKING FINANCE","folder":"payments_banking_finance_integrations_core_ecosystem"},{"id":"SECURITY_PRIVACY_COMPLIANCE","name":"SECURITY PRIVACY COMPLIANCE","folder":"security_privacy_compliance_integrations_core_ecosystem"},{"id":"SEXUAL_WELLNESS_EDUCATION","name":"SEXUAL WELLNESS EDUCATION","folder":"sexual_wellness_education_integrations_core_ecosystem"}]
INTEGRATION_CATALOG = tuple(
    IntegrationDescriptor(
        integration_id=row["id"],
        display_name=row["name"],
        domain_id=row["id"],
        capabilities=(row["id"] + "_DISCOVERY", row["id"] + "_POLICY_METADATA"),
        sensitivity="RESTRICTED" if row["id"].startswith("ADULT_") or row["id"].startswith("SEXUAL_") else "STANDARD",
        age_restricted=row["id"].startswith("ADULT_"),
        consent_required=row["id"].startswith("ADULT_"),
    )
    for row in _DOMAIN_ROWS
)
_PROVIDER_ROWS = (
    ("aws", "Amazon Web Services", "CLOUD"),
    ("google", "Google", "CLOUD_PRODUCTIVITY"),
    ("microsoft", "Microsoft", "CLOUD_PRODUCTIVITY"),
    ("apple", "Apple", "DEVICE_PRODUCTIVITY"),
    ("cloudflare", "Cloudflare", "NETWORK_SECURITY"),
    ("github", "GitHub", "DEVELOPER"),
    ("stripe", "Stripe", "PAYMENTS"),
    ("india_digital_services", "India Digital Services", "REGIONAL"),
    ("other", "Other / Self-hosted", "GENERAL"),
)
PROVIDER_CATALOG = tuple(ProviderDescriptor(*row) for row in _PROVIDER_ROWS)

def get_integrations_catalog():
    return deepcopy([{
        "integration_id": x.integration_id, "display_name": x.display_name,
        "domain_id": x.domain_id, "capabilities": list(x.capabilities),
        "sensitivity": x.sensitivity, "age_restricted": x.age_restricted,
        "consent_required": x.consent_required, "status": x.status,
        "live_connection_verified": False,
    } for x in INTEGRATION_CATALOG])

def get_integration(integration_id: str):
    for item in get_integrations_catalog():
        if item["integration_id"] == integration_id:
            return item
    return None

def get_provider_catalog():
    return [{
        "provider_id": x.provider_id, "display_name": x.display_name,
        "category": x.category, "status": x.status,
        "live_connection_verified": False,
    } for x in PROVIDER_CATALOG]

def get_catalog():
    return {"ecosystem_id": "GLOBAL-INTEGRATIONS-CORE-ECOSYSTEM",
            "status": STATUS, "integration_domain_count": len(INTEGRATION_CATALOG),
            "integrations": get_integrations_catalog(), "providers": get_provider_catalog(),
            "live_connection_verified": False}
