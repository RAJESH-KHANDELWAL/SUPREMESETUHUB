"""Owner-authenticated API for the Bada Business integration catalog."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from backend.integration.connector.bada_business import bada_business_connector

router = APIRouter(
    prefix="/api/v1/bada-business-integration",
    tags=["Bada Business Integration"],
)


@router.get("/status")
def bada_business_integration_status():
    """Report catalog readiness without implying a live provider connection."""
    return bada_business_connector.status()


@router.get("/catalog")
def bada_business_integration_catalog():
    """Return canonical links and program metadata."""
    return bada_business_connector.catalog()


@router.get("/links")
def bada_business_integration_links():
    return {
        "success": True,
        "count": len(bada_business_connector.links()),
        "links": bada_business_connector.links(),
    }


@router.get("/links/{link_id}")
def bada_business_integration_link(link_id: str):
    link = bada_business_connector.link(link_id)
    if link is None:
        raise HTTPException(status_code=404, detail="BADA_BUSINESS_LINK_NOT_FOUND")
    return {"success": True, "link": link}


@router.get("/programs")
def bada_business_integration_programs():
    programs = bada_business_connector.programs()
    return {"success": True, "count": len(programs), "programs": programs}


@router.get("/programs/{program_id}")
def bada_business_integration_program(program_id: str):
    program = bada_business_connector.program(program_id)
    if program is None:
        raise HTTPException(status_code=404, detail="BADA_BUSINESS_PROGRAM_NOT_FOUND")
    return {"success": True, "program": program}


__all__ = ["router"]
