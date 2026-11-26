"""Backend Global Foundation Ecosystem manager."""
from pathlib import Path

FOUNDATION_DOMAINS = (
    "backup", "rebackup", "recovery", "rerecovery", "database",
    "redatabase", "history", "rehistory", "storage", "restorage",
    "sync", "resync",
)


class GlobalFoundationEcosystemManager:
    NAME = "BACKEND GLOBAL FOUNDATION ECOSYSTEM"
    VERSION = "1.1.0"

    def __init__(self):
        self.root = Path(__file__).resolve().parent
        self.status = "READY"

    def initialize(self):
        self.status = "RUNNING"
        return self.health()

    def health(self):
        checks = {
            name: (self.root / name).is_file()
            for name in ("__init__.py", "manager.py", "manager.php")
        }
        for name in FOUNDATION_DOMAINS:
            package = self.root / name / "global_ecosystem" / f"global_{name}_ecosystem"
            checks[f"domain_{name}"] = package.is_dir() and (package / "README.md").is_file()
        return {
            "name": self.NAME,
            "version": self.VERSION,
            "status": self.status,
            "expected_domain_count": len(FOUNDATION_DOMAINS),
            "present_domain_count": sum(checks[f"domain_{name}"] for name in FOUNDATION_DOMAINS),
            "checks": checks,
            "healthy": all(checks.values()),
        }

    def shutdown(self):
        self.status = "STOPPED"
        return {"name": self.NAME, "status": self.status}


def get_manager():
    return GlobalFoundationEcosystemManager()
