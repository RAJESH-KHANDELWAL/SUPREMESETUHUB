"""MICROSOFT Storage Core provider package."""
PROVIDER = "microsoft"
ECOSYSTEM_ID = "MICROSOFT-STORAGE-CORE-ECOSYSTEM"

from .service import MicrosoftStorageCoreService

__all__ = ["PROVIDER", "ECOSYSTEM_ID", "MicrosoftStorageCoreService"]
