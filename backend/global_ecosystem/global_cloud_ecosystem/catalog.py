"""Bharat-to-global cloud provider catalog. Metadata is not proof of live access."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
_ROWS = (
("aws","Amazon Web Services","global","compute,object_storage,databases,networking,identity"),
("google_cloud","Google Cloud","global","compute,object_storage,databases,analytics,ai_infrastructure"),
("microsoft_azure","Microsoft Azure","global","compute,storage,identity,databases,networking"),
("oracle_cloud","Oracle Cloud Infrastructure","global","compute,object_storage,databases,networking"),
("ibm_cloud","IBM Cloud","global","enterprise_compute,storage,ai,hybrid_cloud"),
("alibaba_cloud","Alibaba Cloud","china","compute,object_storage,databases,networking"),
("tencent_cloud","Tencent Cloud","china","compute,storage,media,databases"),
("huawei_cloud","Huawei Cloud","china","compute,storage,databases,ai_infrastructure"),
("digitalocean","DigitalOcean","global","virtual_machines,managed_databases,object_storage"),
("cloudflare","Cloudflare","global","edge_compute,cdn,dns,object_storage,security"),
("vercel","Vercel","global","frontend_deployment,serverless,edge_hosting"),
("netlify","Netlify","global","web_deployment,functions,edge_hosting"),
("render","Render","global","application_hosting,background_workers,databases"),
("hetzner","Hetzner","europe","cloud_servers,volumes,networking"),
("linode","Akamai Cloud (Linode)","global","compute,object_storage,networking"),
("vultr","Vultr","global","cloud_compute,storage,networking"),
("ovhcloud","OVHcloud","europe","compute,object_storage,private_cloud,public_cloud"),
("scaleway","Scaleway","europe","compute,object_storage,kubernetes,databases"),
("proton_drive","Proton Drive","switzerland","encrypted_file_storage"),
("dropbox","Dropbox","global","file_sync,storage,sharing,collaboration"),
("box","Box","global","enterprise_content_cloud,governance"),
("onedrive","Microsoft OneDrive","global","personal_storage,enterprise_storage"),
("google_drive","Google Drive","global","personal_storage,enterprise_storage"),
("mega","MEGA","global","encrypted_storage,file_transfer"),
("icloud","Apple iCloud","global","device_backup,sync,cloud_storage"),
("backblaze","Backblaze","global","object_storage,backup"),
("wasabi","Wasabi","global","object_storage"),
("idrive","IDrive","global","cloud_backup,storage"),
("pcloud","pCloud","switzerland","consumer_storage,business_storage"),
("jio_cloud","JioCloud","india","consumer_storage,backup"),
("digiboxx","DigiBoxx","india","cloud_storage,file_sharing"),
("tata_communications_cloud","Tata Communications","india","enterprise_cloud,network_services"),
("nxtgen","NxtGen","india","data_centres,cloud_infrastructure"),
("esds","ESDS","india","managed_cloud,data_centres"),
("ctrls","CtrlS","india","data_centres,managed_cloud"),
("yotta","Yotta","india","hyperscale_data_centres,cloud_services"),
("e2e_networks","E2E Networks","india","gpu_compute,cloud_compute"),
("oracle_cloud_india","Oracle Cloud India","india","regional_compute,data_services"),
("aws_india","AWS India Regions","india","regional_cloud_infrastructure"),
("azure_india","Microsoft Azure India Regions","india","regional_cloud_infrastructure"),
("gcp_india","Google Cloud India Regions","india","regional_cloud_infrastructure"),
)
_CATALOG: tuple[dict[str, Any], ...] = tuple({"id":r[0],"name":r[1],"origin":r[2],"capabilities":tuple(r[3].split(",")),"integration_status":"catalog_only","live_connection_verified":False} for r in _ROWS)
def list_cloud_providers(*,origin:str|None=None)->tuple[dict[str,Any],...]:
    rows=_CATALOG if origin is None else tuple(x for x in _CATALOG if x["origin"]==origin)
    return tuple(deepcopy(x) for x in rows)
def get_cloud_provider(provider_id:str)->dict[str,Any]|None:
    key=str(provider_id or "").strip().lower()
    for item in _CATALOG:
        if item["id"]==key:return deepcopy(item)
    return None
def validate_cloud_catalog()->tuple[str,...]:
    errors=[];ids=[x["id"] for x in _CATALOG]
    if len(ids)!=len(set(ids)):errors.append("duplicate provider ids")
    for item in _CATALOG:
        if not item["name"] or not item["capabilities"]:errors.append(f"{item['id']} missing metadata")
        if item["integration_status"]=="live_verified" and item["live_connection_verified"] is not True:errors.append(f"{item['id']} lacks live verification")
    return tuple(errors)
__all__=["list_cloud_providers","get_cloud_provider","validate_cloud_catalog"]
