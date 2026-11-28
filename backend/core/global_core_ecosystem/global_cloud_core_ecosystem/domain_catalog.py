"""Cloud Core domains and deterministic provider/workload classification."""
from __future__ import annotations
from collections import Counter
from typing import Any
from backend.global_ecosystem.global_cloud_ecosystem import list_cloud_providers, list_cloud_workloads

CLOUD_DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
    "CLOUD_GOVERNANCE": {"name": "Cloud Governance and Provider Lifecycle", "purpose": "Provider identity, catalog governance, lifecycle, policy, readiness and cost controls."},
    "COMPUTE_AND_ACCELERATION": {"name": "Compute and Acceleration", "purpose": "Virtual machines, bare metal, GPU compute, containers and accelerated workloads."},
    "STORAGE_AND_BACKUP": {"name": "Storage, Backup and Content", "purpose": "Object, block and file storage, backup, sync, sharing and recovery."},
    "DATABASE_AND_DATA": {"name": "Database and Data Platforms", "purpose": "Relational/document databases, caches, analytics, warehouses and data processing."},
    "NETWORK_AND_EDGE": {"name": "Networking, DNS and Edge", "purpose": "VPC, routing, DNS, CDN, edge delivery, private connectivity and network security."},
    "APPLICATION_PLATFORM": {"name": "Application and Developer Platforms", "purpose": "Application hosting, serverless, deployment, managed platforms and developer environments."},
    "SECURITY_AND_IDENTITY": {"name": "Security, Identity and Compliance", "purpose": "IAM, encryption, key/secrets management, audit, threat protection and compliance."},
    "REGIONAL_AND_SOVEREIGN_CLOUD": {"name": "Regional, Hybrid and Sovereign Cloud", "purpose": "India regions, data residency, sovereign deployments, hybrid and multi-cloud placement."},
    "PERSONAL_AND_COLLABORATION_CLOUD": {"name": "Personal Storage and Collaboration Cloud", "purpose": "Consumer file storage, sync, device backup, file transfer and collaboration."},
    "ENTERPRISE_AND_SPECIALTY_CLOUD": {"name": "Enterprise and Specialty Cloud Workloads", "purpose": "Enterprise content platforms, managed services, media, specialist and cross-domain workloads."},
}

_CAPABILITY_RULES = (
    (("compute", "virtual_machines", "cloud_servers", "gpu_compute", "bare_metal", "containers"), "COMPUTE_AND_ACCELERATION"),
    (("object_storage", "block_storage", "file_storage", "storage", "backup", "sync", "sharing", "encrypted_storage", "device_backup"), "STORAGE_AND_BACKUP"),
    (("database", "databases", "warehouse", "analytics", "data_services", "data_processing", "cache"), "DATABASE_AND_DATA"),
    (("network", "networking", "dns", "cdn", "edge", "connectivity"), "NETWORK_AND_EDGE"),
    (("hosting", "serverless", "deployment", "functions", "application_hosting", "frontend_deployment", "kubernetes"), "APPLICATION_PLATFORM"),
    (("security", "identity", "key_management", "secrets", "audit", "compliance", "zero_trust"), "SECURITY_AND_IDENTITY"),
    (("enterprise", "hybrid_cloud", "sovereign", "regional", "data_residency", "multi_cloud"), "REGIONAL_AND_SOVEREIGN_CLOUD"),
    (("personal_storage", "file_sync", "file_transfer", "collaboration", "consumer_storage"), "PERSONAL_AND_COLLABORATION_CLOUD"),
)

def _domain_for(provider: dict[str, Any]) -> tuple[str, str]:
    provider_id = provider["id"]
    if provider_id.endswith("_india") or provider_id in {"oracle_cloud_india", "aws_india", "azure_india", "gcp_india"}:
        return "REGIONAL_AND_SOVEREIGN_CLOUD", "REGIONAL_PROVIDER_RULE"
    tokens = set(provider.get("capabilities", ()))
    for needles, domain_id in _CAPABILITY_RULES:
        if any(any(needle in token for needle in needles) for token in tokens):
            return domain_id, "CAPABILITY_RULE"
    return "ENTERPRISE_AND_SPECIALTY_CLOUD", "SPECIALTY_REVIEW_REQUIRED"

def list_cloud_domain_inventory() -> list[dict[str, Any]]:
    inventory = []
    for provider in list_cloud_providers():
        domain_id, rule = _domain_for(provider)
        definition = CLOUD_DOMAIN_DEFINITIONS[domain_id]
        inventory.append({**provider, "core_domain_id": domain_id,
                          "core_domain_name": definition["name"], "domain_assignment": rule})
    return inventory

def cloud_domain_summary() -> dict[str, Any]:
    inventory = list_cloud_domain_inventory()
    counts = Counter(item["core_domain_id"] for item in inventory)
    workloads = list_cloud_workloads()
    return {
        "success": True, "domain_count": len(CLOUD_DOMAIN_DEFINITIONS),
        "provider_count": len(inventory), "workload_count": len(workloads),
        "domains": [{"domain_id": domain_id, **definition,
                     "provider_count": counts.get(domain_id, 0)}
                    for domain_id, definition in CLOUD_DOMAIN_DEFINITIONS.items()],
        "live_connections_verified": 0,
        "note": "Domain classification is metadata only; it does not verify provider API availability, regional entitlement or live connectivity.",
    }

__all__ = ["CLOUD_DOMAIN_DEFINITIONS", "list_cloud_domain_inventory", "cloud_domain_summary"]
