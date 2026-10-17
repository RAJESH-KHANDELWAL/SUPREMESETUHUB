"""Authenticated Google ecosystem registry endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from backend.GOOGLE.GOOGLE_ECOSYSTEM.service import GoogleEcosystemService
from backend.security.dependencies import require_admin

router = APIRouter(
    prefix="/api/v1/google-ecosystem",
    tags=["Google Ecosystem"],
    dependencies=[Depends(require_admin)],
)

service = GoogleEcosystemService()


@router.get("/status")
def google_ecosystem_status():
    """Return configuration and implementation status, not a false live-connect claim."""
    return service.status()


@router.get("/products")
def google_ecosystem_products():
    """List Google products registered under the shared ecosystem."""
    return {
        "success": True,
        "ecosystem": "GOOGLE_ECOSYSTEM",
        "products": service.catalog(),
    }


@router.get("/products/{product_id}")
def google_ecosystem_product(product_id: str):
    """Return integration metadata for one registered Google product."""
    product = service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="GOOGLE_PRODUCT_NOT_FOUND")
    return {"success": True, "product": product}
