"""STORAGE-owned metadata provider catalog; no live connection is implied."""
from .catalog import get_provider_catalog
def list_providers(): return get_provider_catalog()
def get_provider(provider_id):
    key=provider_id.strip().lower()
    for provider in list_providers():
        if provider["provider_id"]==key: return provider
    raise KeyError(f"Unknown STORAGE provider: {provider_id!r}")
