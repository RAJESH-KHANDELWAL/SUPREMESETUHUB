"""ENGINE-owned GLOBAL ECOSYSTEM taxonomy and complete provider namespace catalog.

The catalog discovers only ENGINE-owned package directories. It never imports or
reads API/CORE implementation objects or runtime data.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import re
from typing import Any

ROOT_ID = "GLOBAL-ENGINE-ECOSYSTEM"
ROOT = {
    "ecosystem_id": ROOT_ID,
    "name": "GLOBAL ENGINE ECOSYSTEM",
    "ecosystem_type": "ENGINE_ROOT",
    "parent_id": None,
    "capabilities": ["ENGINE_REGISTRY", "EXECUTION_RUNTIME", "LIFECYCLE"],
}

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

def _base_catalog() -> list[dict[str, Any]]:
    records = [deepcopy(ROOT)]
    for key, kind, capabilities in CATEGORIES:
        records.append({
            "ecosystem_id": f"GLOBAL-{key.replace('_','-')}-ENGINE-ECOSYSTEM",
            "name": f"GLOBAL {key.replace('_',' ')} ENGINE ECOSYSTEM",
            "ecosystem_type": kind,
            "parent_id": ROOT_ID,
            "capabilities": list(capabilities),
            "status": "REGISTERED",
            "enabled": True,
            "repository_ref": None,
            "metadata": {"implementation_state": "ENGINE_OWNED"},
        })
    return records

def get_category_catalog() -> list[dict[str, Any]]:
    return _base_catalog()[1:]

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

def _slug(value: str) -> str:
    # Preserve nested package suffixes: a plain namespace and a nested
    # *_engine_ecosystem package can coexist as distinct directories.
    return re.sub(r"[^A-Z0-9]+", "-", value.upper()).strip("-")

def _provider_id(provider: str, parts: tuple[str, ...] = ()) -> str:
    segments = [_slug(provider), *(_slug(part) for part in parts)]
    return "GLOBAL-PROVIDER-" + "-".join(segment for segment in segments if segment) + "-ENGINE-ECOSYSTEM"

def get_provider_catalog() -> list[dict[str, Any]]:
    """Return every provider root and nested ENGINE namespace directory.

    All records are discovered from this ENGINE package tree itself. The 58
    provider roots and every nested package directory get stable IDs and
    explicit parent relationships.
    """
    package_root = Path(__file__).resolve().parent / "global_engine_ecosystem"
    records: list[dict[str, Any]] = []
    for provider in PROVIDER_ECOSYSTEMS:
        provider_dir = package_root / f"{provider}_engine_ecosystem"
        if not provider_dir.is_dir():
            raise RuntimeError(f"ENGINE provider package is missing: {provider_dir}")
        root_id = _provider_id(provider)
        records.append({
            "ecosystem_id": root_id,
            "name": provider.replace("_", " ").upper() + " ENGINE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_OR_DOMAIN",
            "parent_id": ROOT_ID,
            "capabilities": ["PROVIDER_RUNTIME_BOUNDARY", "ENGINE_LIFECYCLE"],
            "status": "REGISTERED",
            "enabled": True,
            "repository_ref": str(provider_dir.relative_to(package_root.parent)),
            "metadata": {"source_taxonomy": "ENGINE_OWNED", "implementation_state": "SCAFFOLDED"},
        })
        package_dirs = sorted(
            item.parent for item in provider_dir.rglob("__init__.py")
            if item.parent != provider_dir
        )
        for directory in package_dirs:
            relative_parts = directory.relative_to(provider_dir).parts
            parent_id = _provider_id(provider, relative_parts[:-1])
            records.append({
                "ecosystem_id": _provider_id(provider, relative_parts),
                "name": relative_parts[-1].removesuffix("_engine_ecosystem").replace("_", " ").upper(),
                "ecosystem_type": "PROVIDER_SUBSYSTEM",
                "parent_id": parent_id,
                "capabilities": ["ENGINE_NAMESPACE", "LIFECYCLE_BOUNDARY"],
                "status": "REGISTERED",
                "enabled": True,
                "repository_ref": str(directory.relative_to(package_root.parent)),
                "metadata": {"source_taxonomy": "ENGINE_OWNED", "implementation_state": "SCAFFOLDED"},
            })
    return records

def get_catalog() -> list[dict[str, Any]]:
    """Return root, shared category taxonomy, and full provider hierarchy."""
    return _base_catalog() + get_provider_catalog()
