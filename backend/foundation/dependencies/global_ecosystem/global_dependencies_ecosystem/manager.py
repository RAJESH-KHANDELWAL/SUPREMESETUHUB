"""Manager for Global Dependencies Ecosystem."""

class GlobalDependenciesEcosystemManager:
    NAME = "GLOBAL_DEPENDENCIES_ECOSYSTEM"
    STATUS = "READY"

    def status(self):
        return {"ecosystem": self.NAME, "status": self.STATUS}
