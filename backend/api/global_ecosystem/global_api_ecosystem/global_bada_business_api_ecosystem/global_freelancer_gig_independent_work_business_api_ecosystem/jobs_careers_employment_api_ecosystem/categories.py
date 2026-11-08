"""Canonical detailed catalogue for the Work, Jobs & Careers domain.

This is taxonomy metadata, not a live vacancy database, employer-verification service,
recruitment agency, legal eligibility engine, or proof of active hiring.
"""
from __future__ import annotations

DOMAIN_ID = "work_careers_employment"
DOMAIN_NAME = "Work, Jobs & Careers"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
TAXONOMY_STATUS = "taxonomy_only"
COVERAGE_SCOPE = ("india", "global")

# Dimensions overlap by design: sector, geography, work arrangement, schedule,
# engagement type, seniority and career pathway are separate classification axes.
CATEGORY_DEFINITIONS = (
    {
        "id": "government_jobs", "name": "Government Jobs",
        "description": "Direct employment and recruitment by government ministries, departments, civil services, local authorities and statutory public administration bodies. Public-sector enterprises and government-owned corporations must also retain their separate employer-organization and ownership classifications; this category does not establish that a vacancy is active or that an applicant is eligible.",
        "category_type": "employer_sector",
        "ownership_sectors": ("government",),
        "employer_organization_types": ("ministry", "government_department", "local_authority", "statutory_public_authority", "civil_service_body"),
        "employment_types": ("permanent", "fixed_term", "temporary", "apprenticeship", "internship"),
        "work_arrangements": ("on_site", "field_based", "hybrid", "remote_where_officially_permitted"),
        "seniority_levels": ("entry_level", "graduate", "experienced", "supervisory", "senior", "executive"),
        "audience_groups": ("students_and_graduates", "job_seekers", "experienced_professionals", "career_returners"),
        "search_terms": ("sarkari naukri", "public service recruitment", "civil services", "government vacancy"),
        "scope_notes": ("Classify by the recruiting or employing public authority, not merely by public benefit.", "Capture country, jurisdiction, authority, recruitment body and notice identifier.", "Age, domicile, nationality, reservation, qualification and examination rules are notice- and jurisdiction-specific."),
        "verification_requirements": ("official_notice_url", "issuing_authority", "jurisdiction", "notice_id", "publication_date", "application_deadline_if_any", "last_verified_at"),
        "related_category_ids": ("public_sector_jobs", "local_jobs", "full_time_jobs", "contract_jobs", "entry_level_jobs", "experienced_jobs"),
    },
    {
        "id": "private_sector_jobs", "name": "Private Jobs (Private Sector)",
        "description": "Employment with privately owned businesses and non-government employers, including proprietorships, partnerships, private firms, startups and privately owned companies. Corporate employers may also be tagged under the separate Corporate Jobs category; this category represents ownership sector, not company size or corporate structure.",
        "category_type": "employer_sector",
        "ownership_sectors": ("private",),
        "employer_organization_types": ("proprietorship", "partnership", "private_company", "private_limited_company", "private_corporate_group", "startup", "small_or_medium_business"),
        "employment_types": ("permanent", "fixed_term", "temporary", "contract", "internship", "apprenticeship"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("entry_level", "junior", "mid_level", "senior", "lead", "executive"),
        "audience_groups": ("students_and_graduates", "job_seekers", "professionals", "career_changers"),
        "search_terms": ("private jobs", "private sector jobs", "private company jobs", "private employment", "startup jobs", "company careers"),
        "scope_notes": ("Do not infer employer legitimacy from a listing or domain name.", "Capture employer identity, location, source, compensation basis and verification state separately."),
        "verification_requirements": ("employer_identity", "original_listing_url", "jurisdiction", "published_or_updated_at", "last_verified_at"),
        "related_category_ids": ("full_time_jobs", "part_time_jobs", "contract_jobs", "remote_jobs", "hybrid_jobs"),
    },
    {
        "id": "corporate_jobs", "name": "Corporate Jobs",
        "description": "Employment with incorporated companies, corporate groups, multinational companies, listed companies, large and mid-sized organized enterprises, and other employers operating through a formal corporate structure. Corporate describes the employer organization type, not its ownership: a corporate employer may be privately owned or government-owned, so ownership_sector must be recorded separately.",
        "category_type": "employer_organization_type",
        "ownership_sectors": ("private", "public_sector_or_state_owned", "mixed_or_joint_ownership", "unknown"),
        "employer_organization_types": ("private_limited_company", "public_limited_company", "listed_company", "multinational_corporation", "corporate_group", "government_owned_corporation", "state_owned_enterprise"),
        "employment_types": ("permanent", "fixed_term", "temporary", "contract", "internship", "apprenticeship"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("entry_level", "junior", "mid_level", "senior", "lead", "executive", "board_level"),
        "audience_groups": ("students_and_graduates", "job_seekers", "experienced_professionals", "corporate_professionals", "executives"),
        "search_terms": ("corporate jobs", "MNC jobs", "multinational company careers", "corporate careers", "company group jobs", "listed company jobs"),
        "scope_notes": ("Corporate is an employer-organization classification and may overlap with private-sector or public-sector ownership.", "Record the legal employer name, registration jurisdiction, ownership sector and corporate group relationship separately.", "Do not infer that an employer is listed, multinational, large or government-owned without a reliable source."),
        "verification_requirements": ("legal_employer_identity", "employer_organization_type", "ownership_sector", "registration_jurisdiction_if_available", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("private_sector_jobs", "public_sector_jobs", "government_jobs", "full_time_jobs", "executive_jobs"),
    },
    {
        "id": "public_sector_jobs", "name": "Public Sector Jobs",
        "description": "Employment in public-sector enterprises, government-owned or government-controlled entities, public institutions and other jurisdictionally defined public bodies; distinct from direct civil-service recruitment.",
        "category_type": "employer_sector",
        "ownership_sectors": ("public_sector_or_state_owned", "mixed_or_joint_ownership"),
        "employer_organization_types": ("public_sector_enterprise", "state_owned_company", "government_owned_corporation", "public_institution"),
        "employment_types": ("permanent", "fixed_term", "temporary", "contract", "apprenticeship"),
        "work_arrangements": ("on_site", "field_based", "hybrid", "remote_where_permitted"),
        "seniority_levels": ("entry_level", "graduate", "experienced", "supervisory", "senior", "executive"),
        "audience_groups": ("graduates", "technical_professionals", "experienced_workers", "job_seekers"),
        "search_terms": ("public sector undertaking jobs", "PSU recruitment", "state enterprise careers"),
        "scope_notes": ("Record the ownership or control basis used for classification.", "Do not merge public-sector enterprise roles with civil-service posts without retaining employer type."),
        "verification_requirements": ("employer_identity", "ownership_or_control_basis", "official_notice_url", "jurisdiction", "last_verified_at"),
        "related_category_ids": ("government_jobs", "full_time_jobs", "contract_jobs", "experienced_jobs"),
    },
    {
        "id": "international_jobs", "name": "International Jobs",
        "description": "Employment in a country other than the worker's ordinary residence, cross-border recruitment, international organizations or explicitly multi-country hiring. Work authorization is a separate legal attribute.",
        "category_type": "geographic_scope",
        "employment_types": ("permanent", "fixed_term", "contract", "temporary", "internship"),
        "work_arrangements": ("relocation", "cross_border_remote", "travel_based", "hybrid"),
        "seniority_levels": ("entry_level", "experienced", "senior", "executive"),
        "audience_groups": ("international_job_seekers", "migrant_workers", "global_professionals"),
        "search_terms": ("overseas jobs", "jobs abroad", "international recruitment", "global careers"),
        "scope_notes": ("Capture hiring country, work location and employing entity.", "Never imply visa sponsorship or work authorization unless the source explicitly confirms it."),
        "verification_requirements": ("employer_identity", "destination_country", "work_location", "official_listing_url", "sponsorship_statement_if_any", "last_verified_at"),
        "related_category_ids": ("remote_jobs", "contract_jobs", "full_time_jobs", "experienced_jobs"),
    },
    {
        "id": "local_jobs", "name": "Local Jobs",
        "description": "Roles whose primary work location is a specified city, district, region or commuting area. Locality is a geographic filter, not an employer-sector or contract-type classification.",
        "category_type": "geographic_scope",
        "employment_types": ("permanent", "temporary", "part_time", "contract", "seasonal"),
        "work_arrangements": ("on_site", "field_based", "hybrid"),
        "seniority_levels": ("entry_level", "junior", "experienced", "senior"),
        "audience_groups": ("local_job_seekers", "students", "returning_workers"),
        "search_terms": ("jobs near me", "city jobs", "district jobs", "local vacancies"),
        "scope_notes": ("Store normalized locality and country separately; do not infer a user's location.", "A remote role is not local merely because the employer has a local office."),
        "verification_requirements": ("work_location", "employer_identity", "original_listing_url", "published_or_updated_at", "last_verified_at"),
        "related_category_ids": ("full_time_jobs", "part_time_jobs", "temporary_jobs", "seasonal_jobs"),
    },
    {
        "id": "remote_jobs", "name": "Remote Jobs",
        "description": "Roles explicitly advertised as performable away from a designated employer workplace. Geographic restrictions, time-zone expectations, equipment and attendance requirements must be retained.",
        "category_type": "work_arrangement",
        "employment_types": ("permanent", "fixed_term", "contract", "part_time", "temporary"),
        "work_arrangements": ("fully_remote", "distributed_team", "remote_with_periodic_travel"),
        "seniority_levels": ("entry_level", "junior", "mid_level", "senior", "executive"),
        "audience_groups": ("remote_workers", "global_professionals", "career_changers"),
        "search_terms": ("work from home jobs", "WFH jobs", "fully remote careers", "distributed teams"),
        "scope_notes": ("Remote does not mean work-from-anywhere; capture eligible countries and regions.", "Distinguish employee roles from freelance projects and independent-contractor engagements."),
        "verification_requirements": ("remote_policy_statement", "eligible_work_locations", "employment_relationship", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("international_jobs", "hybrid_jobs", "full_time_jobs", "part_time_jobs", "contract_jobs"),
    },
    {
        "id": "hybrid_jobs", "name": "Hybrid Jobs",
        "description": "Roles combining work at an employer-designated workplace with remote work. Required attendance frequency and location should be recorded when supplied.",
        "category_type": "work_arrangement",
        "employment_types": ("permanent", "fixed_term", "contract", "part_time"),
        "work_arrangements": ("hybrid", "office_and_remote", "field_and_office"),
        "seniority_levels": ("entry_level", "junior", "mid_level", "senior", "executive"),
        "audience_groups": ("job_seekers", "working_professionals", "career_returners"),
        "search_terms": ("hybrid work jobs", "office hybrid careers", "flexible workplace jobs"),
        "scope_notes": ("Record office location and stated on-site cadence; do not assume a standard number of office days.", "Occasional travel alone does not make a role hybrid."),
        "verification_requirements": ("hybrid_policy_statement", "office_location", "attendance_expectation_if_stated", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("remote_jobs", "local_jobs", "full_time_jobs", "part_time_jobs"),
    },
    {
        "id": "full_time_jobs", "name": "Full-Time Jobs",
        "description": "Roles described by the employer or applicable jurisdiction as full-time. Working-hour thresholds and statutory definitions differ by country and sector.",
        "category_type": "working_time",
        "employment_types": ("permanent", "fixed_term", "contract"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("entry_level", "junior", "mid_level", "senior", "executive"),
        "audience_groups": ("job_seekers", "graduates", "experienced_professionals"),
        "search_terms": ("full time employment", "full-time vacancies", "regular jobs"),
        "scope_notes": ("Preserve employer-stated hours and local full-time definition where available.", "Do not determine statutory status from hours without jurisdiction-specific rules."),
        "verification_requirements": ("employer_stated_hours", "employment_relationship", "original_listing_url", "jurisdiction", "last_verified_at"),
        "related_category_ids": ("private_sector_jobs", "government_jobs", "remote_jobs", "contract_jobs"),
    },
    {
        "id": "part_time_jobs", "name": "Part-Time Jobs",
        "description": "Roles expressly designated as part-time or scheduled for fewer hours than the employer's ordinary full-time schedule.",
        "category_type": "working_time",
        "employment_types": ("permanent", "fixed_term", "temporary", "contract"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("entry_level", "junior", "experienced"),
        "audience_groups": ("students", "caregivers", "career_returners", "supplementary_income_seekers"),
        "search_terms": ("part time jobs", "part-time work", "flexible hours employment"),
        "scope_notes": ("Record hours, shifts and schedule constraints when published.", "Part-time is not synonymous with temporary, casual or freelance work."),
        "verification_requirements": ("stated_hours_or_schedule", "employment_relationship", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("temporary_jobs", "seasonal_jobs", "remote_jobs", "local_jobs"),
    },
    {
        "id": "contract_jobs", "name": "Contract Jobs",
        "description": "Time-bounded or deliverable-bounded engagements governed by an employment or services contract. Preserve whether the worker is an employee, agency worker or independent contractor.",
        "category_type": "engagement_type",
        "employment_types": ("fixed_term_employee", "independent_contractor", "agency_contract", "project_contract"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("entry_level", "experienced", "specialist", "senior"),
        "audience_groups": ("contract_professionals", "specialists", "project_workers"),
        "search_terms": ("contract employment", "fixed term jobs", "project contract roles"),
        "scope_notes": ("Record duration, deliverables and termination terms only when sourced.", "Do not classify gig or freelance work as employment without evidence of the relationship."),
        "verification_requirements": ("contract_relationship_type", "duration_if_stated", "employer_or_client_identity", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("temporary_jobs", "experienced_jobs", "remote_jobs"),
    },
    {
        "id": "temporary_jobs", "name": "Temporary Jobs",
        "description": "Roles intended to exist for a limited period, including short-term cover, temporary staffing and time-limited operational work.",
        "category_type": "engagement_type",
        "employment_types": ("temporary_employee", "agency_worker", "fixed_term"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("entry_level", "junior", "experienced"),
        "audience_groups": ("temporary_workers", "students", "seasonal_workers", "career_returners"),
        "search_terms": ("temporary vacancies", "short term jobs", "temp staffing"),
        "scope_notes": ("Record start and end dates only when the source provides them.", "Do not assume benefits or conversion to permanent employment."),
        "verification_requirements": ("employer_or_agency_identity", "duration_if_stated", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("contract_jobs", "seasonal_jobs", "part_time_jobs"),
    },
    {
        "id": "seasonal_jobs", "name": "Seasonal Jobs",
        "description": "Roles linked to recurring or time-limited seasonal demand in agriculture, tourism, hospitality, retail, logistics and related sectors.",
        "category_type": "engagement_type",
        "employment_types": ("seasonal_employee", "temporary", "fixed_term"),
        "work_arrangements": ("on_site", "field_based", "remote_where_role_allows"),
        "seniority_levels": ("entry_level", "experienced", "supervisory"),
        "audience_groups": ("seasonal_workers", "students", "temporary_workers"),
        "search_terms": ("seasonal employment", "harvest jobs", "holiday season jobs"),
        "scope_notes": ("Record season, duration, location and accommodation or travel terms when stated.", "Seasonality describes demand timing, not legal employment status."),
        "verification_requirements": ("season_or_period", "work_location", "employer_identity", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("temporary_jobs", "local_jobs", "part_time_jobs"),
    },
    {
        "id": "shift_work", "name": "Shift Work",
        "description": "Roles scheduled in defined day, evening, night, rotating, split or continuous-operation shifts.",
        "category_type": "schedule_pattern",
        "employment_types": ("permanent", "fixed_term", "temporary", "contract"),
        "work_arrangements": ("on_site", "field_based", "remote_where_shift_based"),
        "seniority_levels": ("entry_level", "experienced", "supervisory"),
        "audience_groups": ("shift_workers", "operations_workers", "healthcare_workers", "service_workers"),
        "search_terms": ("night shift jobs", "rotational shifts", "day shift vacancies", "24x7 operations jobs"),
        "scope_notes": ("Capture shift timing, rotation, rest days and stated allowances.", "Do not infer working-time-law compliance from a schedule label."),
        "verification_requirements": ("shift_pattern_if_stated", "work_location", "employer_identity", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("full_time_jobs", "part_time_jobs", "local_jobs"),
    },
    {
        "id": "entry_level_jobs", "name": "Entry-Level Jobs",
        "description": "Roles designed for applicants with limited relevant work experience, including graduate-entry, trainee and junior pathways where stated.",
        "category_type": "experience_level",
        "employment_types": ("permanent", "fixed_term", "internship", "apprenticeship", "trainee"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("entry_level", "trainee", "graduate", "junior"),
        "audience_groups": ("first_time_job_seekers", "students", "recent_graduates", "career_changers"),
        "search_terms": ("fresher jobs", "graduate jobs", "no experience jobs", "junior vacancies"),
        "scope_notes": ("Preserve actual experience and qualification requirements; entry-level does not always mean no experience.", "Internships and apprenticeships remain distinct engagement types."),
        "verification_requirements": ("stated_experience_requirements", "qualification_requirements_if_stated", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("career_changes", "placements", "full_time_jobs", "government_jobs"),
    },
    {
        "id": "experienced_jobs", "name": "Experienced Professional Jobs",
        "description": "Roles requiring prior relevant experience, specialist capability, demonstrated responsibility or a stated professional track record.",
        "category_type": "experience_level",
        "employment_types": ("permanent", "fixed_term", "contract", "temporary"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("mid_level", "senior", "specialist", "lead"),
        "audience_groups": ("experienced_professionals", "specialists", "career_returners"),
        "search_terms": ("experienced candidate jobs", "professional vacancies", "mid career jobs", "specialist roles"),
        "scope_notes": ("Capture minimum years and type of experience as stated; do not infer seniority from title alone.", "Professional registration requirements must be jurisdiction- and role-specific."),
        "verification_requirements": ("stated_experience_requirements", "role_requirements", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("executive_jobs", "contract_jobs", "private_sector_jobs", "government_jobs"),
    },
    {
        "id": "executive_jobs", "name": "Executive Jobs",
        "description": "Senior leadership, executive management and board-level employment roles with organization-wide or major business-unit accountability.",
        "category_type": "seniority_level",
        "employment_types": ("permanent", "fixed_term", "executive_contract"),
        "work_arrangements": ("on_site", "hybrid", "remote_where_role_allows", "travel_based"),
        "seniority_levels": ("director", "vice_president", "c_suite", "managing_director", "board_level"),
        "audience_groups": ("senior_leaders", "executives", "board_candidates"),
        "search_terms": ("C-suite jobs", "director vacancies", "executive leadership roles"),
        "scope_notes": ("Record reporting line, remit and governance responsibilities when disclosed.", "Do not infer board appointment, fiduciary authority or compensation from title alone."),
        "verification_requirements": ("employer_identity", "role_remit_if_published", "original_listing_url", "last_verified_at"),
        "related_category_ids": ("experienced_jobs", "private_sector_jobs", "government_jobs"),
    },
    {
        "id": "career_changes", "name": "Career Change Opportunities",
        "description": "Roles and structured pathways suitable for transitions between occupations, sectors or professional tracks. This describes candidate intent, not a separate employment relationship.",
        "category_type": "career_pathway",
        "employment_types": ("permanent", "fixed_term", "internship", "apprenticeship", "trainee", "contract"),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": ("entry_level", "junior", "experienced"),
        "audience_groups": ("career_changers", "returning_workers", "reskilling_adults"),
        "search_terms": ("career transition jobs", "second career", "reskilling jobs", "career switch"),
        "scope_notes": ("Show transferable-skill and retraining requirements only when supported by the source.", "Do not promise placement or guaranteed employment."),
        "verification_requirements": ("employer_or_programme_identity", "pathway_requirements", "original_source_url", "last_verified_at"),
        "related_category_ids": ("entry_level_jobs", "career_guidance", "return_to_work"),
    },
    {
        "id": "return_to_work", "name": "Return-to-Work Opportunities",
        "description": "Roles and programmes intended to support people re-entering employment after a career break, caregiving period, education or other absence.",
        "category_type": "career_pathway",
        "employment_types": ("permanent", "fixed_term", "part_time", "internship", "returnship"),
        "work_arrangements": ("on_site", "remote", "hybrid", "flexible_where_offered"),
        "seniority_levels": ("entry_level", "experienced", "senior"),
        "audience_groups": ("career_returners", "caregivers_reentering_work", "professionals_after_break"),
        "search_terms": ("returnship", "back to work programme", "career relaunch", "returner jobs"),
        "scope_notes": ("Avoid collecting or inferring sensitive reasons for a career break.", "Record programme eligibility and support terms only from the official source."),
        "verification_requirements": ("programme_or_employer_identity", "eligibility_terms_if_stated", "original_source_url", "last_verified_at"),
        "related_category_ids": ("part_time_jobs", "career_guidance", "career_changes", "remote_jobs"),
    },
    {
        "id": "retirement_work", "name": "Retirement-Age Work Opportunities",
        "description": "Phased-retirement roles, consultancy and flexible engagements that may be relevant to people continuing or resuming work around retirement age.",
        "category_type": "career_pathway",
        "employment_types": ("part_time", "fixed_term", "consultancy", "contract", "temporary"),
        "work_arrangements": ("on_site", "remote", "hybrid", "flexible_where_offered"),
        "seniority_levels": ("experienced", "specialist", "advisory"),
        "audience_groups": ("older_workers", "retired_professionals", "experienced_consultants"),
        "search_terms": ("retirement jobs", "phased retirement work", "experienced consultant roles"),
        "scope_notes": ("Do not assume age eligibility, pension effects or statutory retirement rules.", "Use inclusive, non-discriminatory descriptions."),
        "verification_requirements": ("employer_or_client_identity", "engagement_terms", "jurisdiction", "original_source_url", "last_verified_at"),
        "related_category_ids": ("part_time_jobs", "contract_jobs", "experienced_jobs", "career_guidance"),
    },
    {
        "id": "career_guidance", "name": "Career Guidance",
        "description": "Career information, counselling, assessment, mentoring and planning services supporting education-to-work and career decisions; these are services, not vacancies.",
        "category_type": "career_support_service",
        "employment_types": (),
        "work_arrangements": ("in_person", "online", "hybrid"),
        "seniority_levels": (),
        "audience_groups": ("students", "job_seekers", "career_changers", "working_professionals", "career_returners"),
        "search_terms": ("career counselling", "career coaching", "career assessment", "career planning"),
        "scope_notes": ("Keep guidance providers and service offers separate from vacancy records.", "Do not claim accreditation, guaranteed outcomes or professional credentials without evidence."),
        "verification_requirements": ("provider_identity", "service_description", "credential_claims_if_any", "source_url", "last_verified_at"),
        "related_category_ids": ("career_changes", "return_to_work", "recruitment", "placements"),
    },
    {
        "id": "recruitment", "name": "Recruitment",
        "description": "Activities and services for sourcing, assessing and selecting candidates for employment. Distinguish employer-side hiring from third-party recruitment agencies.",
        "category_type": "recruitment_service",
        "employment_types": (),
        "work_arrangements": ("in_person", "online", "hybrid"),
        "seniority_levels": (),
        "audience_groups": ("employers", "recruiters", "job_seekers"),
        "search_terms": ("recruitment services", "talent acquisition", "hiring services", "recruitment agency"),
        "scope_notes": ("Recruitment service listings are not job vacancies.", "Capture fee payer, service territory and licensing claims where applicable; do not assume authorization."),
        "verification_requirements": ("provider_identity", "service_terms", "jurisdiction", "licence_claim_if_any", "source_url", "last_verified_at"),
        "related_category_ids": ("staffing", "placements", "private_sector_jobs", "government_jobs"),
    },
    {
        "id": "staffing", "name": "Staffing Services",
        "description": "Workforce supply and staffing services, including temporary staffing, contract staffing, managed workforce and employer-of-record arrangements where lawfully offered.",
        "category_type": "workforce_service",
        "employment_types": (),
        "work_arrangements": ("on_site", "remote", "hybrid", "field_based"),
        "seniority_levels": (),
        "audience_groups": ("employers", "staffing_providers", "workers"),
        "search_terms": ("staffing agency", "temporary staffing", "contract staffing", "workforce solutions"),
        "scope_notes": ("Identify legal employer, intermediary and end client separately when known.", "Do not treat marketing statements as proof of worker classification or compliance."),
        "verification_requirements": ("provider_identity", "service_scope", "jurisdiction", "worker_relationship_disclosure", "source_url", "last_verified_at"),
        "related_category_ids": ("recruitment", "contract_jobs", "temporary_jobs", "placements"),
    },
    {
        "id": "placements", "name": "Job Placement Services",
        "description": "Services and programmes connecting candidates with employers, including institutional placement cells, workforce programmes and placement agencies.",
        "category_type": "career_support_service",
        "employment_types": (),
        "work_arrangements": ("in_person", "online", "hybrid"),
        "seniority_levels": (),
        "audience_groups": ("students", "graduates", "job_seekers", "employers"),
        "search_terms": ("job placement", "campus placement", "employment placement services", "placement agency"),
        "scope_notes": ("A placement service is not itself an employment offer.", "Do not promise placement, salary or selection; distinguish historical outcomes from guarantees."),
        "verification_requirements": ("provider_identity", "employer_relationship_if_claimed", "service_terms", "outcome_claim_evidence_if_any", "source_url", "last_verified_at"),
        "related_category_ids": ("recruitment", "staffing", "career_guidance", "entry_level_jobs"),
    },
)

CATEGORY_IDS = tuple(item["id"] for item in CATEGORY_DEFINITIONS)
# Compatibility alias consumed by the shared cross-domain registry.
SUBCATEGORY_IDS = CATEGORY_IDS

def get_category_definition(category_id: str) -> dict | None:
    """Return a defensive copy of a category definition by stable ID."""
    for item in CATEGORY_DEFINITIONS:
        if item["id"] == category_id:
            return {key: tuple(value) if isinstance(value, tuple) else value for key, value in item.items()}
    return None

def validate_category_definitions() -> dict:
    """Validate internal structure and references, not external truth or legal status."""
    ids = [item["id"] for item in CATEGORY_DEFINITIONS]
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    required = ("name", "description", "category_type", "search_terms", "scope_notes")
    missing_fields = {
        item["id"]: [field for field in required if not item.get(field)]
        for item in CATEGORY_DEFINITIONS
        if any(not item.get(field) for field in required)
    }
    unknown_related = {
        item["id"]: sorted(set(item["related_category_ids"]) - set(ids))
        for item in CATEGORY_DEFINITIONS
        if set(item["related_category_ids"]) - set(ids)
    }
    return {
        "domain_id": DOMAIN_ID,
        "category_count": len(CATEGORY_DEFINITIONS),
        "duplicate_ids": duplicate_ids,
        "missing_required_fields": missing_fields,
        "unknown_related_category_ids": unknown_related,
        "structurally_valid": not duplicate_ids and not missing_fields and not unknown_related,
        "taxonomy_status": TAXONOMY_STATUS,
        "live_vacancies_verified": False,
        "employers_verified": False,
        "legal_eligibility_verified": False,
    }


# Backward-compatible cross-category specialization lookup. Each category package
# owns its specialization catalogue; this resolver only locates the canonical owner.
from importlib import import_module as _import_module

def list_specializations(category_id: str) -> list[dict]:
    if category_id not in CATEGORY_IDS:
        return []
    module = _import_module(f"{__package__}.{category_id}.categories")
    accessor = getattr(module, "list_tracks", None)
    return accessor() if callable(accessor) else []

def get_track(track_id: str) -> dict | None:
    """Find a specialization by stable ID across its owning category packages."""
    for category_id in CATEGORY_IDS:
        for item in list_specializations(category_id):
            if item.get("id") == track_id:
                return dict(item)
    return None
