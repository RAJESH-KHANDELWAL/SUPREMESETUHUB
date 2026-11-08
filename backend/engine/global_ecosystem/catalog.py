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
    return get_catalog()[1:]
