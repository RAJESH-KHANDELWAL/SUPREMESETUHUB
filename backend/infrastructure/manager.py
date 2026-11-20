"""Backend Infrastructure structural health manager."""
from pathlib import Path

class BackendInfrastructureManager:
    NAME = "BACKEND INFRASTRUCTURE"
    VERSION = "1.1.0"

    def __init__(self):
        self.root = Path(__file__).resolve().parent
        self.global_root = self.root / "global_ecosystem"
        self.ecosystem = self.global_root / "global_infrastructure_ecosystem"
        self.modules = self.ecosystem / "modules"

    def health(self):
        required_modules = ("controller.py", "repository.py", "service.py", "hostinger_catalog.py", "__init__.py")
        checks = {f"canonical_module_{name}": (self.modules / name).is_file() for name in required_modules}
        checks["root_compatibility_package"] = (self.root / "__init__.py").is_file()
        checks["global_ecosystem"] = self.global_root.is_dir()
        backend_global = self.root.parent / "global_ecosystem"
        checks["backend_global_hostinger_api"] = (backend_global / "global_hosting_ecosystem" / "hostinger_api.py").is_file()
        checks["backend_global_nsfwinfra"] = (backend_global / "nsfwinfra_ecosystem" / "nsfwinfra.py").is_file()
        checks["global_infrastructure_manager"] = (self.ecosystem / "manager.py").is_file()
        healthy = all(checks.values())
        return {"name":self.NAME,"version":self.VERSION,"status":"READY" if healthy else "INCOMPLETE",
                "checks":checks,"healthy":healthy,"provider_operations_enabled":False}

def get_manager():
    return BackendInfrastructureManager()
