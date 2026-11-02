"""Work, Jobs & Careers subcategory API router."""
from fastapi import APIRouter

from .subcategories.government_jobs.routes import router as government_jobs_router
from .subcategories.private_sector_jobs.routes import router as private_jobs_router
from .subcategories.corporate_jobs.routes import router as corporate_jobs_router
from .subcategories.public_sector_jobs.routes import router as public_sector_jobs_router
from .subcategories.full_time_jobs.routes import router as full_time_jobs_router
from .subcategories.seasonal_jobs.routes import router as seasonal_jobs_router
from .subcategories.entry_level_jobs.routes import router as entry_level_jobs_router
from .subcategories.shift_work.routes import router as shift_work_router
from .subcategories.temporary_jobs.routes import router as temporary_jobs_router
from .subcategories.contract_jobs.routes import router as contract_jobs_router
from .subcategories.part_time_jobs.routes import router as part_time_jobs_router
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
router.include_router(part_time_jobs_router)
router.include_router(contract_jobs_router)
router.include_router(temporary_jobs_router)
router.include_router(seasonal_jobs_router)
router.include_router(shift_work_router)
router.include_router(entry_level_jobs_router)
