from backend.engines.base import BaseEngine


class FoundationEngine(BaseEngine):
    """
    FOUNDATION ENGINE

    ENGINE layer में MAIN BASE FOUNDATION को
    expose और control करने वाला engine.

    Actual Foundation implementation:
        backend/foundation/

    यह class Foundation की duplicate implementation
    नहीं बनाती.
    """

    NAME = "FOUNDATION ENGINE"
    VERSION = "1.0.0"

    def __init__(self):
        super().__init__(
            name=self.NAME,
            version=self.VERSION
        )

        self.foundation = None

    def initialize(self, foundation=None):
        """
        Connect the ENGINE layer with
        MAIN BASE FOUNDATION.
        """

        self.foundation = foundation

        self.status = "READY"

        return {
            "engine": self.NAME,
            "version": self.VERSION,
            "status": self.status,
            "foundation_connected": (
                self.foundation is not None
            ),
        }

    def start(self):
        """
        Start Foundation Engine.
        """

        self.status = "RUNNING"

        return {
            "engine": self.NAME,
            "status": self.status,
            "foundation_connected": (
                self.foundation is not None
            ),
        }

    def health(self):
        """
        Return Foundation Engine health.
        """

        return {
            "engine": self.NAME,
            "version": self.VERSION,
            "status": self.status,
            "foundation_connected": (
                self.foundation is not None
            ),
        }

    def stop(self):
        """
        Stop Foundation Engine.
        """

        self.status = "STOPPED"

        return {
            "engine": self.NAME,
            "status": self.status,
        }
