"""Work, Jobs & Careers subcategory API router."""
from fastapi import APIRouter

from .subcategories.government_jobs.routes import router as government_jobs_router
from .subcategories.private_sector_jobs.routes import router as private_jobs_router
from .subcategories.corporate_jobs.routes import router as corporate_jobs_router
from .subcategories.public_sector_jobs.routes import router as public_sector_jobs_router
from .subcategories.full_time_jobs.routes import router as full_time_jobs_router
from .subcategories.hybrid_jobs.routes import router as hybrid_jobs_router
from .subcategories.remote_jobs.routes import router as remote_jobs_router
from .subcategories.local_jobs.routes import router as local_jobs_router
from .subcategories.international_jobs.routes import router as international_jobs_router

router = APIRouter(prefix="/work-careers", tags=["Work, Jobs & Careers"])
router.include_router(government_jobs_router)
router.include_router(private_jobs_router)
router.include_router(corporate_jobs_router)
router.include_router(public_sector_jobs_router)
router.include_router(international_jobs_router)
router.include_router(local_jobs_router)
router.include_router(remote_jobs_router)
router.include_router(hybrid_jobs_router)
router.include_router(full_time_jobs_router)
