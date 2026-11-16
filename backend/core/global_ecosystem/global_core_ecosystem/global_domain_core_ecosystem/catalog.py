"""Canonical provider-neutral Global Domain Core catalog."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

GLOBAL_DOMAIN_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "GLOBAL-DOMAIN-CORE-ECOSYSTEM",
    "name": "GLOBAL DOMAIN CORE ECOSYSTEM",
    "ecosystem_type": "CORE_SERVICE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "capabilities": [
        "DOMAIN_PROVIDER_REGISTRY",
        "DOMAIN_REGISTRAR_DISCOVERY",
        "DNS_AND_NAMESERVER_CAPABILITY_METADATA",
        "REGISTRY_GOVERNANCE_AND_LOOKUP",
        "TLS_CERTIFICATE_LIFECYCLE_METADATA",
        "DOMAIN_HOSTING_ASSOCIATION_METADATA",
        "TENANT_SCOPED_DOMAIN_POLICY",
        "PROVIDER_READINESS_AND_HEALTH_METADATA",
        "CROSS_PROVIDER_DEPENDENCY_DISCOVERY",
    ],
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_domain_api_ecosystem",
    "provider_catalog_ref": "backend/core/global_ecosystem/global_core_ecosystem/global_domain_core_ecosystem/provider_catalog.py",
    "live_connections_verified": 0,
    "api_calls_performed": 0,
}

DOMAIN_CAPABILITY_DOMAINS: tuple[dict[str, Any], ...] = (
    {"domain_id":"REGISTRAR_AND_RESELLER","name":"Registrar and Reseller","purpose":"Registration, renewal, transfer and registrar account metadata."},
    {"domain_id":"DNS_AND_NAMESERVER","name":"DNS and Nameserver","purpose":"DNS zones, records, delegation, nameserver and DNSSEC metadata."},
    {"domain_id":"REGISTRY_GOVERNANCE_AND_LOOKUP","name":"Registry Governance and Lookup","purpose":"Registry policy references, RDAP/WHOIS and domain discovery metadata."},
    {"domain_id":"CERTIFICATE_AND_TLS","name":"Certificate and TLS","purpose":"Certificate inventory, TLS lifecycle and expiry metadata."},
    {"domain_id":"HOSTING_AND_INFRASTRUCTURE","name":"Hosting and Infrastructure","purpose":"Domain-to-hosting, origin, deployment and infrastructure associations."},
    {"domain_id":"CROSS_PROVIDER_DOMAIN_OPERATIONS","name":"Cross-provider Domain Operations","purpose":"Portfolio, lifecycle, migration and cross-provider coordination metadata."},
)

def get_domain_core_catalog() -> dict[str, Any]:
    return deepcopy(GLOBAL_DOMAIN_CORE_ECOSYSTEM)

def list_domain_capability_domains() -> list[dict[str, Any]]:
    return deepcopy(list(DOMAIN_CAPABILITY_DOMAINS))
