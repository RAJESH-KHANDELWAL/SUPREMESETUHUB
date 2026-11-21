"""Canonical read-only Global VPN provider catalogue."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
ECOSYSTEM_ID="GLOBAL-VPN-CORE-ECOSYSTEM"
SOURCE_REGISTRY_REF="backend/vpn/global_ecosystem/global_vpn_ecosystem/registry.py"
PROVIDERS:tuple[dict[str,Any],...]=[
    {
        "provider_id": "wireguard",
        "name": "WireGuard",
        "directory": "wireguard_vpn_core_ecosystem",
        "ecosystem_id": "WIREGUARD-VPN-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "configured": False,
        "live_connection_verified": False,
        "source_service_ref": "backend/vpn/global_ecosystem/global_vpn_ecosystem/wireguard_vpn/service.py",
        "api_transport_verified": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"
    },
    {
        "provider_id": "openvpn",
        "name": "OpenVPN",
        "directory": "openvpn_vpn_core_ecosystem",
        "ecosystem_id": "OPENVPN-VPN-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "configured": False,
        "live_connection_verified": False,
        "source_service_ref": "backend/vpn/global_ecosystem/global_vpn_ecosystem/openvpn_vpn/service.py",
        "api_transport_verified": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"
    },
    {
        "provider_id": "tailscale",
        "name": "Tailscale",
        "directory": "tailscale_vpn_core_ecosystem",
        "ecosystem_id": "TAILSCALE-VPN-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "configured": False,
        "live_connection_verified": False,
        "source_service_ref": "backend/vpn/global_ecosystem/global_vpn_ecosystem/tailscale_vpn/service.py",
        "api_transport_verified": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"
    },
    {
        "provider_id": "protonvpn",
        "name": "Proton VPN",
        "directory": "proton_vpn_core_ecosystem",
        "ecosystem_id": "PROTONVPN-VPN-CORE-ECOSYSTEM",
        "status": "CORE_CATALOG_ONLY",
        "enabled": True,
        "configured": False,
        "live_connection_verified": False,
        "source_service_ref": "backend/vpn/global_ecosystem/global_vpn_ecosystem/proton_vpn/service.py",
        "api_transport_verified": False,
        "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"
    }
]
CAPABILITIES=("VPN_PROVIDER_DISCOVERY","PROTOCOL_CAPABILITY_METADATA","DEVICE_CLIENT_COVERAGE","TUNNEL_AND_MESH_METADATA","ROUTING_AND_DNS_POLICY_METADATA","PRIVACY_AND_SECURITY_METADATA","CONNECTIVITY_HEALTH_METADATA","JURISDICTION_AND_COMPLIANCE_METADATA")
def get_catalog()->dict[str,Any]:
 return {"ecosystem_id":ECOSYSTEM_ID,"name":"GLOBAL VPN CORE ECOSYSTEM","ecosystem_type":"GLOBAL_NETWORK_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","layer":"CORE","status":"CORE_CATALOG_ONLY","enabled":True,"source_service_ref":SOURCE_REGISTRY_REF,"provider_count":len(PROVIDERS),"provider_directory_count":len(PROVIDERS),"providers":deepcopy(list(PROVIDERS)),"capabilities":list(CAPABILITIES),"configured_provider_count":0,"connected_provider_count":0,"live_connection_verified":False,"tunnel_operations_in_core":False,"credential_storage":"EXTERNAL_SECRET_STORE_ONLY"}
def get_provider(provider_id:str)->dict[str,Any]|None:
 needle=provider_id.strip().casefold() if isinstance(provider_id,str) else ""
 item=next((p for p in PROVIDERS if p["provider_id"]==needle or p["directory"]==needle),None)
 return deepcopy(item) if item else None
