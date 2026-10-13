"""Catalog provider ecosystems and common server service types.

Metadata only: this module does not provision servers, establish VPNs, or connect
to cloud providers. Status stays unconfigured until an authorized integration is
implemented and verified end to end.
"""

ROOT_ECOSYSTEM_ID = "GLOBAL-ECOSYSTEM"
SERVER_ECOSYSTEM_ID = "GLOBAL-SERVER-ECOSYSTEM"

PROVIDERS = [
    {"provider_id": "hostinger", "ecosystem_id": "HOSTINGER-SERVER-ECOSYSTEM", "name": "HOSTINGER SERVER ECOSYSTEM", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "provider_type": "web_hosting", "capabilities": ["wordpress-hosting", "domains", "mysql", "web-hosting"], "status": "not_configured"},
    {"provider_id": "google", "ecosystem_id": "GOOGLE-SERVER-ECOSYSTEM", "name": "GOOGLE SERVER ECOSYSTEM", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "provider_type": "cloud_compute", "capabilities": ["cloud-run", "compute-engine", "cloud-deployment"], "status": "not_configured"},
    {"provider_id": "aws", "ecosystem_id": "AWS-SERVER-ECOSYSTEM", "name": "AWS SERVER ECOSYSTEM", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "provider_type": "cloud_compute", "capabilities": ["compute", "containers", "cloud-deployment"], "status": "not_configured"},
    {"provider_id": "microsoft", "ecosystem_id": "MICROSOFT-SERVER-ECOSYSTEM", "name": "MICROSOFT SERVER ECOSYSTEM", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "provider_type": "cloud_compute", "capabilities": ["azure-virtual-machines", "azure-app-service", "cloud-deployment"], "status": "not_configured"},
    {"provider_id": "oracle", "ecosystem_id": "ORACLE-SERVER-ECOSYSTEM", "name": "ORACLE SERVER ECOSYSTEM", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "provider_type": "cloud_compute", "capabilities": ["compute", "virtual-machines", "cloud-deployment"], "status": "not_configured"},
    {"provider_id": "digitalocean", "ecosystem_id": "DIGITALOCEAN-SERVER-ECOSYSTEM", "name": "DIGITALOCEAN SERVER ECOSYSTEM", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "provider_type": "cloud_compute", "capabilities": ["droplets", "app-platform", "cloud-deployment"], "status": "not_configured"},
    {"provider_id": "proton", "ecosystem_id": "PROTON-STORAGE-ECOSYSTEM", "name": "PROTON STORAGE ECOSYSTEM", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "provider_type": "privacy_storage_service", "capabilities": ["proton-drive", "encrypted-file-storage"], "status": "catalog_only", "notes": "Storage/privacy service; not a general-purpose application server provider."},
    {"provider_id": "mega", "ecosystem_id": "MEGA-STORAGE-ECOSYSTEM", "name": "MEGA STORAGE ECOSYSTEM", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "provider_type": "cloud_file_storage", "capabilities": ["cloud-file-storage", "file-sharing"], "status": "catalog_only", "notes": "Cloud file-storage service; not a general-purpose application server provider."},
]

# Service types describe what can run on a server; they are not hosting vendors.
SERVICE_TYPES = [
    {"service_type_id": "VPN-SERVER", "name": "VPN SERVER", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "category": "networking", "capabilities": ["encrypted-tunnel", "remote-access", "site-to-site-vpn"], "status": "catalog_only"},
    {"service_type_id": "VPS-SERVER", "name": "VPS SERVER", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "category": "virtual_compute", "capabilities": ["virtual-machine", "root-or-admin-control", "self-managed-services"], "status": "catalog_only"},
    {"service_type_id": "CLOUD-SERVER", "name": "CLOUD SERVER", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "category": "cloud_compute", "capabilities": ["on-demand-compute", "scaling", "cloud-networking"], "status": "catalog_only"},
    {"service_type_id": "WEB-SERVER", "name": "WEB SERVER", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "category": "web-serving", "capabilities": ["http", "https", "reverse-proxy", "static-content"], "status": "catalog_only"},
    {"service_type_id": "CLOUD-WEB-SERVER", "name": "CLOUD WEB SERVER", "parent_ecosystem_id": SERVER_ECOSYSTEM_ID, "category": "cloud-web-hosting", "capabilities": ["managed-web-deployment", "tls", "autoscaling-where-supported"], "status": "catalog_only"},
]


def _copy_record(record):
    """Return a record with a copied capabilities list."""
    return {**record, "capabilities": list(record["capabilities"])}


def list_providers():
    """Return independent provider records for catalog/API consumers."""
    return [_copy_record(provider) for provider in PROVIDERS]


def get_provider(provider_id):
    """Return one provider record by its stable identifier."""
    normalized_id = provider_id.strip().lower()
    for provider in PROVIDERS:
        if provider["provider_id"] == normalized_id:
            return _copy_record(provider)
    raise KeyError(f"Unknown server provider: {provider_id!r}")


def list_service_types():
    """Return independent records for supported server service categories."""
    return [_copy_record(service_type) for service_type in SERVICE_TYPES]


def get_service_type(service_type_id):
    """Return one service type by its stable identifier."""
    normalized_id = service_type_id.strip().upper().replace("_", "-")
    for service_type in SERVICE_TYPES:
        if service_type["service_type_id"] == normalized_id:
            return _copy_record(service_type)
    raise KeyError(f"Unknown server service type: {service_type_id!r}")
