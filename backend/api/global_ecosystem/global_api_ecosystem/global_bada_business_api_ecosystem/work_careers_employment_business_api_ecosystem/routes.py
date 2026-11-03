"""Work, Jobs & Careers category API router."""
from importlib import import_module
from fastapi import APIRouter

from .ecosystem_routes import router as api_ecosystems_router
from .professional_fields.routes import router as professional_fields_router

from .government_jobs.routes import router as government_jobs_router
from .private_sector_jobs.routes import router as private_jobs_router
from .corporate_jobs.routes import router as corporate_jobs_router
from .public_sector_jobs.routes import router as public_sector_jobs_router
from .full_time_jobs.routes import router as full_time_jobs_router
from .seasonal_jobs.routes import router as seasonal_jobs_router
from .entry_level_jobs.routes import router as entry_level_jobs_router
from .career_changes.routes import router as career_changes_router
from .placements.routes import router as placements_router
from .staffing.routes import router as staffing_router
from .recruitment.routes import router as recruitment_router
from .career_guidance.routes import router as career_guidance_router
from .retirement_work.routes import router as retirement_work_router
from .return_to_work.routes import router as return_to_work_router
from .executive_jobs.routes import router as executive_jobs_router
from .experienced_jobs.routes import router as experienced_jobs_router
from .shift_work.routes import router as shift_work_router
from .temporary_jobs.routes import router as temporary_jobs_router
from .contract_jobs.routes import router as contract_jobs_router
from .part_time_jobs.routes import router as part_time_jobs_router
from .hybrid_jobs.routes import router as hybrid_jobs_router
from .remote_jobs.routes import router as remote_jobs_router
from .local_jobs.routes import router as local_jobs_router
from .international_jobs.routes import router as international_jobs_router

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

# Category and track API Ecosystems are exposed through a shared hierarchical registry.
router.include_router(api_ecosystems_router)

# Professional occupation fields use a separate taxonomy axis from employment context.
router.include_router(professional_fields_router)


# Mount each work/job specialization as an independent API Ecosystem resource beneath its category.
from .categories import CATEGORY_IDS as _WORK_CAREERS_CATEGORY_IDS
for _category_id in _WORK_CAREERS_CATEGORY_IDS:
    _category_routes = import_module(f"{__package__}.{_category_id}.routes").router
    _category_module = import_module(f"{__package__}.{_category_id}.categories")
    for _specialization_definition in _category_module.list_tracks():
        _specialization_router = import_module(
            f"{__package__}.{_category_id}.{_specialization_definition['id']}.routes"
        ).router
        _specialization_router.prefix = _specialization_router.prefix.replace("/tracks/", "/work-jobs/")
        router.include_router(_specialization_router, prefix=_category_routes.prefix)
del _category_id, _category_routes, _category_module, _specialization_definition, _specialization_router, _WORK_CAREERS_CATEGORY_IDS
