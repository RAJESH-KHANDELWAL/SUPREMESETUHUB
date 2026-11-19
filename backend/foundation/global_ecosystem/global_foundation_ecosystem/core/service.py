from backend.foundation.core.foundation import MainBaseFoundation


class FoundationService:
    """
    Foundation service entry point.

    API, CORE and ENGINE can use this service instead of
    creating separate foundation implementations.
    """

    def __init__(self):
        self.foundation = MainBaseFoundation()

    def initialize(self):
        return self.foundation.initialize()

    def health(self):
        return self.foundation.health()

    def shutdown(self):
        return self.foundation.shutdown()
