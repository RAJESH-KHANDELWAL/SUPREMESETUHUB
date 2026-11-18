"""GLOBAL SECURITY CORE manager and canonical security-domain registry.

This module owns security-domain discovery and protected-group safety metadata.
It describes control-plane policy only; production enforcement belongs to the
independent API, application, storage and runtime layers.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
ECOSYSTEM_ID = "GLOBAL-SECURITY-CORE-ECOSYSTEM"
STATUS = "CORE_CATALOG_ONLY"

# Canonical domain records are loaded and validated by this manager.
# Every domain package remains a direct child of this ecosystem root.
_DOMAIN_DATA = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
if _DOMAIN_DATA.get("ecosystem_id") != ECOSYSTEM_ID:
    raise ValueError("SECURITY_CATALOG_ECOSYSTEM_ID_MISMATCH")
if _DOMAIN_DATA.get("domain_package_location") != "ECOSYSTEM_ROOT":
    raise ValueError("SECURITY_DOMAIN_PACKAGE_LOCATION_INVALID")

def _load_domains() -> tuple[dict[str, Any], ...]:
    loaded: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    seen_folders: set[str] = set()
    for item in _DOMAIN_DATA.get("domains", []):
        domain_id = str(item.get("id", "")).strip().upper()
        folder = str(item.get("folder", "")).strip()
        if not domain_id or not folder:
            raise ValueError("SECURITY_DOMAIN_ID_AND_FOLDER_REQUIRED")
        if domain_id in seen_ids or folder in seen_folders:
            raise ValueError("DUPLICATE_SECURITY_DOMAIN_ID_OR_FOLDER")
        if not folder.endswith("_core_ecosystem"):
            raise ValueError(f"SECURITY_DOMAIN_CORE_ECOSYSTEM_SUFFIX_REQUIRED: {domain_id}")
        package = (ROOT / folder).resolve()
        if package.parent != ROOT:
            raise ValueError("SECURITY_DOMAIN_PACKAGE_MUST_BE_DIRECT_CHILD_OF_ECOSYSTEM_ROOT")
        manifest_path = package / "domain_manifest.json"
        if not package.is_dir() or not manifest_path.is_file() or not (package / "__init__.py").is_file():
            raise ValueError(f"SECURITY_DOMAIN_PACKAGE_INCOMPLETE: {domain_id}")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("domain_id") != domain_id:
            raise ValueError(f"SECURITY_DOMAIN_MANIFEST_ID_MISMATCH: {domain_id}")
        if manifest.get("parent_id") != ECOSYSTEM_ID:
            raise ValueError(f"SECURITY_DOMAIN_PARENT_MISMATCH: {domain_id}")
        if manifest.get("status") != STATUS:
            raise ValueError(f"SECURITY_DOMAIN_STATUS_INVALID: {domain_id}")
        loaded.append({**item, "status": STATUS})
        seen_ids.add(domain_id)
        seen_folders.add(folder)
    if not loaded:
        raise ValueError("SECURITY_DOMAIN_CATALOG_EMPTY")
    return tuple(loaded)

SECURITY_DOMAINS = _load_domains()

# Safety coverage is explicitly separated by audience. These are policy
# requirements and workflow metadata, not claims of live protection.
PROTECTED_GROUP_SAFETY: dict[str, dict[str, Any]] = {
    "MEN": {
        "label": "Men safety",
        "controls": [
            "PERSONAL_AND_PHYSICAL_SAFETY", "WORKPLACE_HARASSMENT_PREVENTION",
            "DOMESTIC_AND_RELATIONSHIP_ABUSE_REPORTING", "CYBERSTALKING_AND_IMPERSONATION",
            "PRIVACY_AND_IDENTITY_PROTECTION", "FRAUD_AND_EXTORTION_REPORTING",
            "CONSENT_AND_INTIMATE_IMAGE_PROTECTION", "MENTAL_WELLBEING_REFERRAL",
        ],
    },
    "WOMEN": {
        "label": "Women safety",
        "controls": [
            "PERSONAL_AND_PHYSICAL_SAFETY", "WORKPLACE_AND_PUBLIC_HARASSMENT_PREVENTION",
            "DOMESTIC_AND_RELATIONSHIP_ABUSE_REPORTING", "STALKING_AND_CYBERSTALKING_PROTECTION",
            "IDENTITY_LOCATION_AND_PRIVACY_PROTECTION", "SEXUAL_EXPLOITATION_AND_TRAFFICKING_PREVENTION",
            "CONSENT_AND_INTIMATE_IMAGE_PROTECTION", "FRAUD_AND_IMPERSONATION_REPORTING",
            "VICTIM_CENTRED_REPORTING_AND_SUPPORT",
        ],
    },
    "GIRLS": {
        "label": "Girls safety",
        "controls": [
            "CHILD_SAFETY_AND_AGE_ASSURANCE", "GROOMING_AND_EXPLOITATION_PREVENTION",
            "CYBERBULLYING_AND_UNSAFE_CONTACT_REPORTING", "AGE_APPROPRIATE_CONTENT_ACCESS",
            "PRIVACY_AND_LOCATION_PROTECTION", "TRUSTED_ADULT_ESCALATION",
            "CHILD_SEXUAL_ABUSE_PREVENTION_AND_LAWFUL_REPORTING",
        ],
        "minor_protection": True,
        "adult_content_access": "PROHIBITED",
    },
    "BOYS": {
        "label": "Boys safety",
        "controls": [
            "CHILD_SAFETY_AND_AGE_ASSURANCE", "GROOMING_AND_EXPLOITATION_PREVENTION",
            "CYBERBULLYING_AND_UNSAFE_CONTACT_REPORTING", "AGE_APPROPRIATE_CONTENT_ACCESS",
            "PRIVACY_AND_LOCATION_PROTECTION", "TRUSTED_ADULT_ESCALATION",
            "CHILD_SEXUAL_ABUSE_PREVENTION_AND_LAWFUL_REPORTING",
        ],
        "minor_protection": True,
        "adult_content_access": "PROHIBITED",
    },
}

UNIVERSAL_SAFETY_BASELINE = {
    "least_privilege": True,
    "privacy_by_design": True,
    "data_minimization": True,
    "consent_required_for_intimate_content": True,
    "non_consensual_intimate_imagery": "PROHIBITED",
    "child_exploitation_material": "PROHIBITED_NEVER_STORE_OR_REPRODUCE",
    "child_safety_escalation": "TRUSTED_AND_LAWFUL_REPORTING_WORKFLOWS",
    "production_enforcement_verified": False,
}

def get_domains() -> list[dict[str, Any]]:
    """Return defensive copies of every registered security domain."""
    return deepcopy(list(SECURITY_DOMAINS))

def get_domain(domain_id: str) -> dict[str, Any] | None:
    """Return one registered domain by case-insensitive ID."""
    needle = domain_id.strip().upper()
    for item in SECURITY_DOMAINS:
        if item["id"] == needle:
            return deepcopy(item)
    return None

def domain_summary() -> dict[str, Any]:
    return {
        "domain_count": len(SECURITY_DOMAINS),
        "coverage_exhaustive": bool(_DOMAIN_DATA.get("domain_coverage_exhaustive", False)),
    }

def get_protected_group_safety(group_id: str | None = None) -> dict[str, Any]:
    """Return safety policy metadata for all groups or one named group."""
    if group_id is None:
        return {
            "groups": deepcopy(PROTECTED_GROUP_SAFETY),
            "universal_baseline": deepcopy(UNIVERSAL_SAFETY_BASELINE),
            "production_enforcement_verified": False,
        }
    needle = group_id.strip().upper()
    if needle not in PROTECTED_GROUP_SAFETY:
        return {"success": False, "error": "UNKNOWN_PROTECTED_GROUP", "group_id": needle}
    return {
        "success": True,
        "group_id": needle,
        "safety": deepcopy(PROTECTED_GROUP_SAFETY[needle]),
        "universal_baseline": deepcopy(UNIVERSAL_SAFETY_BASELINE),
        "production_enforcement_verified": False,
    }


def get_security_core_catalog() -> dict[str, Any]:
    """Build the provider-neutral security CORE registry from manager-owned data."""
    from .provider_catalog import get_provider_catalog

    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": "GLOBAL SECURITY CORE ECOSYSTEM",
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "status": STATUS,
        "enabled": True,
        "capabilities": [
            "SECURITY_DOMAIN_REGISTRY", "PROVIDER_SECURITY_METADATA",
            "JURISDICTION_PROFILE_METADATA", "CONTENT_SAFETY_POLICY_METADATA",
            "IDENTITY_AND_ACCESS_POLICY_METADATA", "THREAT_AND_VULNERABILITY_METADATA",
            "GOVERNANCE_AND_AUDIT_METADATA", "PROTECTED_GROUP_SAFETY_METADATA",
        ],
        "children": [
            {
                "ecosystem_id": item["ecosystem_id"],
                "provider_id": item["provider_id"],
                "name": item["name"],
                "provider": item["provider_id"].lower(),
                "core_module": f"backend/core/global_ecosystem/global_core_ecosystem/global_security_core_ecosystem/{item['folder']}",
                "status": item["status"],
                "enabled": item["enabled"],
                "capabilities": list(item["capabilities"]),
                "live_connection_verified": False,
            }
            for item in get_provider_catalog()
        ],
    }

def list_security_core_modules(include_disabled: bool = False) -> list[dict[str, Any]]:
    items = get_security_core_catalog()["children"]
    return items if include_disabled else [item for item in items if item.get("enabled", True)]

def get_catalog() -> dict[str, Any]:
    """Return the complete security discovery view through the manager."""
    from .jurisdiction_catalog import get_jurisdictions, jurisdiction_summary
    from .provider_catalog import get_provider_catalog, provider_summary

    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": "GLOBAL SECURITY CORE ECOSYSTEM",
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "status": STATUS,
        "domain_count": domain_summary()["domain_count"],
        "domains": get_domains(),
        "provider_count": provider_summary()["provider_count"],
        "providers": get_provider_catalog(),
        "jurisdiction_profile_count": jurisdiction_summary()["jurisdiction_profile_count"],
        "jurisdictions": get_jurisdictions(),
        "service_tiers": [
            {"tier_id": tier, "rank": rank}
            for rank, tier in enumerate(
                ("NORMAL", "BASIC", "STANDARD", "PREMIUM", "PROFESSIONAL", "ENTERPRISE", "SUPREME"),
                start=1,
            )
        ],
        "domain_coverage_exhaustive": False,
        "provider_coverage_exhaustive": False,
        "jurisdiction_coverage_exhaustive": False,
        "legal_compliance_verified": False,
        "live_provider_connections_verified": False,
        "api_calls_performed": 0,
        "security_enforcement_verified": False,
        "protected_group_safety": get_protected_group_safety(),
    }

class GlobalSecurityCoreManager:
    """Read-only manager for security domains and safety policy metadata."""

    def status(self) -> dict[str, Any]:
        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "status": STATUS,
            **domain_summary(),
            "protected_group_count": len(PROTECTED_GROUP_SAFETY),
            "protected_groups": list(PROTECTED_GROUP_SAFETY),
            "production_enforcement_verified": False,
        }

    def get_domains(self) -> list[dict[str, Any]]:
        return get_domains()

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_domain(domain_id)

    def get_protected_group_safety(self, group_id: str | None = None) -> dict[str, Any]:
        return get_protected_group_safety(group_id)

    def catalog(self) -> dict[str, Any]:
        return get_catalog()

    def get_security_core_catalog(self) -> dict[str, Any]:
        return get_security_core_catalog()

    def list_modules(self, include_disabled: bool = False) -> list[dict[str, Any]]:
        return list_security_core_modules(include_disabled)

_manager_instance: GlobalSecurityCoreManager | None = None

def get_manager() -> GlobalSecurityCoreManager:
    """Return the shared GLOBAL SECURITY CORE manager instance."""
    global _manager_instance
    if _manager_instance is None:
        _manager_instance = GlobalSecurityCoreManager()
    return _manager_instance

__all__ = [
    "ECOSYSTEM_ID", "STATUS", "SECURITY_DOMAINS", "PROTECTED_GROUP_SAFETY",
    "UNIVERSAL_SAFETY_BASELINE", "GlobalSecurityCoreManager", "get_manager",
    "get_domains", "get_domain", "domain_summary", "get_protected_group_safety",
    "get_catalog", "get_security_core_catalog", "list_security_core_modules",
]
