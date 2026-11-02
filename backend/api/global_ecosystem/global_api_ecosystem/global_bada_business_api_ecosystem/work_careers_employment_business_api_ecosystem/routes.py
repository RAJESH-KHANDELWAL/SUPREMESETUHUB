"""Work, Jobs & Careers subcategory API router."""
from fastapi import APIRouter

from .subcategories.government_jobs.routes import router as government_jobs_router
from .subcategories.private_sector_jobs.routes import router as private_jobs_router
from .subcategories.corporate_jobs.routes import router as corporate_jobs_router

router = APIRouter(prefix="/work-careers", tags=["Work, Jobs & Careers"])
router.include_router(government_jobs_router)
router.include_router(private_jobs_router)
router.include_router(corporate_jobs_router)
