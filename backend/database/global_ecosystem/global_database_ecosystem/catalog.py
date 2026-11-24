"""DATABASE-owned GLOBAL DATABASE ECOSYSTEM taxonomy.

This catalog is maintained locally by the DATABASE layer. It does not import,
inspect, or copy API, CORE, or ENGINE runtime objects.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT_ID = "GLOBAL-DATABASE-ECOSYSTEM"
ROOT = {
    "ecosystem_id": ROOT_ID,
    "name": "GLOBAL DATABASE ECOSYSTEM",
    "ecosystem_type": "DATABASE_ROOT",
    "parent_id": None,
    "capabilities": ["DATABASE_REGISTRY", "PERSISTENCE_CATALOG", "DATA_LIFECYCLE"],
    "metadata": {"layer": "DATABASE", "independent": True},
}

CATEGORIES = (
    ("COMPANIES", "BUSINESS", ["ORGANIZATION_DATA", "COMPANY_RECORDS"]),
    ("PLATFORMS", "PLATFORM", ["PLATFORM_DATA", "SERVICE_RECORDS"]),
    ("SERVER", "INFRASTRUCTURE", ["SERVER_INVENTORY", "RESOURCE_METADATA"]),
    ("AI", "AI", ["MODEL_METADATA", "AI_DATASETS"]),
    ("SOFTWARE_AI", "SOFTWARE_AI", ["SOFTWARE_METADATA", "AI_TOOL_DATA"]),
    ("CLOUD", "INFRASTRUCTURE", ["CLOUD_RESOURCES", "CLOUD_METADATA"]),
    ("SECURITY", "SECURITY", ["AUDIT_RECORDS", "POLICY_DATA"]),
    ("INDIVIDUAL", "IDENTITY", ["USER_RECORDS", "PROFILE_DATA"]),
    ("DEVELOPER", "DEVELOPER", ["REPOSITORY_METADATA", "BUILD_RECORDS"]),
    ("COMMUNICATION", "COMMUNICATION", ["MESSAGE_METADATA", "DELIVERY_RECORDS"]),
    ("LANGUAGE", "LANGUAGE", ["LANGUAGE_DATA", "TRANSLATION_RECORDS"]),
    ("VIDEO", "MEDIA", ["MEDIA_METADATA", "VIDEO_ASSETS"]),
    ("PAYMENT", "COMMERCE", ["PAYMENT_RECORDS", "BILLING_DATA"]),
    ("STORAGE", "DATA", ["OBJECT_METADATA", "FILE_INDEXES"]),
    ("SYSTEM", "PLATFORM", ["SYSTEM_STATE", "HEALTH_RECORDS"]),
    ("HOSTING", "INFRASTRUCTURE", ["DEPLOYMENT_METADATA", "HOSTING_RECORDS"]),
    ("INTIMACY", "WELLNESS", ["CONSENT_RECORDS", "PRIVACY_CONTROLS"]),
    ("DOMAIN", "NETWORK", ["DOMAIN_RECORDS", "DNS_METADATA"]),
    ("WEB", "WEB", ["WEB_CONTENT", "REQUEST_METADATA"]),
    ("SOCIAL_MEDIA", "MEDIA", ["SOCIAL_CONTENT", "PUBLISHING_RECORDS"]),
    ("FREELANCER", "BUSINESS", ["PROJECT_RECORDS", "WORK_DELIVERABLES"]),
    ("CULTURAL_KNOWLEDGE", "KNOWLEDGE", ["CULTURAL_RECORDS", "SOURCE_REFERENCES", "EVIDENCE_METADATA", "PROVENANCE"]),
)

PROVIDER_IDS = ("aws", "google", "mega", "microsoft", "proton")


def _category_records() -> list[dict[str, Any]]:
    records = []
    for key, kind, capabilities in CATEGORIES:
        records.append({
            "ecosystem_id": f"GLOBAL-{key.replace('_', '-')}-DATABASE-ECOSYSTEM",
            "name": f"GLOBAL {key.replace('_', ' ')} DATABASE ECOSYSTEM",
            "ecosystem_type": kind,
            "parent_id": ROOT_ID,
            "capabilities": list(capabilities),
            "metadata": {"ownership": "DATABASE"},
        })
    return records


def _provider_records() -> list[dict[str, Any]]:
    base = Path(__file__).resolve().parent
    records = []
    for provider in PROVIDER_IDS:
        folder = base / f"{provider}_database_ecosystem"
        if not folder.is_dir():
            continue
        records.append({
            "ecosystem_id": f"GLOBAL-{provider.upper()}-DATABASE-ECOSYSTEM",
            "name": f"GLOBAL {provider.upper()} DATABASE ECOSYSTEM",
            "ecosystem_type": "DATABASE_PROVIDER",
            "parent_id": ROOT_ID,
            "repository_ref": str(folder.relative_to(base)),
            "capabilities": ["PROVIDER_ADAPTER", "DATA_SERVICE_DISCOVERY"],
            "metadata": {"provider_id": provider, "connection_status": "NOT_CONFIGURED"},
        })
        for directory in sorted(p for p in folder.rglob("*") if p.is_dir()):
            relative = directory.relative_to(folder).parts
            slug = "-".join(part.upper().replace("_", "-") for part in relative)
            records.append({
                "ecosystem_id": f"GLOBAL-{provider.upper()}-{slug}-DATABASE-ECOSYSTEM",
                "name": f"GLOBAL {provider.upper()} {' '.join(relative).replace('_', ' ').upper()} DATABASE ECOSYSTEM",
                "ecosystem_type": "DATABASE_NAMESPACE",
                "parent_id": f"GLOBAL-{provider.upper()}-DATABASE-ECOSYSTEM",
                "repository_ref": str(directory.relative_to(base)),
                "capabilities": ["DATABASE_NAMESPACE"],
                "metadata": {"ownership": "DATABASE", "implementation_state": "SCAFFOLDED"},
            })
    return records


def get_catalog() -> list[dict[str, Any]]:
    """Return a fresh parent-first catalog of DATABASE-owned ecosystem nodes."""
    return [deepcopy(ROOT), *_category_records(), *_provider_records()]


def get_root_catalog() -> dict[str, Any]:
    return deepcopy(ROOT)
