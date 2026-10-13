"""Provider registry for GLOBAL ECOSYSTEM -> GLOBAL SERVER ECOSYSTEM.

This is a metadata catalog only. It does not provision or connect to providers.
Provider status remains not_configured until an authorized integration is implemented
and verified end to end.
"""

ROOT_ECOSYSTEM_ID = "GLOBAL-ECOSYSTEM"
SERVER_ECOSYSTEM_ID = "GLOBAL-SERVER-ECOSYSTEM"

PROVIDERS = [
    {
        "provider_id": "hostinger",
        "ecosystem_id": "HOSTINGER-SERVER-ECOSYSTEM",
        "name": "HOSTINGER SERVER ECOSYSTEM",
        "parent_ecosystem_id": SERVER_ECOSYSTEM_ID,
        "provider_type": "web_hosting",
        "capabilities": ["wordpress-hosting", "domains", "mysql", "web-hosting"],
        "status": "not_configured",
    },
    {
        "provider_id": "google",
        "ecosystem_id": "GOOGLE-SERVER-ECOSYSTEM",
        "name": "GOOGLE SERVER ECOSYSTEM",
        "parent_ecosystem_id": SERVER_ECOSYSTEM_ID,
        "provider_type": "cloud_compute",
        "capabilities": ["cloud-run", "compute-engine", "cloud-deployment"],
        "status": "not_configured",
    },
    {
        "provider_id": "aws",
        "ecosystem_id": "AWS-SERVER-ECOSYSTEM",
        "name": "AWS SERVER ECOSYSTEM",
        "parent_ecosystem_id": SERVER_ECOSYSTEM_ID,
        "provider_type": "cloud_compute",
        "capabilities": ["compute", "containers", "cloud-deployment"],
        "status": "not_configured",
    },
    {
        "provider_id": "microsoft",
        "ecosystem_id": "MICROSOFT-SERVER-ECOSYSTEM",
        "name": "MICROSOFT SERVER ECOSYSTEM",
        "parent_ecosystem_id": SERVER_ECOSYSTEM_ID,
        "provider_type": "cloud_compute",
        "capabilities": ["azure-virtual-machines", "azure-app-service", "cloud-deployment"],
        "status": "not_configured",
    },
    {
        "provider_id": "oracle",
        "ecosystem_id": "ORACLE-SERVER-ECOSYSTEM",
        "name": "ORACLE SERVER ECOSYSTEM",
        "parent_ecosystem_id": SERVER_ECOSYSTEM_ID,
        "provider_type": "cloud_compute",
        "capabilities": ["compute", "virtual-machines", "cloud-deployment"],
        "status": "not_configured",
    },
    {
        "provider_id": "digitalocean",
        "ecosystem_id": "DIGITALOCEAN-SERVER-ECOSYSTEM",
        "name": "DIGITALOCEAN SERVER ECOSYSTEM",
        "parent_ecosystem_id": SERVER_ECOSYSTEM_ID,
        "provider_type": "cloud_compute",
        "capabilities": ["droplets", "app-platform", "cloud-deployment"],
        "status": "not_configured",
    },
    {
        "provider_id": "proton",
        "ecosystem_id": "PROTON-STORAGE-ECOSYSTEM",
        "name": "PROTON STORAGE ECOSYSTEM",
        "parent_ecosystem_id": SERVER_ECOSYSTEM_ID,
        "provider_type": "privacy_storage_service",
        "capabilities": ["proton-drive", "encrypted-file-storage"],
        "status": "catalog_only",
        "notes": "Storage/privacy service; not a general-purpose application server provider.",
    },
    {
        "provider_id": "mega",
        "ecosystem_id": "MEGA-STORAGE-ECOSYSTEM",
        "name": "MEGA STORAGE ECOSYSTEM",
        "parent_ecosystem_id": SERVER_ECOSYSTEM_ID,
        "provider_type": "cloud_file_storage",
        "capabilities": ["cloud-file-storage", "file-sharing"],
        "status": "catalog_only",
        "notes": "Cloud file-storage service; not a general-purpose application server provider.",
    },
]


def list_providers():
    """Return independent provider records for catalog/API consumers."""
    return [
        {**provider, "capabilities": list(provider["capabilities"])}
        for provider in PROVIDERS
    ]


def get_provider(provider_id):
    """Return one provider record by its stable identifier."""
    normalized_id = provider_id.strip().lower()
    for provider in PROVIDERS:
        if provider["provider_id"] == normalized_id:
            return {**provider, "capabilities": list(provider["capabilities"])}
    raise KeyError(f"Unknown server provider: {provider_id!r}")
