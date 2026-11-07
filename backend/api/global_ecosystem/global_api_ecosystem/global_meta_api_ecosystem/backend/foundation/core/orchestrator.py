from backend.foundation.core.integrity import FoundationIntegrity
from backend.foundation.core.service import FoundationService


class FoundationOrchestrator:
    """
    MAIN BASE FOUNDATION orchestrator.

    Foundation के अलग-अलग core components को
    एक central flow में coordinate करता है।
    """

    NAME = "FOUNDATION ORCHESTRATOR"

    def __init__(self):
        self.service = FoundationService()
        self.integrity = FoundationIntegrity()

    def initialize(self):
        foundation = self.service.initialize()
        integrity = self.integrity.verify()

        return {
            "orchestrator": self.NAME,
            "foundation": foundation,
            "integrity": integrity,
            "status": "RUNNING",
        }

    def health(self):
        integrity = self.integrity.verify()

        return {
            "orchestrator": self.NAME,
            "foundation": self.service.health(),
            "integrity": integrity,
            "status": "HEALTHY" if integrity["verified"] else "UNHEALTHY",
        }

    def shutdown(self):
        foundation = self.service.shutdown()

        return {
            "orchestrator": self.NAME,
            "foundation": foundation,
            "status": "STOPPED",
        }
