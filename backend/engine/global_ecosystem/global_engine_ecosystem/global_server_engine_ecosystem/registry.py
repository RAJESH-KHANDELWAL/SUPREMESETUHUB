"""Canonical provider catalog and in-memory SERVER inventory registry."""
from __future__ import annotations
from copy import deepcopy
from threading import RLock

ROOT_ECOSYSTEM_ID = "GLOBAL-ECOSYSTEM"
SERVER_ECOSYSTEM_ID = "GLOBAL-SERVER-ECOSYSTEM"

PROVIDERS = [
    {"provider_id":"hostinger","ecosystem_id":"HOSTINGER-SERVER-ECOSYSTEM","name":"HOSTINGER SERVER ECOSYSTEM","provider_type":"web_hosting","capabilities":["wordpress-hosting","domains","mysql","web-hosting"],"status":"not_configured"},
    {"provider_id":"google","ecosystem_id":"GOOGLE-SERVER-ECOSYSTEM","name":"GOOGLE SERVER ECOSYSTEM","provider_type":"cloud_compute","capabilities":["cloud-run","compute-engine","cloud-deployment"],"status":"not_configured"},
    {"provider_id":"aws","ecosystem_id":"AWS-SERVER-ECOSYSTEM","name":"AWS SERVER ECOSYSTEM","provider_type":"cloud_compute","capabilities":["compute","containers","cloud-deployment"],"status":"not_configured"},
    {"provider_id":"microsoft","ecosystem_id":"MICROSOFT-SERVER-ECOSYSTEM","name":"MICROSOFT SERVER ECOSYSTEM","provider_type":"cloud_compute","capabilities":["azure-virtual-machines","azure-app-service","cloud-deployment"],"status":"not_configured"},
    {"provider_id":"azure","ecosystem_id":"AZURE-SERVER-ECOSYSTEM","name":"AZURE SERVER ECOSYSTEM","provider_type":"cloud_compute","capabilities":["virtual-machines","app-service","cloud-deployment"],"status":"not_configured"},
    {"provider_id":"oracle","ecosystem_id":"ORACLE-SERVER-ECOSYSTEM","name":"ORACLE SERVER ECOSYSTEM","provider_type":"cloud_compute","capabilities":["compute","virtual-machines","cloud-deployment"],"status":"not_configured"},
    {"provider_id":"digitalocean","ecosystem_id":"DIGITALOCEAN-SERVER-ECOSYSTEM","name":"DIGITALOCEAN SERVER ECOSYSTEM","provider_type":"cloud_compute","capabilities":["droplets","app-platform","cloud-deployment"],"status":"not_configured"},
    {"provider_id":"cloudflare","ecosystem_id":"CLOUDFLARE-SERVER-ECOSYSTEM","name":"CLOUDFLARE SERVER ECOSYSTEM","provider_type":"edge_compute","capabilities":["workers","pages","edge-network"],"status":"not_configured"},
    {"provider_id":"abelohost","ecosystem_id":"ABELOHOST-SERVER-ECOSYSTEM","name":"ABELOHOST SERVER ECOSYSTEM","provider_type":"hosting","capabilities":["vps","dedicated-hosting"],"status":"not_configured"},
    {"provider_id":"vicetemple","ecosystem_id":"VICETEMPLE-SERVER-ECOSYSTEM","name":"VICETEMPLE SERVER ECOSYSTEM","provider_type":"specialized_hosting","capabilities":["specialized-hosting"],"status":"not_configured"},
    {"provider_id":"proton","ecosystem_id":"PROTON-STORAGE-ECOSYSTEM","name":"PROTON STORAGE ECOSYSTEM","provider_type":"privacy_storage_service","capabilities":["proton-drive","encrypted-file-storage"],"status":"catalog_only","notes":"Storage provider, not a general-purpose server host."},
    {"provider_id":"mega","ecosystem_id":"MEGA-STORAGE-ECOSYSTEM","name":"MEGA STORAGE ECOSYSTEM","provider_type":"cloud_file_storage","capabilities":["cloud-file-storage","file-sharing"],"status":"catalog_only","notes":"Cloud file storage, not a general-purpose server host."},
]
SERVICE_TYPES = [
    {"service_type_id":"VPN-SERVER","name":"VPN SERVER","category":"networking","capabilities":["encrypted-tunnel","remote-access","site-to-site-vpn"],"status":"catalog_only"},
    {"service_type_id":"VPS-SERVER","name":"VPS SERVER","category":"virtual_compute","capabilities":["virtual-machine","root-or-admin-control","self-managed-services"],"status":"catalog_only"},
    {"service_type_id":"CLOUD-SERVER","name":"CLOUD SERVER","category":"cloud_compute","capabilities":["on-demand-compute","scaling","cloud-networking"],"status":"catalog_only"},
    {"service_type_id":"WEB-SERVER","name":"WEB SERVER","category":"web-serving","capabilities":["http","https","reverse-proxy","static-content"],"status":"catalog_only"},
    {"service_type_id":"CLOUD-WEB-SERVER","name":"CLOUD WEB SERVER","category":"cloud-web-hosting","capabilities":["managed-web-deployment","tls"],"status":"catalog_only"},
    {"service_type_id":"DEDICATED-SERVER","name":"DEDICATED SERVER","category":"bare_metal_compute","capabilities":["dedicated-hardware","root-access"],"status":"catalog_only"},
    {"service_type_id":"EDGE-SERVER","name":"EDGE SERVER","category":"edge_compute","capabilities":["edge-runtime","distributed-compute"],"status":"catalog_only"},
    {"service_type_id":"APPLICATION-SERVER","name":"APPLICATION SERVER","category":"application_runtime","capabilities":["application-runtime","process-management"],"status":"catalog_only"},
    {"service_type_id":"DATABASE-SERVER","name":"DATABASE SERVER","category":"data_infrastructure","capabilities":["database-hosting","database-networking"],"status":"catalog_only"},
]

def _copy(value):
    return deepcopy(value)

def list_providers():
    return [_copy(item) for item in PROVIDERS]

def get_provider(provider_id):
    key = str(provider_id).strip().lower()
    for item in PROVIDERS:
        if item["provider_id"] == key:
            return _copy(item)
    raise KeyError(f"Unknown server provider: {provider_id!r}")

def list_service_types():
    return [_copy(item) for item in SERVICE_TYPES]

def get_service_type(service_type_id):
    key = str(service_type_id).strip().upper().replace("_", "-")
    for item in SERVICE_TYPES:
        if item["service_type_id"] == key:
            return _copy(item)
    raise KeyError(f"Unknown server service type: {service_type_id!r}")

class ServerRegistrationRegistry:
    """Thread-safe, process-local inventory; it never connects to remote hosts."""
    def __init__(self):
        self._servers = {}
        self._lock = RLock()

    def register(self, server):
        row = _copy(server)
        required = ("server_id","server_name","provider_id","server_type","server_role","country","region","environment")
        for field in required:
            if not str(row.get(field, "")).strip():
                raise ValueError(f"{field} is required")
        key = row["server_id"].strip()
        row["server_id"] = key
        row.setdefault("status", "REGISTERED")
        row.setdefault("authorized", False)
        row.setdefault("enabled", True)
        with self._lock:
            if key in self._servers:
                raise ValueError(f"Server already registered: {key}")
            self._servers[key] = row
            return _copy(row)

    def get(self, server_id):
        with self._lock:
            item = self._servers.get(server_id)
            return _copy(item) if item is not None else None

    def list(self):
        with self._lock:
            return [_copy(item) for item in self._servers.values()]

    def update(self, server_id, **changes):
        allowed = {"authorized","enabled","status","endpoint","protocol","region","environment"}
        extra = set(changes) - allowed
        if extra:
            raise ValueError("Unsupported server fields: " + ", ".join(sorted(extra)))
        with self._lock:
            row = self._servers.get(server_id)
            if row is None:
                return None
            self._servers[server_id] = {**row, **changes}
            return _copy(self._servers[server_id])

    def count(self):
        with self._lock:
            return len(self._servers)
