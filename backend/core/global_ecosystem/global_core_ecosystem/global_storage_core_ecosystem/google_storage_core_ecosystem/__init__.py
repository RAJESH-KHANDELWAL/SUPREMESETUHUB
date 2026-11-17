"""GOOGLE Storage Core provider package."""
PROVIDER = "google"
ECOSYSTEM_ID = "GOOGLE-STORAGE-CORE-ECOSYSTEM"

from .service import GoogleStorageCoreService

__all__ = ["PROVIDER", "ECOSYSTEM_ID", "GoogleStorageCoreService"]
