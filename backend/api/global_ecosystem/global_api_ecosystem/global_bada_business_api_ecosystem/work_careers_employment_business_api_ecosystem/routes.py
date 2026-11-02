"""Work, Jobs & Careers subcategory API router."""
from fastapi import APIRouter

from .subcategories.government_jobs.routes import router as government_jobs_router

router = APIRouter(prefix="/work-careers", tags=["Work, Jobs & Careers"])
router.include_router(government_jobs_router)
