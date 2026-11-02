from backend.foundation.core.bootstrap import FoundationBootstrap


class FoundationEntryPoint:
    """
    MAIN BASE FOUNDATION entry point.

    Backend इसी entry point के माध्यम से
    Foundation को initialize कर सकता है।
    """

    NAME = "FOUNDATION ENTRY POINT"

    def __init__(self):
        self.bootstrap = FoundationBootstrap()

    def start(self):
        return self.bootstrap.boot()

    def health(self):
        return self.bootstrap.health()

    def stop(self):
        return self.bootstrap.shutdown()
