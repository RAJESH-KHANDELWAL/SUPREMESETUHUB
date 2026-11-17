"""Canonical Global Security CORE registry and compatibility facade."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, PARENT_ECOSYSTEM_ID, STATUS
from .domain_catalog import get_domains, domain_summary
from .jurisdiction_catalog import get_jurisdictions, jurisdiction_summary
from .provider_catalog import get_provider_catalog, provider_summary

SECURITY_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": ECOSYSTEM_ID,
    "name": ECOSYSTEM_NAME,
    "parent_id": PARENT_ECOSYSTEM_ID,
    "status": STATUS,
    "enabled": True,
    "capabilities": [
        "SECURITY_DOMAIN_REGISTRY", "PROVIDER_SECURITY_METADATA",
        "JURISDICTION_PROFILE_METADATA", "CONTENT_SAFETY_POLICY_METADATA",
        "IDENTITY_AND_ACCESS_POLICY_METADATA", "THREAT_AND_VULNERABILITY_METADATA",
        "GOVERNANCE_AND_AUDIT_METADATA",
    ],
    "children": [{
        "ecosystem_id": x["ecosystem_id"], "provider_id": x["provider_id"],
        "name": x["name"], "provider": x["provider_id"].lower(),
        "core_module": f"backend/core/global_ecosystem/global_core_ecosystem/global_security_core_ecosystem/{x['folder']}",
        "status": x["status"], "enabled": x["enabled"],
        "capabilities": list(x["capabilities"]), "live_connection_verified": False,
    } for x in get_provider_catalog()],
}

def get_security_core_catalog():
    return deepcopy(SECURITY_CORE_ECOSYSTEM)

def list_security_core_modules(include_disabled=False):
    items = get_security_core_catalog()["children"]
    return items if include_disabled else [x for x in items if x.get("enabled", True)]

def get_catalog():
    return {
        "ecosystem_id": ECOSYSTEM_ID, "name": ECOSYSTEM_NAME,
        "parent_id": PARENT_ECOSYSTEM_ID, "status": STATUS,
        "domain_count": domain_summary()["domain_count"], "domains": get_domains(),
        "provider_count": provider_summary()["provider_count"], "providers": get_provider_catalog(),
        "jurisdiction_profile_count": jurisdiction_summary()["jurisdiction_profile_count"],
        "jurisdictions": get_jurisdictions(),
        "service_tiers": [{"tier_id": x, "rank": i + 1} for i, x in enumerate(
            ("NORMAL", "BASIC", "STANDARD", "PREMIUM", "PROFESSIONAL", "ENTERPRISE", "SUPREME")
        )],
        "domain_coverage_exhaustive": False, "provider_coverage_exhaustive": False,
        "jurisdiction_coverage_exhaustive": False, "legal_compliance_verified": False,
        "live_provider_connections_verified": False, "api_calls_performed": 0,
        "security_enforcement_verified": False,
    }
