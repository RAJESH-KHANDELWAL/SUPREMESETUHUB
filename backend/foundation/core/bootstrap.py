from backend.foundation.core.service import FoundationService


class FoundationBootstrap:
    """
    Bootstrap entry point for MAIN BASE FOUNDATION.
    """

    def __init__(self):
        self.service = FoundationService()

    def boot(self):
        return self.service.initialize()

    def health(self):
        return self.service.health()

    def shutdown(self):
        return self.service.shutdown()
