"""Canonical subsystem catalog for core, engines, data, and infrastructure.

This catalog links to existing project modules. It does not claim that external
DNS, VPS, VPN, cloud, storage, or database providers are connected or provisioned.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any


SUBSYSTEM_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {
        "subsystem_id": "core",
        "name": "GLOBAL CORE ECOSYSTEM",
        "purpose": "Shared application foundation, readiness, configuration, and lifecycle boundaries.",
        "code_paths": ["backend/engines/core", "backend/api/core_readiness.py"],
        "status": "EXISTING_FOUNDATION_LINKED",
        "external_connection_verified": False,
    },
    {
        "subsystem_id": "engine",
        "name": "GLOBAL ENGINE ECOSYSTEM",
        "purpose": "Registry and orchestration layer for independent runtime engines.",
        "code_paths": ["backend/engines", "backend/engines/base.py", "backend/engines/ecosystem"],
        "status": "EXISTING_FOUNDATION_LINKED",
        "external_connection_verified": False,
    },
    {
        "subsystem_id": "database",
        "name": "GLOBAL DATABASE ECOSYSTEM",
        "purpose": "Database connections, models, services, persistence, and data-platform adapters.",
        "code_paths": ["backend/database", "backend/engines/database", "backend/database/global_ecosystem/global_database_ecosystem/google_database_ecosystem/service.py"],
        "status": "EXISTING_FOUNDATION_LINKED",
        "external_connection_verified": False,
    },
    {
        "subsystem_id": "storage",
        "name": "GLOBAL STORAGE ECOSYSTEM",
        "purpose": "Local and provider-backed file/object storage, backup, and storage lifecycle.",
        "code_paths": ["backend/engines/storage", "backend/api/storage_routes.py", "backend/api/storage.py", "backend/storage/global_ecosystem/global_storage_ecosystem/google_storage/service.py"],
        "status": "EXISTING_FOUNDATION_LINKED",
        "external_connection_verified": False,
    },
    {
        "subsystem_id": "dns",
        "name": "GLOBAL DNS ECOSYSTEM",
        "purpose": "DNS records, zones, domain routing, and registrar/provider adapter boundaries.",
        "code_paths": ["backend/api/dns.py", "backend/engines/connectivity", "backend/dns/global_ecosystem/global_dns_ecosystem/google_dns/service.py"],
        "status": "EXISTING_FOUNDATION_LINKED",
        "external_connection_verified": False,
    },
    {
        "subsystem_id": "vps",
        "name": "GLOBAL VPS ECOSYSTEM",
        "purpose": "Virtual server inventory, provisioning adapters, deployment, and server operations.",
        "code_paths": ["backend/api/infrastructure.py", "backend/engines/cloud", "backend/server/global_ecosystem/global_server_ecosystem/google_server/service.py"],
        "status": "FOUNDATION_LINKED_ADAPTERS_PENDING",
        "external_connection_verified": False,
    },
    {
        "subsystem_id": "vpn",
        "name": "GLOBAL VPN ECOSYSTEM",
        "purpose": "VPN provider configuration, tunnel lifecycle, and connectivity health boundaries.",
        "code_paths": ["backend/engines/connectivity", "backend/api/infrastructure.py"],
        "status": "FOUNDATION_LINKED_ADAPTERS_PENDING",
        "external_connection_verified": False,
    },
    {
        "subsystem_id": "cloud",
        "name": "GLOBAL CLOUD ECOSYSTEM",
        "purpose": "Cloud accounts, compute, networking, managed services, and provider adapters.",
        "code_paths": ["backend/engines/cloud", "backend/api/cloud.py", "backend/api/infrastructure.py", "backend/cloud/global_ecosystem/global_cloud_ecosystem/google_cloud/service.py"],
        "status": "EXISTING_FOUNDATION_LINKED",
        "external_connection_verified": False,
    },
)


def list_subsystem_ecosystems() -> list[dict[str, Any]]:
    """Return an isolated copy so callers cannot mutate the canonical catalog."""
    return deepcopy(list(SUBSYSTEM_ECOSYSTEMS))


def get_subsystem_ecosystem(subsystem_id: str) -> dict[str, Any] | None:
    """Get a subsystem by case-insensitive ID."""
    key = subsystem_id.strip().casefold()
    for item in SUBSYSTEM_ECOSYSTEMS:
        if item["subsystem_id"] == key:
            return deepcopy(item)
    return None
