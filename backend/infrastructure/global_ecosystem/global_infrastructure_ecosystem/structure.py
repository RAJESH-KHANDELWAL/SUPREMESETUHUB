"""Canonical infrastructure module paths and cross-layer ownership boundaries."""

INFRASTRUCTURE_MODULES = (
    "backup", "billing", "cdn", "containers", "database", "dns",
    "domains", "email", "firewall", "ftp", "hosting", "ipam",
    "load_balancer", "model", "monitoring", "network", "object_storage",
    "security", "server", "ssl", "storage",
)

INFRASTRUCTURE_ROOT_MODULES = (
    "controller", "hostinger_api", "hostinger_catalog", "nsfwinfra",
    "repository", "service",
)

def get_module_paths() -> dict[str, str]:
    return {name: f"backend.infrastructure.{name}" for name in INFRASTRUCTURE_MODULES}

def get_root_module_paths() -> dict[str, str]:
    return {name: f"backend.infrastructure.{name}" for name in INFRASTRUCTURE_ROOT_MODULES}

def get_canonical_ownership() -> dict[str, str]:
    return {
        "infrastructure_control_plane": "backend.infrastructure",
        "infrastructure_global_hub": "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem",
        "core_foundation": "backend.core",
        "core_global_ecosystem_facade": "backend.core.global_ecosystem",
        "global_core_ecosystem": "backend.core.global_ecosystem.global_core_ecosystem",
        "global_ecosystem_root": "backend.global_ecosystem",
        "server_ecosystem": "backend.server.global_ecosystem.global_server_ecosystem",
        "database_persistence": "backend.database",
        "storage_implementation": "backend.storage",
        "http_orchestration": "backend.api",
        "provider_execution": "backend.engine",
    }
