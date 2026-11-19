"""Manager for Global File Manager Ecosystem."""

class GlobalFileManagerEcosystemManager:
    NAME = "GLOBAL_FILE_MANAGER_ECOSYSTEM"
    STATUS = "READY"

    def status(self):
        return {"ecosystem": self.NAME, "status": self.STATUS}
