"""SSH domain entry point."""
class DomainService:
    domain = "SSH"
    ecosystem_package = "backend.SSH.GLOBAL_ECOSYSTEM.GLOBAL_SSH_ECOSYSTEM"
    def describe(self): return {"domain": self.domain, "ecosystem_package": self.ecosystem_package, "status": "scaffold"}
