"""STORAGE domain entry point."""
from backend.STORAGE.GLOBAL_ECOSYSTEM.GLOBAL_STORAGE_ECOSYSTEM.service import EcosystemService


class DomainService:
    domain = "STORAGE"
    ecosystem_package = "backend.STORAGE.GLOBAL_ECOSYSTEM.GLOBAL_STORAGE_ECOSYSTEM"

    def __init__(self):
        self.ecosystem = EcosystemService()

    def describe(self):
        return {
            "domain": self.domain,
            "ecosystem_package": self.ecosystem_package,
            "status": "FOUNDATION_READY",
            "ecosystem": self.ecosystem.describe(),
        }
