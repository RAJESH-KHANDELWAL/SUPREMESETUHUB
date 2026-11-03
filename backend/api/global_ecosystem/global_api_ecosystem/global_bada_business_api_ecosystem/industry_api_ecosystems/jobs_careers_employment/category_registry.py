"""Registry of independently mounted Jobs, Careers & Employment category routers."""
from .recruitment_and_job_portals.routes import router as RECRUITMENT_AND_JOB_PORTALS_ROUTER
from .freelancing_and_gig_work.routes import router as FREELANCING_AND_GIG_WORK_ROUTER
from .remote_and_hybrid_work.routes import router as REMOTE_AND_HYBRID_WORK_ROUTER
from .staffing_and_placement.routes import router as STAFFING_AND_PLACEMENT_ROUTER
from .human_resources_and_payroll.routes import router as HUMAN_RESOURCES_AND_PAYROLL_ROUTER
from .career_guidance_and_counselling.routes import router as CAREER_GUIDANCE_AND_COUNSELLING_ROUTER
from .internships_and_apprenticeships.routes import router as INTERNSHIPS_AND_APPRENTICESHIPS_ROUTER
from .executive_search.routes import router as EXECUTIVE_SEARCH_ROUTER
from .workforce_management.routes import router as WORKFORCE_MANAGEMENT_ROUTER
from .resume_and_interview_services.routes import router as RESUME_AND_INTERVIEW_SERVICES_ROUTER
from .employer_branding.routes import router as EMPLOYER_BRANDING_ROUTER
from .employment_compliance.routes import router as EMPLOYMENT_COMPLIANCE_ROUTER
from .outsourcing_and_bpo.routes import router as OUTSOURCING_AND_BPO_ROUTER
from .reskilling_and_outplacement.routes import router as RESKILLING_AND_OUTPLACEMENT_ROUTER
from .professional_networking.routes import router as PROFESSIONAL_NETWORKING_ROUTER

CATEGORY_ROUTERS = (
    RECRUITMENT_AND_JOB_PORTALS_ROUTER,
    FREELANCING_AND_GIG_WORK_ROUTER,
    REMOTE_AND_HYBRID_WORK_ROUTER,
    STAFFING_AND_PLACEMENT_ROUTER,
    HUMAN_RESOURCES_AND_PAYROLL_ROUTER,
    CAREER_GUIDANCE_AND_COUNSELLING_ROUTER,
    INTERNSHIPS_AND_APPRENTICESHIPS_ROUTER,
    EXECUTIVE_SEARCH_ROUTER,
    WORKFORCE_MANAGEMENT_ROUTER,
    RESUME_AND_INTERVIEW_SERVICES_ROUTER,
    EMPLOYER_BRANDING_ROUTER,
    EMPLOYMENT_COMPLIANCE_ROUTER,
    OUTSOURCING_AND_BPO_ROUTER,
    RESKILLING_AND_OUTPLACEMENT_ROUTER,
    PROFESSIONAL_NETWORKING_ROUTER,
)
