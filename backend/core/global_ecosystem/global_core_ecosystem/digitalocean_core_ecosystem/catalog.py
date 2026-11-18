"""Canonical DigitalOcean CORE registry; catalog metadata only."""
from copy import deepcopy
_CATALOG={"provider":"digitalocean","layer":"CORE","status":"INTERFACE_ONLY","live_provider_calls_enabled":False,"api_ecosystem_ref":"backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem","capabilities":{
"cloud":{"package":"digitalocean_cloud_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_cloud_api_ecosystem","status":"CONTRACT_ONLY","live_enabled":False},
"hosting":{"package":"digitalocean_hosting_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_hosting_api_ecosystem","status":"CONTRACT_ONLY","live_enabled":False},
"server":{"package":"digitalocean_server_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_server_api_ecosystem","status":"CONTRACT_ONLY","live_enabled":False},
"storage":{"package":"digitalocean_storage_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_storage_api_ecosystem","status":"CONTRACT_ONLY","live_enabled":False},
"vps":{"package":"digitalocean_vps_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/digitalocean_api_ecosystem/digitalocean_vps_api_ecosystem","status":"CONTRACT_ONLY","live_enabled":False}
}}
def get_catalog(): return deepcopy(_CATALOG)
def list_capabilities(): return deepcopy(_CATALOG["capabilities"])
