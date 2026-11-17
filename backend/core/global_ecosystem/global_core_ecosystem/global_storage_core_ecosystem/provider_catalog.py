"""Canonical provider-neutral storage provider catalog."""
from __future__ import annotations

from .contracts import Readiness, StorageProvider

PROVIDERS: tuple[StorageProvider, ...] = (
    StorageProvider("google", "Google Cloud Storage", "OBJECT_STORAGE",
                    ("OBJECT_STORAGE", "ARCHIVE", "LIFECYCLE", "REGIONAL_STORAGE")),
    StorageProvider("aws", "Amazon Web Services", "CLOUD_STORAGE",
                    ("OBJECT_STORAGE", "BLOCK_STORAGE", "FILE_STORAGE", "ARCHIVE", "LIFECYCLE")),
    StorageProvider("microsoft", "Microsoft Azure Storage", "CLOUD_STORAGE",
                    ("OBJECT_STORAGE", "FILE_STORAGE", "BLOCK_STORAGE", "ARCHIVE", "LIFECYCLE")),
    StorageProvider("apple", "Apple Storage Services", "CONSUMER_CLOUD_STORAGE",
                    ("FILE_SYNC", "DEVICE_BACKUP")),
    StorageProvider("digitalocean", "DigitalOcean Spaces", "OBJECT_STORAGE",
                    ("OBJECT_STORAGE", "CDN_INTEGRATION")),
)

PROVIDER_INDEX = {provider.provider_id: provider for provider in PROVIDERS}


def list_providers(*, include_disabled: bool = False) -> tuple[StorageProvider, ...]:
    """Return catalog metadata; no provider discovery or network request occurs."""
    if include_disabled:
        return PROVIDERS
    return tuple(p for p in PROVIDERS if p.readiness is not Readiness.DISABLED)


def get_provider(provider_id: str) -> StorageProvider | None:
    return PROVIDER_INDEX.get(provider_id.strip().lower())


__all__ = ["PROVIDERS", "PROVIDER_INDEX", "list_providers", "get_provider"]
