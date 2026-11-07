"""Jobs, Careers & Employment category taxonomy."""
from __future__ import annotations

JOBS_CAREERS_EMPLOYMENT_CATEGORIES = [
    {
        "id": "recruitment_and_job_portals",
        "name": "Recruitment & Job Portals",
        "subcategories": [
            "job_boards",
            "employer_job_sites",
            "executive_vacancies",
            "campus_recruitment"
        ]
    },
    {
        "id": "freelancing_and_gig_work",
        "name": "Freelancing & Gig Work",
        "subcategories": [
            "freelance_marketplaces",
            "independent_contracting",
            "gig_platforms",
            "project_based_work"
        ]
    },
    {
        "id": "remote_and_hybrid_work",
        "name": "Remote & Hybrid Work",
        "subcategories": [
            "fully_remote_jobs",
            "hybrid_roles",
            "cross_border_remote_work",
            "distributed_teams"
        ]
    },
    {
        "id": "staffing_and_placement",
        "name": "Staffing & Placement",
        "subcategories": [
            "temporary_staffing",
            "permanent_placement",
            "contract_staffing",
            "recruitment_process_outsourcing"
        ]
    },
    {
        "id": "human_resources_and_payroll",
        "name": "Human Resources & Payroll",
        "subcategories": [
            "hr_consulting",
            "payroll_services",
            "benefits_administration",
            "hr_technology"
        ]
    },
    {
        "id": "career_guidance_and_counselling",
        "name": "Career Guidance & Counselling",
        "subcategories": [
            "career_assessment",
            "career_coaching",
            "career_transition",
            "workplace_guidance"
        ]
    },
    {
        "id": "internships_and_apprenticeships",
        "name": "Internships & Apprenticeships",
        "subcategories": [
            "student_internships",
            "graduate_programmes",
            "trade_apprenticeships",
            "returnships"
        ]
    },
    {
        "id": "executive_search",
        "name": "Executive Search & Leadership Hiring",
        "subcategories": [
            "c_suite_search",
            "board_search",
            "senior_management_hiring",
            "leadership_assessment"
        ]
    },
    {
        "id": "workforce_management",
        "name": "Workforce Management",
        "subcategories": [
            "workforce_planning",
            "shift_scheduling",
            "attendance_management",
            "field_workforce"
        ]
    },
    {
        "id": "resume_and_interview_services",
        "name": "Resume, Interview & Job Readiness",
        "subcategories": [
            "resume_writing",
            "profile_optimisation",
            "interview_preparation",
            "job_search_support"
        ]
    },
    {
        "id": "employer_branding",
        "name": "Employer Branding & Talent Marketing",
        "subcategories": [
            "employer_value_proposition",
            "talent_campaigns",
            "candidate_experience",
            "recruitment_marketing"
        ]
    },
    {
        "id": "employment_compliance",
        "name": "Labour & Employment Compliance",
        "subcategories": [
            "employment_contracts",
            "workplace_policies",
            "labour_compliance_advisory",
            "workplace_safety_training"
        ]
    },
    {
        "id": "outsourcing_and_bpo",
        "name": "Outsourcing & Business Process Services",
        "subcategories": [
            "business_process_outsourcing",
            "customer_support_operations",
            "knowledge_process_outsourcing",
            "staff_augmentation"
        ]
    },
    {
        "id": "reskilling_and_outplacement",
        "name": "Reskilling & Outplacement",
        "subcategories": [
            "career_reskilling",
            "redeployment_support",
            "outplacement_services",
            "workforce_transition"
        ]
    },
    {
        "id": "professional_networking",
        "name": "Professional Networking & Talent Communities",
        "subcategories": [
            "professional_networks",
            "talent_communities",
            "referral_networks",
            "industry_associations"
        ]
    }
]

def list_categories() -> list[dict[str, object]]:
    """Return defensive copies of all categories."""
    return [dict(item, subcategories=list(item["subcategories"])) for item in JOBS_CAREERS_EMPLOYMENT_CATEGORIES]

def get_category(category_id: str) -> dict[str, object] | None:
    """Return one category by stable identifier."""
    for item in JOBS_CAREERS_EMPLOYMENT_CATEGORIES:
        if item["id"] == category_id:
            return dict(item, subcategories=list(item["subcategories"]))
    return None
