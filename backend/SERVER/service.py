"""SERVER domain entry point."""
class DomainService:
    domain = "SERVER"
    ecosystem_package = "backend.SERVER.GLOBAL_ECOSYSTEM.GLOBAL_SERVER_ECOSYSTEM"
    def describe(self): return {"domain": self.domain, "ecosystem_package": self.ecosystem_package, "status": "scaffold"}
