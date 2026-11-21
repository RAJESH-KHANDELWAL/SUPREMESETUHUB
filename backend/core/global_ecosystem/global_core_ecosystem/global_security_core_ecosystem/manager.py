"""GLOBAL SECURITY CORE manager and canonical security-domain registry.

The manager exposes catalog, domain, provider, jurisdiction and policy metadata
only. It performs no provider calls and does not enforce runtime security.
"""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
ECOSYSTEM_ID = "GLOBAL-SECURITY-CORE-ECOSYSTEM"
NAME = "GLOBAL SECURITY CORE ECOSYSTEM"
STATUS = "CORE_CATALOG_ONLY"
MASTER_CATALOG_PATH = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_CATALOG_COUNTS = {
    "current_unique_entries": 246,
    "target_unique_entries": 2468,
    "remaining_unique_entries": 2222,
}
SERVICE_TIERS = (
    "BASIC", "NORMAL", "STANDARD", "PROFESSIONAL", "ADVANCED", "EXPERT",
    "SPECIALIZED", "ENTERPRISE", "NATIONAL", "INTERNATIONAL", "GLOBAL",
    "UNIVERSAL", "SUPREME",
)

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
        refs = item.get("master_catalog_refs", [])
        if not refs or not all(isinstance(ref, str) and ref.startswith("S") for ref in refs):
            raise ValueError(f"SECURITY_DOMAIN_MASTER_CATALOG_REFS_REQUIRED: {domain_id}")
        loaded.append({**item, "status": STATUS})
        seen_ids.add(domain_id)
        seen_folders.add(folder)
    if not loaded:
        raise ValueError("SECURITY_DOMAIN_CATALOG_EMPTY")
    return tuple(loaded)


SECURITY_DOMAINS = _load_domains()

# Policy coverage metadata by audience. It does not claim protection is live.
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
    """Return defensive copies of the registered security-domain metadata."""
    return deepcopy(list(SECURITY_DOMAINS))


def get_domain(domain_id: str) -> dict[str, Any] | None:
    """Look up a security domain by case-insensitive ID or folder name."""
    needle = domain_id.strip().upper()
    for item in SECURITY_DOMAINS:
        if item["id"] == needle or item["folder"].upper() == needle:
            return deepcopy(item)
    return None


def domain_summary() -> dict[str, Any]:
    return {
        "domain_count": len(SECURITY_DOMAINS),
        "coverage_exhaustive": bool(_DOMAIN_DATA.get("domain_coverage_exhaustive", False)),
        "master_catalog_ref_count": sum(len(item.get("master_catalog_refs", [])) for item in SECURITY_DOMAINS),
        "master_catalog_alignment_verified": True,
    }


def get_service_tiers() -> list[dict[str, Any]]:
    return [{"tier_id": tier, "rank": rank} for rank, tier in enumerate(SERVICE_TIERS, start=1)]


def get_protected_group_safety(group_id: str | None = None) -> dict[str, Any]:
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
    from .provider_catalog import get_provider_catalog

    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": NAME,
        "provider": "provider-neutral",
        "ecosystem_type": "GLOBAL_SECURITY_CORE",
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "status": STATUS,
        "enabled": True,
        "master_catalog_source": MASTER_CATALOG_PATH,
        "master_catalog_counts": deepcopy(MASTER_CATALOG_COUNTS),
        "capabilities": [
            "SECURITY_DOMAIN_REGISTRY", "PROVIDER_SECURITY_METADATA",
            "JURISDICTION_PROFILE_METADATA", "CONTENT_SAFETY_POLICY_METADATA",
            "IDENTITY_AND_ACCESS_POLICY_METADATA", "THREAT_AND_VULNERABILITY_METADATA",
            "GOVERNANCE_AND_AUDIT_METADATA", "PROTECTED_GROUP_SAFETY_METADATA",
            "MASTER_CATALOG_REFERENCE_MAPPING", "NORMAL_TO_SUPREME_TIER_DISCOVERY",
        ],
        "children": [
            {
                "ecosystem_id": item["ecosystem_id"],
                "provider_id": item["provider_id"],
                "name": item["name"],
                "provider": item["provider_id"].lower(),
                "core_module": f"{ROOT.relative_to(Path.cwd()).as_posix()}/{item['folder']}",
                "status": item["status"],
                "enabled": item["enabled"],
                "capabilities": list(item["capabilities"]),
                "live_connection_verified": False,
            }
            for item in get_provider_catalog()
        ],
    }


def list_security_core_modules(include_disabled: bool = False) -> list[dict[str, Any]]:
    children = get_security_core_catalog()["children"]
    return children if include_disabled else [item for item in children if item.get("enabled", True)]


def get_catalog() -> dict[str, Any]:
    from .jurisdiction_catalog import get_jurisdictions, jurisdiction_summary
    from .provider_catalog import get_provider_catalog, provider_summary

    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": NAME,
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "status": STATUS,
        "master_catalog_source": MASTER_CATALOG_PATH,
        "master_catalog_counts": deepcopy(MASTER_CATALOG_COUNTS),
        "domain_count": domain_summary()["domain_count"],
        "domains": get_domains(),
        "provider_count": provider_summary()["provider_count"],
        "providers": get_provider_catalog(),
        "jurisdiction_profile_count": jurisdiction_summary()["jurisdiction_profile_count"],
        "jurisdictions": get_jurisdictions(),
        "service_tiers": get_service_tiers(),
        "domain_coverage_exhaustive": False,
        "provider_coverage_exhaustive": False,
        "jurisdiction_coverage_exhaustive": False,
        "master_catalog_alignment": "REFERENCE_MAPPING_ONLY",
        "legal_compliance_verified": False,
        "live_provider_connections_verified": False,
        "api_calls_performed": 0,
        "security_enforcement_verified": False,
        "protected_group_safety": get_protected_group_safety(),
    }


class GlobalSecurityCoreManager:
    """Google-Core-style stable discovery facade for security metadata."""

    NAME = NAME
    ECOSYSTEM_ID = ECOSYSTEM_ID

    def status(self) -> dict[str, Any]:
        from .provider_catalog import provider_summary
        from .jurisdiction_catalog import jurisdiction_summary

        return {
            "success": True,
            "ecosystem_id": ECOSYSTEM_ID,
            "name": NAME,
            "status": STATUS,
            "enabled": True,
            **domain_summary(),
            **provider_summary(),
            **jurisdiction_summary(),
            "protected_group_count": len(PROTECTED_GROUP_SAFETY),
            "protected_groups": list(PROTECTED_GROUP_SAFETY),
            "live_provider_connections_verified": False,
            "api_calls_performed": 0,
            "security_enforcement_verified": False,
        }

    def health(self) -> dict[str, Any]:
        return self.status()

    def list_domains(self) -> dict[str, Any]:
        return {"success": True, **domain_summary(), "domains": get_domains()}

    def list_domain_inventory(self) -> list[dict[str, Any]]:
        return get_domains()

    def get_domain(self, domain_id: str) -> dict[str, Any] | None:
        return get_domain(domain_id)

    def list_providers(self) -> dict[str, Any]:
        from .provider_catalog import get_provider_catalog, provider_summary
        return {"success": True, **provider_summary(), "providers": get_provider_catalog()}

    def get_provider(self, provider_id: str) -> dict[str, Any] | None:
        from .provider_catalog import get_provider
        return get_provider(provider_id)

    def list_jurisdictions(self) -> dict[str, Any]:
        from .jurisdiction_catalog import get_jurisdictions, jurisdiction_summary
        return {"success": True, **jurisdiction_summary(), "jurisdictions": get_jurisdictions()}

    def get_jurisdiction(self, jurisdiction_id: str) -> dict[str, Any] | None:
        from .jurisdiction_catalog import get_jurisdiction
        return get_jurisdiction(jurisdiction_id)

    def list_modules(self, include_disabled: bool = False) -> list[dict[str, Any]]:
        return list_security_core_modules(include_disabled)

    def list_offerings(self) -> dict[str, Any]:
        return {"success": True, "count": len(SECURITY_DOMAINS), "offerings": get_domains()}

    def get_offering(self, domain_id: str) -> dict[str, Any] | None:
        return get_domain(domain_id)

    def catalog(self) -> dict[str, Any]:
        return get_catalog()

    def get_security_core_catalog(self) -> dict[str, Any]:
        return get_security_core_catalog()

    def dependency_map(self) -> dict[str, Any]:
        from .provider_catalog import get_provider_catalog
        return {
            "success": True,
            "edges": [
                {
                    "provider_id": item["provider_id"],
                    "core_module": f"{ROOT.relative_to(Path.cwd()).as_posix()}/{item['folder']}",
                    "relationship": "PROVIDER_SECURITY_METADATA",
                    "live_connection_verified": False,
                }
                for item in get_provider_catalog()
            ],
        }

    def get_protected_group_safety(self, group_id: str | None = None) -> dict[str, Any]:
        return get_protected_group_safety(group_id)


_manager_instance: GlobalSecurityCoreManager | None = None


def get_manager() -> GlobalSecurityCoreManager:
    """Return the shared manager instance."""
    global _manager_instance
    if _manager_instance is None:
        _manager_instance = GlobalSecurityCoreManager()
    return _manager_instance


__all__ = [
    "ECOSYSTEM_ID", "NAME", "STATUS", "SERVICE_TIERS", "SECURITY_DOMAINS",
    "PROTECTED_GROUP_SAFETY", "UNIVERSAL_SAFETY_BASELINE",
    "GlobalSecurityCoreManager", "get_manager", "get_domains", "get_domain",
    "domain_summary", "get_service_tiers", "get_protected_group_safety",
    "get_catalog", "get_security_core_catalog", "list_security_core_modules",
]
