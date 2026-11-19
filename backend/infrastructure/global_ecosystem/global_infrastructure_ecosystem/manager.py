"""Canonical Backend Global Infrastructure Ecosystem manager."""
from pathlib import Path
from .structure import INFRASTRUCTURE_MODULES
from .service import GlobalInfrastructureEcosystemService

class BackendGlobalInfrastructureEcosystemManager:
    NAME = "BACKEND GLOBAL INFRASTRUCTURE ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self):
        self.root = Path(__file__).resolve().parent

    def health(self):
        domain_checks = {name: (self.root / name).is_dir() for name in INFRASTRUCTURE_MODULES}
        count = sum(domain_checks.values())
        return {"name": self.NAME, "version": self.VERSION,
                "status": "READY" if all(domain_checks.values()) else "INCOMPLETE",
                "expected_domain_count": len(INFRASTRUCTURE_MODULES),
                "present_domain_count": count, "domain_checks": domain_checks,
                "healthy": all(domain_checks.values()),
                "provider_operations_enabled": False}

    def overview(self):
        return GlobalInfrastructureEcosystemService().get_overview()

def get_manager():
    return BackendGlobalInfrastructureEcosystemManager()
