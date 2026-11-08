"""ENGINE-owned GLOBAL ECOSYSTEM taxonomy and seed records.

Independent ENGINE catalog: no API/CORE imports, objects, or runtime data.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ROOT_ID = "GLOBAL-ENGINE-ECOSYSTEM"
ROOT = {"ecosystem_id": ROOT_ID, "name": "GLOBAL ENGINE ECOSYSTEM",
        "ecosystem_type": "ENGINE_ROOT", "parent_id": None,
        "capabilities": ["ENGINE_REGISTRY", "EXECUTION_RUNTIME", "LIFECYCLE"]}
CATEGORIES = (
    ("COMPANIES","BUSINESS",["ORGANIZATION_RUNTIME","COMPANY_WORKFLOWS"]),
    ("PLATFORMS","PLATFORM",["PLATFORM_RUNTIME","SERVICE_LIFECYCLE"]),
    ("SERVER","INFRASTRUCTURE",["SERVER_RUNTIME","PROCESS_LIFECYCLE"]),
    ("AI","AI",["MODEL_RUNTIME","INFERENCE_RUNTIME"]),
    ("SOFTWARE_AI","SOFTWARE_AI",["SOFTWARE_RUNTIME","AI_TOOL_EXECUTION"]),
    ("CLOUD","INFRASTRUCTURE",["CLOUD_RUNTIME","RESOURCE_LIFECYCLE"]),
    ("SECURITY","SECURITY",["POLICY_RUNTIME","AUDIT_EXECUTION"]),
    ("INDIVIDUAL","IDENTITY",["USER_WORKFLOWS","PROFILE_RUNTIME"]),
    ("DEVELOPER","DEVELOPER",["BUILD_RUNTIME","TOOLING"]),
    ("COMMUNICATION","COMMUNICATION",["MESSAGE_RUNTIME","EVENT_DELIVERY"]),
    ("LANGUAGE","LANGUAGE",["LANGUAGE_PROCESSING","TRANSLATION_RUNTIME"]),
    ("VIDEO","MEDIA",["MEDIA_PROCESSING","VIDEO_WORKFLOWS"]),
    ("PAYMENT","COMMERCE",["PAYMENT_WORKFLOWS","BILLING_RUNTIME"]),
    ("STORAGE","DATA",["STORAGE_RUNTIME","ASSET_LIFECYCLE"]),
    ("SYSTEM","PLATFORM",["SYSTEM_RUNTIME","HEALTH_MONITORING"]),
    ("HOSTING","INFRASTRUCTURE",["DEPLOYMENT_RUNTIME","HOSTING_LIFECYCLE"]),
    ("INTIMACY","WELLNESS",["AGE_GATED_WORKFLOW_CONTROLS","CONSENT_POLICY_RUNTIME"]),
    ("DOMAIN","NETWORK",["DOMAIN_RUNTIME","DNS_OPERATIONS"]),
    ("WEB","WEB",["WEB_RUNTIME","REQUEST_LIFECYCLE"]),
    ("SOCIAL_MEDIA","MEDIA",["PUBLISHING_RUNTIME","SOCIAL_WORKFLOWS"]),
    ("FREELANCER","BUSINESS",["WORKFLOW_RUNTIME","PROJECT_EXECUTION"]),
    ("DATABASE","DATA",["QUERY_RUNTIME","PERSISTENCE"]),
)

def get_catalog() -> list[dict[str, Any]]:
    records = [deepcopy(ROOT)]
    for key, kind, capabilities in CATEGORIES:
        records.append({"ecosystem_id": f"GLOBAL-{key.replace('_','-')}-ENGINE-ECOSYSTEM",
            "name": f"GLOBAL {key.replace('_',' ')} ENGINE ECOSYSTEM",
            "ecosystem_type": kind, "parent_id": ROOT_ID,
            "capabilities": list(capabilities), "status": "REGISTERED",
            "enabled": True, "repository_ref": None, "metadata": {}})
    return records
def get_category_catalog() -> list[dict[str, Any]]:
    return _original_get_catalog()[1:]


# Provider and domain ecosystems mirrored from the repository's API taxonomy.
# These are ENGINE-owned identifiers and metadata, not imported API records.
PROVIDER_ECOSYSTEMS = (
    "adobe",
    "anthropic",
    "apple",
    "atlassian",
    "aws",
    "bada_business",
    "cohere",
    "deepseek",
    "digitalocean",
    "github",
    "global_ai",
    "global_app",
    "global_bada_business",
    "global_cloud",
    "global_cloudflare",
    "global_communication",
    "global_company_companies",
    "global_database",
    "global_developer",
    "global_domain",
    "global_entity_relationships",
    "global_hosting",
    "global_individual",
    "global_integrations",
    "global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness",
    "global_language",
    "global_organizations",
    "global_payment",
    "global_people_life",
    "global_platforms",
    "global_programming_language",
    "global_security",
    "global_server",
    "global_social_media",
    "global_software",
    "global_storage",
    "global_system",
    "global_tools",
    "global_video",
    "global_vps",
    "global_web",
    "global_website",
    "google",
    "huggingface",
    "ibm",
    "meta",
    "microsoft",
    "mistral",
    "nsfwinfra",
    "nvidia",
    "openai",
    "oracle",
    "paypal",
    "salesforce",
    "shopify",
    "slack",
    "stripe",
    "twilio",
)

def get_provider_catalog() -> list[dict[str, Any]]:
    records = []
    for slug in PROVIDER_ECOSYSTEMS:
        label = slug.replace("_", " ").upper()
        records.append({
            "ecosystem_id": "GLOBAL-PROVIDER-" + slug.upper().replace("_", "-") + "-ENGINE-ECOSYSTEM",
            "name": label + " ENGINE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_OR_DOMAIN",
            "parent_id": ROOT_ID,
            "capabilities": ["PROVIDER_RUNTIME_BOUNDARY", "ENGINE_LIFECYCLE"],
            "status": "REGISTERED", "enabled": True,
            "repository_ref": "backend/engine/global_ecosystem/global_engine_ecosystem/" + slug + "_engine_ecosystem",
            "metadata": {"source_taxonomy": "ENGINE_OWNED_MIRROR", "implementation_state": "SCAFFOLDED"},
        })
    return records

# The manager consumes both the 22 domain categories and the complete provider/domain catalog.
_original_get_catalog = get_catalog
def get_catalog() -> list[dict[str, Any]]:
    return _original_get_catalog() + get_provider_catalog()
