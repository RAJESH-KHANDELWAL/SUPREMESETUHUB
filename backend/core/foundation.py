from backend.foundation.core.bootstrap import FoundationBootstrap


class CoreFoundation:
    """
    CORE → MAIN BASE FOUNDATION bridge.

    CORE की actual business/management responsibility
    CORE में ही रहेगी।
    """

    NAME = "CORE FOUNDATION BRIDGE"

    def __init__(self):
        self.foundation = FoundationBootstrap()

    def initialize(self):
        return self.foundation.boot()

    def health(self):
        return self.foundation.health()

    def shutdown(self):
        return self.foundation.shutdown()
