"""
MAIN BASE FOUNDATION
Infrastructure Control Plane API

Public API facade for infrastructure inventory.
"""

from fastapi import APIRouter

from backend.infrastructure.domains.controller import DomainController
from backend.infrastructure.hosting.controller import HostingController
from backend.infrastructure.servers.controller import ServerController
from backend.infrastructure.ipam.controller import IPAMController
from backend.infrastructure.network.controller import NetworkController
from backend.infrastructure.dns.controller import DNSController
from backend.infrastructure.hostinger_catalog import (
    hostinger_catalog,
    hostinger_readiness,
)
from backend.infrastructure.hostinger_api import (
    connection_status as hostinger_connection_status,
    list_vps_instances as hostinger_list_vps_instances,
    list_websites as hostinger_list_websites,
    HostingerAPIError,
)


router = APIRouter(
    prefix="/infrastructure",
    tags=["Infrastructure Control Plane"],
)


domain_controller = DomainController()
hosting_controller = HostingController()
server_controller = ServerController()
ipam_controller = IPAMController()
network_controller = NetworkController()
dns_controller = DNSController()


def _safe_list(name, callback):
    try:
        data = callback()
        return {
            "status": "LIVE",
            "count": len(data),
            "data": data,
        }
    except Exception as exc:
        return {
            "status": "ERROR",
            "count": 0,
            "data": [],
            "error": f"{type(exc).__name__}: {exc}",
        }


@router.get("/")
def infrastructure_status():
    return {
        "project": "MAIN BASE FOUNDATION",
        "system": "INFRASTRUCTURE CONTROL PLANE",
        "status": "RUNNING",
        "modules": {
            "domains": "READY",
            "hosting": "READY",
            "servers": "READY",
            "ipam": "READY",
            "network": "READY",
            "dns": "READY",
        },
    }


@router.get("/providers/hostinger/catalog")
def list_hostinger_catalog():
    """List Hostinger service categories; this does not claim live connectivity."""
    return hostinger_catalog()


@router.get("/providers/hostinger/readiness")
def hostinger_provider_readiness():
    """Return safe configuration readiness without exposing credentials."""
    return hostinger_readiness()


@router.get("/providers/hostinger/connection")
def hostinger_live_connection_status():
    """Test the Hostinger token using a read-only website inventory request."""
    return hostinger_connection_status()


@router.get("/providers/hostinger/websites")
def hostinger_websites(page: int = 1):
    """Read websites from the connected Hostinger account."""
    if page < 1:
        from fastapi import HTTPException
        raise HTTPException(status_code=422, detail="PAGE_MUST_BE_POSITIVE")
    try:
        return hostinger_list_websites(page=page)
    except HostingerAPIError as exc:
        from fastapi import HTTPException
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/providers/hostinger/vps")
def hostinger_vps_instances(page: int = 1):
    """Read VPS instances from the connected Hostinger account."""
    if page < 1:
        from fastapi import HTTPException
        raise HTTPException(status_code=422, detail="PAGE_MUST_BE_POSITIVE")
    try:
        return hostinger_list_vps_instances(page=page)
    except HostingerAPIError as exc:
        from fastapi import HTTPException
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get("/domains")
def list_domains():
    return domain_controller.list()


@router.get("/hosting")
def list_hosting():
    return hosting_controller.list()


@router.get("/servers")
def list_servers():
    return server_controller.list()


@router.get("/ipam")
def list_ip_addresses():
    return ipam_controller.list()


@router.get("/network")
def list_networks():
    return network_controller.list()


@router.get("/dns/zones")
def list_dns_zones():
    return dns_controller.list_zones()


@router.get("/dns/records")
def list_dns_records():
    return dns_controller.list_records()


@router.get("/summary")
def infrastructure_summary():

    modules = {
        "domains": _safe_list(
            "domains",
            domain_controller.list,
        ),
        "hosting": _safe_list(
            "hosting",
            hosting_controller.list,
        ),
        "servers": _safe_list(
            "servers",
            server_controller.list,
        ),
        "ip_addresses": _safe_list(
            "ip_addresses",
            ipam_controller.list,
        ),
        "networks": _safe_list(
            "networks",
            network_controller.list,
        ),
        "dns_zones": _safe_list(
            "dns_zones",
            dns_controller.list_zones,
        ),
        "dns_records": _safe_list(
            "dns_records",
            dns_controller.list_records,
        ),
    }

    live_modules = [
        name
        for name, result in modules.items()
        if result["status"] == "LIVE"
    ]

    error_modules = [
        name
        for name, result in modules.items()
        if result["status"] == "ERROR"
    ]

    overall_status = (
        "LIVE"
        if not error_modules
        else "PARTIAL_ERROR"
    )

    return {
        "project": "MAIN BASE FOUNDATION",
        "system": "INFRASTRUCTURE CONTROL PLANE",
        "status": overall_status,
        "total_modules": len(modules),
        "live_modules": len(live_modules),
        "error_modules": len(error_modules),
        "counts": {
            name: result["count"]
            for name, result in modules.items()
        },
        "modules": modules,
    }
