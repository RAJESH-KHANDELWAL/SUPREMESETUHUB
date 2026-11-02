"""Work, Jobs & Careers subcategory API router."""
from fastapi import APIRouter

from .subcategories.government_jobs.routes import router as government_jobs_router
from .subcategories.private_sector_jobs.routes import router as private_jobs_router
from .subcategories.corporate_jobs.routes import router as corporate_jobs_router
from .subcategories.public_sector_jobs.routes import router as public_sector_jobs_router
from .subcategories.full_time_jobs.routes import router as full_time_jobs_router
from .subcategories.seasonal_jobs.routes import router as seasonal_jobs_router
from .subcategories.entry_level_jobs.routes import router as entry_level_jobs_router
from .subcategories.career_changes.routes import router as career_changes_router
from .subcategories.placements.routes import router as placements_router
from .subcategories.staffing.routes import router as staffing_router
from .subcategories.recruitment.routes import router as recruitment_router
from .subcategories.career_guidance.routes import router as career_guidance_router
from .subcategories.retirement_work.routes import router as retirement_work_router
from .subcategories.return_to_work.routes import router as return_to_work_router
from .subcategories.executive_jobs.routes import router as executive_jobs_router
from .subcategories.experienced_jobs.routes import router as experienced_jobs_router
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
router.include_router(experienced_jobs_router)
router.include_router(executive_jobs_router)
router.include_router(career_changes_router)
router.include_router(return_to_work_router)
router.include_router(retirement_work_router)
router.include_router(career_guidance_router)
router.include_router(recruitment_router)
router.include_router(staffing_router)
router.include_router(placements_router)
