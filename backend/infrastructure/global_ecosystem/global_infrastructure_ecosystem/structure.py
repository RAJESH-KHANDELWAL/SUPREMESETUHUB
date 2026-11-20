"""Canonical paths and ownership for the GLOBAL INFRASTRUCTURE ECOSYSTEM."""
INFRASTRUCTURE_MODULES = (
    "backup", "billing", "cdn", "containers", "database", "dns", "domains",
    "email", "firewall", "ftp", "hosting", "ipam", "load_balancer", "model",
    "monitoring", "network", "object_storage", "security", "server", "ssl", "storage",
)
INFRASTRUCTURE_ROOT_MODULES = ("controller", "hostinger_api", "hostinger_catalog", "nsfwinfra", "repository", "service")
ECOSYSTEM_ROOT = "backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem"
ECOSYSTEM_DOMAIN_PATHS = {name: f"{ECOSYSTEM_ROOT}.{name}" for name in INFRASTRUCTURE_MODULES}
CANONICAL_DOMAIN_PATHS = dict(ECOSYSTEM_DOMAIN_PATHS)
ROOT_MODULE_ADAPTER_PATH = f"{ECOSYSTEM_ROOT}.modules"
CANONICAL_ROOT_MODULE_PATHS = {name: f"{ROOT_MODULE_ADAPTER_PATH}.{name}" for name in INFRASTRUCTURE_ROOT_MODULES if name in {"controller","repository","service","hostinger_catalog"}}
INTEGRATION_PATHS = {
    "core": f"{ECOSYSTEM_ROOT}.integrations.core",
    "global_core_ecosystem": f"{ECOSYSTEM_ROOT}.integrations.global_core_ecosystem",
    "global_infrastructure_core_ecosystem": "backend.core.global_ecosystem.global_core_ecosystem.global_infrastructure_core_ecosystem",
}
def get_module_paths() -> dict[str, str]: return dict(CANONICAL_DOMAIN_PATHS)
def get_ecosystem_domain_paths() -> dict[str, str]: return dict(ECOSYSTEM_DOMAIN_PATHS)
def get_root_module_paths() -> dict[str, str]:
    paths = {name: f"backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.modules.{name}" for name in ("controller","repository","service","hostinger_catalog")}
    paths.update({"hostinger_api":"backend.infrastructure.global_ecosystem.hostinger_api","nsfwinfra":"backend.infrastructure.global_ecosystem.nsfwinfra"})
    return paths
def get_canonical_ownership() -> dict[str, str]:
    return {
        "infrastructure_control_plane": ECOSYSTEM_ROOT,
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
