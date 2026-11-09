from backend.identity.service import IdentityService


class FoundationIdentityManager:
    """
    Foundation-level identity manager.

    Existing backend IdentityService को reuse करता है।
    यह दूसरा Identity system create नहीं करता।
    """

    def __init__(self):
        self.identity = IdentityService()

    def initialize(self):
        identity = self.identity.initialize()

        return {
            "component": "FOUNDATION IDENTITY",
            "identity": identity,
            "status": "READY",
        }

    def get_identity(self):
        identity = self.identity

        return {
            "master_id": getattr(identity, "master_id", None),
            "full_name": getattr(identity, "full_name", None),
            "username": getattr(identity, "primary_username", None),
            "status": getattr(identity, "status", None),
        }
