"""Uppercase legacy compatibility facade; implementation lives in lowercase SERVER."""
from backend.server.global_ecosystem.global_server_ecosystem import EcosystemService
class DomainService:
    domain = "SERVER"
    ecosystem_package = "backend.server.global_ecosystem.global_server_ecosystem"
    def __init__(self):
        self.ecosystem = EcosystemService()
    def describe(self):
        return {
            "domain": self.domain,
            "ecosystem_package": self.ecosystem_package,
            "status": "FOUNDATION_READY",
            "ecosystem": self.ecosystem.describe(),
        }
