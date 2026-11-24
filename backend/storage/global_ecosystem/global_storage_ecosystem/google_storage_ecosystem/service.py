"""Public service entry point for the Google storage category catalog."""
from .ecosystem_service import EcosystemService


class GoogleStorageEcosystem(EcosystemService):
    """Root catalog service; category adapters live in their own packages."""
    pass
