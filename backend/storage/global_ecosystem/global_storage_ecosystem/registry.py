"""Metadata-only catalog for GLOBAL STORAGE ECOSYSTEM providers."""
from copy import deepcopy

PROVIDERS = [
    {"provider_id": "aws_storage", "name": "Amazon S3", "provider": "AWS", "capabilities": ["object-storage", "multipart-upload"], "status": "not_configured"},
    {"provider_id": "google_storage", "name": "Google Cloud Storage", "provider": "GOOGLE", "capabilities": ["object-storage", "versioning"], "status": "not_configured"},
    {"provider_id": "hostinger_storage", "name": "Hostinger Storage", "provider": "HOSTINGER", "capabilities": ["hosting-file-storage"], "status": "not_configured"},
    {"provider_id": "mega_storage", "name": "MEGA Storage", "provider": "MEGA", "capabilities": ["encrypted-cloud-storage", "file-sync"], "status": "not_configured"},
    {"provider_id": "microsoft_storage", "name": "Azure Blob Storage", "provider": "MICROSOFT", "capabilities": ["object-storage", "lifecycle-management"], "status": "not_configured"},
    {"provider_id": "proton_storage", "name": "Proton Drive", "provider": "PROTON", "capabilities": ["privacy-aware-file-storage", "file-sharing"], "status": "not_configured"},
]

def list_providers():
    return deepcopy(PROVIDERS)

def get_provider(provider_id):
    normalized = provider_id.strip().lower()
    for provider in PROVIDERS:
        if provider["provider_id"] == normalized:
            return deepcopy(provider)
    raise KeyError(f"Unknown STORAGE provider: {provider_id!r}")
