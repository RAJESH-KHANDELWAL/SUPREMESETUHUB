"""Canonical paths and ownership for the GLOBAL INFRASTRUCTURE ECOSYSTEM."""

INFRASTRUCTURE_MODULES = (
    "backup", "billing", "cdn", "containers", "database", "dns", "domains",
    "email", "firewall", "ftp", "hosting", "ipam", "load_balancer", "model",
    "monitoring", "network", "object_storage", "security", "server", "ssl", "storage",
)

INFRASTRUCTURE_ROOT_MODULES = (
    "controller", "hostinger_api", "hostinger_catalog", "nsfwinfra", "repository", "service",
)

ECOSYSTEM_ROOT = "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem"

ECOSYSTEM_DOMAIN_PATHS = {
    name: f"{ECOSYSTEM_ROOT}.{name}" for name in INFRASTRUCTURE_MODULES
}

# Compatibility import paths are retained by backend.infrastructure.__path__;
# the actual packages are physically stored under ECOSYSTEM_ROOT.
CANONICAL_DOMAIN_PATHS = dict(ECOSYSTEM_DOMAIN_PATHS)

ROOT_MODULE_ADAPTER_PATH = f"{ECOSYSTEM_ROOT}.modules"

INTEGRATION_PATHS = {
    "core": f"{ECOSYSTEM_ROOT}.integrations.core",
    "global_core_ecosystem": f"{ECOSYSTEM_ROOT}.integrations.global_core_ecosystem",
    "global_infrastructure_core_ecosystem": "backend.core.global_ecosystem.global_core_ecosystem.global_infrastructure_core_ecosystem",
}

def get_module_paths() -> dict[str, str]:
    """Return canonical ecosystem package paths for all infrastructure domains."""
    return dict(CANONICAL_DOMAIN_PATHS)

def get_ecosystem_domain_paths() -> dict[str, str]:
    """Return direct root-level ecosystem package paths for all domains."""
    return dict(ECOSYSTEM_DOMAIN_PATHS)

def get_root_module_paths() -> dict[str, str]:
    return {name: f"backend.infrastructure.{name}" for name in INFRASTRUCTURE_ROOT_MODULES}

def get_canonical_ownership() -> dict[str, str]:
    return {
        "infrastructure_control_plane": "backend.infrastructure",
        "infrastructure_global_hub": ECOSYSTEM_ROOT,
        "infrastructure_domain_sources": f"{ECOSYSTEM_ROOT}/<domain>",
        "infrastructure_domain_adapters": f"{ECOSYSTEM_ROOT}/<domain>",
        "infrastructure_root_module_adapters": ROOT_MODULE_ADAPTER_PATH,
        "core_foundation": "backend.core",
        "core_global_ecosystem_facade": "backend.core.global_ecosystem",
        "global_core_ecosystem": "backend.core.global_ecosystem.global_core_ecosystem",
        "global_infrastructure_core_ecosystem": INTEGRATION_PATHS["global_infrastructure_core_ecosystem"],
        "core_integration_adapter": INTEGRATION_PATHS["core"],
        "global_core_integration_adapter": INTEGRATION_PATHS["global_core_ecosystem"],
        "global_ecosystem_root": "backend.global_ecosystem",
        "server_ecosystem": "backend.server.global_ecosystem.global_server_ecosystem",
        "database_persistence": "backend.database",
        "storage_implementation": "backend.storage",
        "http_orchestration": "backend.api",
        "provider_execution": "backend.engine",
    }
