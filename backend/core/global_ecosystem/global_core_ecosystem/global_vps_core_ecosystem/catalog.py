"""Canonical Global VPS provider catalogue."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
ECOSYSTEM_ID="GLOBAL-VPS-CORE-ECOSYSTEM"
API_CATALOG_REF="backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem"
PROVIDERS: tuple[dict[str,Any],...]=[
    {
        "provider_id": "aws",
        "name": "AWS",
        "directory": "aws_vps_core_ecosystem",
        "ecosystem_id": "AWS-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "google",
        "name": "Google Cloud",
        "directory": "google_vps_core_ecosystem",
        "ecosystem_id": "GOOGLE-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "microsoft",
        "name": "Microsoft Azure",
        "directory": "microsoft_vps_core_ecosystem",
        "ecosystem_id": "MICROSOFT-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "oracle",
        "name": "Oracle Cloud Infrastructure",
        "directory": "oracle_vps_core_ecosystem",
        "ecosystem_id": "ORACLE-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "digitalocean",
        "name": "DigitalOcean",
        "directory": "digitalocean_vps_core_ecosystem",
        "ecosystem_id": "DIGITALOCEAN-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "alibaba_cloud",
        "name": "Alibaba Cloud",
        "directory": "alibaba_cloud_vps_core_ecosystem",
        "ecosystem_id": "ALIBABA-CLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "tencent_cloud",
        "name": "Tencent Cloud",
        "directory": "tencent_cloud_vps_core_ecosystem",
        "ecosystem_id": "TENCENT-CLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "huawei_cloud",
        "name": "Huawei Cloud",
        "directory": "huawei_cloud_vps_core_ecosystem",
        "ecosystem_id": "HUAWEI-CLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "rackspace",
        "name": "Rackspace",
        "directory": "rackspace_vps_core_ecosystem",
        "ecosystem_id": "RACKSPACE-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "scaleway",
        "name": "Scaleway",
        "directory": "scaleway_vps_core_ecosystem",
        "ecosystem_id": "SCALEWAY-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "ovhcloud",
        "name": "OVHcloud",
        "directory": "ovhcloud_vps_core_ecosystem",
        "ecosystem_id": "OVHCLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "hetzner_cloud",
        "name": "Hetzner Cloud",
        "directory": "hetzner_cloud_vps_core_ecosystem",
        "ecosystem_id": "HETZNER-CLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "vultr",
        "name": "Vultr",
        "directory": "vultr_vps_core_ecosystem",
        "ecosystem_id": "VULTR-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "ibm",
        "name": "IBM Cloud",
        "directory": "ibm_vps_core_ecosystem",
        "ecosystem_id": "IBM-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "cloudflare",
        "name": "Cloudflare",
        "directory": "cloudflare_vps_core_ecosystem",
        "ecosystem_id": "CLOUDFLARE-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "nvidia",
        "name": "NVIDIA",
        "directory": "nvidia_vps_core_ecosystem",
        "ecosystem_id": "NVIDIA-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "jd_cloud",
        "name": "JD Cloud",
        "directory": "jd_cloud_vps_core_ecosystem",
        "ecosystem_id": "JD-CLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "kingsoft_cloud",
        "name": "Kingsoft Cloud",
        "directory": "kingsoft_cloud_vps_core_ecosystem",
        "ecosystem_id": "KINGSOFT-CLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "baidu_cloud",
        "name": "Baidu AI Cloud",
        "directory": "baidu_cloud_vps_core_ecosystem",
        "ecosystem_id": "BAIDU-CLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    },
    {
        "provider_id": "china_telecom_cloud",
        "name": "China Telecom Cloud",
        "directory": "china_telecom_cloud_vps_core_ecosystem",
        "ecosystem_id": "CHINA-TELECOM-CLOUD-VPS-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "connected": False,
        "live_connection_verified": False,
        "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/global_vps_api_ecosystem",
        "provider_api_adapter_verified": False
    }
]
CAPABILITIES=("PROVIDER_DISCOVERY","VPS_INSTANCE_METADATA","REGION_AND_IMAGE_METADATA","COMPUTE_CAPACITY_METADATA","NETWORK_AND_IP_METADATA","SECURITY_POLICY_METADATA","VOLUME_AND_SNAPSHOT_METADATA","MONITORING_AND_USAGE_METADATA","BILLING_AND_QUOTA_BOUNDARIES","LIFECYCLE_INTENT_VALIDATION")
def get_catalog()->dict[str,Any]:
 return {"ecosystem_id":ECOSYSTEM_ID,"name":"GLOBAL VPS CORE ECOSYSTEM","ecosystem_type":"GLOBAL_PROVIDER_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","layer":"CORE","status":"CORE_CATALOG_ONLY","enabled":True,"api_catalog_ref":API_CATALOG_REF,"provider_count":len(PROVIDERS),"provider_directory_count":len(PROVIDERS),"providers":deepcopy(list(PROVIDERS)),"capabilities":list(CAPABILITIES),"connected_provider_count":0,"live_connection_verified":False,"api_transport_in_core":False,"credential_storage":"EXTERNAL_SECRET_STORE_ONLY"}
def get_provider(provider_id:str)->dict[str,Any]|None:
 needle=provider_id.strip().casefold() if isinstance(provider_id,str) else ""
 item=next((p for p in PROVIDERS if p["provider_id"]==needle or p["directory"]==needle),None)
 return deepcopy(item) if item else None
