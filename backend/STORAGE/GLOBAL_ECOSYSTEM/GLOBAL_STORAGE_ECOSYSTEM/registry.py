"""Metadata catalog for object, file, and cloud storage providers."""
from copy import deepcopy

PROVIDERS = [
    {"provider_id":"google","name":"Google Cloud Storage","storage_type":"object","status":"not_configured"},
    {"provider_id":"aws","name":"Amazon S3","storage_type":"object","status":"not_configured"},
    {"provider_id":"microsoft","name":"Azure Blob Storage","storage_type":"object","status":"not_configured"},
    {"provider_id":"hostinger","name":"Hostinger Storage","storage_type":"web_hosting_storage","status":"not_configured"},
    {"provider_id":"proton","name":"Proton Drive","storage_type":"encrypted_file_storage","status":"not_configured"},
    {"provider_id":"mega","name":"MEGA","storage_type":"cloud_file_storage","status":"not_configured"},
    {"provider_id":"cloudflare","name":"Cloudflare R2","storage_type":"object","status":"not_configured"},
    {"provider_id":"digitalocean","name":"DigitalOcean Spaces","storage_type":"object","status":"not_configured"},
    {"provider_id":"backblaze","name":"Backblaze B2","storage_type":"object","status":"not_configured"},
    {"provider_id":"wasabi","name":"Wasabi Hot Cloud Storage","storage_type":"object","status":"not_configured"},
]

def list_providers():
    return deepcopy(PROVIDERS)

def get_provider(provider_id):
    key = str(provider_id).strip().lower()
    for provider in PROVIDERS:
        if provider["provider_id"] == key:
            return deepcopy(provider)
    raise KeyError(f"Unknown storage provider: {provider_id!r}")
