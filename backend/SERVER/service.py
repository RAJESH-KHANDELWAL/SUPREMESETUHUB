"""SERVER domain facade backed by its canonical ecosystem."""
from backend.SERVER.GLOBAL_ECOSYSTEM.GLOBAL_SERVER_ECOSYSTEM import EcosystemService


class DomainService:
    domain = "SERVER"
    ecosystem_package = "backend.SERVER.GLOBAL_ECOSYSTEM.GLOBAL_SERVER_ECOSYSTEM"

    def __init__(self):
        self.ecosystem = EcosystemService()

    def describe(self):
        return {
            "domain": self.domain,
            "ecosystem_package": self.ecosystem_package,
            "status": "FOUNDATION_READY",
            "ecosystem": self.ecosystem.describe(),
        }
