"""Structural health manager for the Global Infrastructure Ecosystem."""
from pathlib import Path
from .structure import INFRASTRUCTURE_MODULES, INFRASTRUCTURE_ECOSYSTEM_DOMAINS
from .service import GlobalInfrastructureEcosystemService


class BackendGlobalInfrastructureEcosystemManager:
    NAME = "BACKEND GLOBAL INFRASTRUCTURE ECOSYSTEM"
    VERSION = "1.2.0"

    def __init__(self):
        self.root = Path(__file__).resolve().parent
        self.backend_root = self.root.parents[2]

    def health(self):
        required_files = (
            "README.md", "__init__.py", "catalog.py", "capabilities.py",
            "governance.py", "integrations.py", "models.py", "providers.py",
            "registry.py", "schemas.py", "service.py", "services.py",
            "structure.py", "manager.py", "manager.php",
        )
        checks = {f"root_file_{name}": (self.root / name).is_file() for name in required_files}
        module_files = ("__init__.py", "controller.py", "repository.py", "service.py", "hostinger_catalog.py")
        checks.update({f"canonical_module_{name}": (self.root / "modules" / name).is_file() for name in module_files})
        checks["core_integration_adapter"] = (self.root / "integrations" / "core" / "__init__.py").is_file()
        checks["global_core_integration_adapter"] = (self.root / "integrations" / "global_core_ecosystem" / "__init__.py").is_file()
        for name in INFRASTRUCTURE_MODULES:
            domain = self.root / name
            checks[f"domain_{name}"] = domain.is_dir() and (domain / "__init__.py").is_file()
            ecosystem_root = domain / "global_ecosystem"
            checks[f"domain_global_ecosystem_{name}"] = ecosystem_root.is_dir() and (ecosystem_root / "__init__.py").is_file()
            package = ecosystem_root / f"global_{name}_ecosystem"
            package_files = ("__init__.py",) if name in {"model", "server"} else ("__init__.py", "manager.py", "manager.php")
            checks[f"global_package_{name}"] = package.is_dir() and all((package / filename).is_file() for filename in package_files)
        for name in INFRASTRUCTURE_ECOSYSTEM_DOMAINS:
            package = self.root / name / "global_ecosystem" / f"global_{name}_ecosystem"
            checks[f"ecosystem_domain_{name}"] = package.is_dir() and (package / "README.md").is_file()
        checks["backend_global_hostinger_api"] = (self.backend_root / "global_ecosystem" / "global_hosting_ecosystem" / "hostinger_api.py").is_file()
        checks["backend_global_nsfwinfra"] = (self.backend_root / "global_ecosystem" / "nsfwinfra_ecosystem" / "nsfwinfra.py").is_file()
        domain_checks = {name: checks[f"domain_{name}"] for name in INFRASTRUCTURE_MODULES}
        ecosystem_domain_checks = {name: checks[f"ecosystem_domain_{name}"] for name in INFRASTRUCTURE_ECOSYSTEM_DOMAINS}
        healthy = all(checks.values())
        return {
            "name": self.NAME, "version": self.VERSION,
            "status": "READY" if healthy else "INCOMPLETE",
            "expected_domain_count": len(INFRASTRUCTURE_MODULES),
            "present_domain_count": sum(checks[f"domain_{name}"] for name in INFRASTRUCTURE_MODULES),
            "expected_global_package_count": len(INFRASTRUCTURE_MODULES),
            "present_global_package_count": sum(checks[f"global_package_{name}"] for name in INFRASTRUCTURE_MODULES),
            "expected_ecosystem_domain_count": len(INFRASTRUCTURE_ECOSYSTEM_DOMAINS),
            "present_ecosystem_domain_count": sum(ecosystem_domain_checks.values()),
            "checks": checks, "domain_checks": domain_checks,
            "ecosystem_domain_checks": ecosystem_domain_checks,
            "healthy": healthy, "provider_operations_enabled": False,
        }

    def overview(self):
        return GlobalInfrastructureEcosystemService().get_overview()


def get_manager():
    return BackendGlobalInfrastructureEcosystemManager()
