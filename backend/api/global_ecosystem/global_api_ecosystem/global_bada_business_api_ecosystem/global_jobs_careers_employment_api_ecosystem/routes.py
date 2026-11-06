"""FastAPI routes for Jobs, Careers & Employment."""
from importlib import import_module as _import_module
from pkgutil import iter_modules as _iter_modules

from fastapi import APIRouter, HTTPException, Query

from .schemas import JobsCareersCategoryDetailResponse, JobsCareersCategoryListResponse
from .service import JobsCareersService

router = APIRouter(prefix="/jobs-careers-employment", tags=["GLOBAL BADA BUSINESS - JOBS & CAREERS"])
service = JobsCareersService()


@router.get("/status")
def get_status():
    return service.get_status()


@router.get("/categories", response_model=JobsCareersCategoryListResponse)
def list_domain_categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    items = service.list_categories(query=q)
    return {"success": True, "count": len(items), "categories": items}


@router.get("/categories/{category_id}", response_model=JobsCareersCategoryDetailResponse)
def get_domain_category(category_id: str):
    item = service.get_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "category": item}


@router.get("/employment-categories")
def list_employment_taxonomy_categories(q: str | None = Query(default=None, min_length=1, max_length=100)):
    """List the detailed employment taxonomy without duplicating its canonical source."""
    items = service.list_employment_categories(query=q)
    return {"success": True, "count": len(items), "taxonomy_status": "taxonomy_only", "categories": items}


@router.get("/employment-categories/{category_id}")
def get_employment_taxonomy_category(category_id: str):
    item = service.get_employment_category(category_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "EMPLOYMENT_CATEGORY_NOT_FOUND", "category_id": category_id})
    return {"success": True, "taxonomy_status": "taxonomy_only", "category": item}


# Each industry category owns a dedicated package router and mounts its
# independently addressable subcategory routers.
from . import __path__ as _jobs_careers_package_path
MOUNTED_CATEGORY_IDS: list[str] = []
for _category_package in _iter_modules(_jobs_careers_package_path):
    if not _category_package.ispkg or _category_package.name in {"tests", "__pycache__"}:
        continue
    _category_router = _import_module(
        f"{__package__}.{_category_package.name}.routes"
    ).router
    router.include_router(_category_router)
    MOUNTED_CATEGORY_IDS.append(_category_package.name)
