from backend.foundation.core.bootstrap import FoundationBootstrap


class APIFoundation:
    """
    API → MAIN BASE FOUNDATION bridge.

    API की actual implementation अलग रहेगी।
    यह class सिर्फ Foundation access provide करती है।
    """

    NAME = "API FOUNDATION BRIDGE"

    def __init__(self):
        self.foundation = FoundationBootstrap()

    def initialize(self):
        return self.foundation.boot()

    def health(self):
        return self.foundation.health()

    def shutdown(self):
        return self.foundation.shutdown()
