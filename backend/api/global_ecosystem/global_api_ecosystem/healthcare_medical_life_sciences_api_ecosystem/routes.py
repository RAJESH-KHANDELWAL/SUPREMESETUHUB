"""FastAPI routes for healthcare ecosystem taxonomy."""
from fastapi import APIRouter, HTTPException
from .service import HealthcareMedicalLifeSciencesService

router = APIRouter(prefix="/healthcare-medical-life-sciences", tags=["Healthcare, Medical & Life Sciences"])
service = HealthcareMedicalLifeSciencesService()

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
