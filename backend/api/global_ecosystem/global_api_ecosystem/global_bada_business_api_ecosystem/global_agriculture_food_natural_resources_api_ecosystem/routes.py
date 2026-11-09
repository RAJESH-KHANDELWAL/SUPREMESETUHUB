"""FastAPI routes for the agriculture and food ecosystem."""
from fastapi import APIRouter, HTTPException
from .service import AgricultureFoodNaturalResourcesService

router = APIRouter(prefix="/agriculture-food-natural-resources", tags=["Agriculture, Food & Natural Resources"])
service = AgricultureFoodNaturalResourcesService()

@router.get("/status")
def get_status():
    return service.status().__dict__

@router.get("/domains")
def get_domains():
    return [item.__dict__ for item in service.list_domains()]

@router.get("/domains/{domain_id}")
def get_domain(domain_id: str):
    item = service.get_domain(domain_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Domain not found")
    return item.__dict__
