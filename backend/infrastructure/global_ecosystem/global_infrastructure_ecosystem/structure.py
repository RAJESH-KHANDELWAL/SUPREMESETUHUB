"""Canonical infrastructure module paths and ownership boundaries."""
INFRASTRUCTURE_MODULES = (
    "backup", "billing", "cdn", "containers", "database", "dns",
    "domains", "email", "firewall", "ftp", "hosting", "ipam",
    "load_balancer", "monitoring", "network", "object_storage",
    "security", "server", "ssl", "storage",
)

def get_module_paths() -> dict[str, str]:
    return {
        name: f"backend.infrastructure.{name}"
        for name in INFRASTRUCTURE_MODULES
    }

def get_canonical_ownership() -> dict[str, str]:
    return {
        "server_ecosystem": "backend.server.global_ecosystem.global_server_ecosystem",
        "database_persistence": "backend.database",
        "storage_implementation": "backend.storage",
        "http_orchestration": "backend.api",
        "policy_and_identity": "backend.core",
        "provider_execution": "backend.engine",
    }
