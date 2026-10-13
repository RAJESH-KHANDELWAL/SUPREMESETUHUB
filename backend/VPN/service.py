"""VPN domain entry point."""
class DomainService:
    domain = "VPN"
    ecosystem_package = "backend.VPN.GLOBAL_ECOSYSTEM.GLOBAL_VPN_ECOSYSTEM"
    def describe(self): return {"domain": self.domain, "ecosystem_package": self.ecosystem_package, "status": "scaffold"}
