"""Backend Global Ecosystem manager after foundation consolidation."""
from pathlib import Path

CONSOLIDATED_DOMAIN_FOLDERS = (
    "audit", "core", "dependencies", "file_manager",
    "identity", "registry", "security", "sync",
)


class GlobalEcosystemManager:
    NAME = "BACKEND GLOBAL ECOSYSTEM"
    VERSION = "1.2.0"

    def __init__(self):
        self.root = Path(__file__).resolve().parent
        self.status = "READY"

    def initialize(self):
        self.status = "RUNNING"
        return self.health()

    def health(self):
        foundation = self.root / "global_foundation_ecosystem"
        checks = {
            "package_init": (self.root / "__init__.py").is_file(),
            "manager": (self.root / "manager.py").is_file(),
            "php_bridge": (self.root / "manager.php").is_file(),
            "global_foundation_ecosystem": foundation.is_dir(),
            "foundation_domains_consolidated": all(
                not (foundation / name).exists()
                for name in CONSOLIDATED_DOMAIN_FOLDERS
            ),
        }
        return {
            "name": self.NAME,
            "version": self.VERSION,
            "status": self.status,
            "checks": checks,
            "healthy": all(checks.values()),
        }

    def get_global_foundation_manager(self):
        from .global_foundation_ecosystem.manager import GlobalFoundationEcosystemManager
        return GlobalFoundationEcosystemManager()


def get_manager():
    return GlobalEcosystemManager()
