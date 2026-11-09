"""Detailed taxonomy for Government Jobs.

This package classifies recruitment tracks; it is not a live vacancy directory.
Every real notice must be stored separately with official source provenance.
"""
CATEGORY_ID = "government_jobs"
CATEGORY_NAME = "Government Jobs"
PARENT_DOMAIN_ID = "work_careers_employment"
TAXONOMY_STATUS = "taxonomy_only"

GOVERNMENT_JOB_TRACKS = (
    {
        "id": "central_government_recruitment",
        "name": "Central Government Recruitment",
        "description": "Recruitment issued by national or federal ministries, departments, offices and other central public authorities.",
        "authority_scope": "national_or_federal",
        "role_families": ("administration", "technical", "finance_and_accounts", "research", "clerical_and_support"),
        "source_expectation": "Official ministry, department, commission or recruiting-body notice.",
        "classification_caution": "A government-owned company is not automatically a civil-service employer.",
    },
    {
        "id": "state_government_recruitment",
        "name": "State or Provincial Government Recruitment",
        "description": "Recruitment issued by state, provincial or equivalent subnational government departments and authorities.",
        "authority_scope": "state_or_provincial",
        "role_families": ("administration", "education", "health", "engineering", "revenue", "police_and_public_safety"),
        "source_expectation": "Official state or provincial recruiting commission, department or authority notice.",
        "classification_caution": "Domicile, language, reservation and local eligibility rules are jurisdiction- and notice-specific.",
    },
    {
        "id": "local_government_recruitment",
        "name": "Local Government Recruitment",
        "description": "Recruitment by municipal, city, district, county, panchayat or other local public authorities.",
        "authority_scope": "local",
        "role_families": ("municipal_services", "local_administration", "public_health", "engineering_and_works", "community_services"),
        "source_expectation": "Official local authority or authorized recruiting-body notice.",
        "classification_caution": "Record the exact local jurisdiction; a private contractor is not necessarily a local-government employer.",
    },
    {
        "id": "civil_services",
        "name": "Civil Services",
        "description": "Public administration and civil-service career tracks recruited under the applicable national or subnational civil-service framework.",
        "authority_scope": "jurisdiction_defined",
        "role_families": ("administrative_services", "foreign_or_external_affairs", "revenue_services", "audit_and_accounts", "public_policy"),
        "source_expectation": "Official civil-service commission or authorized government recruitment notice.",
        "classification_caution": "Service names, cadres, examinations and eligibility vary by jurisdiction and recruitment cycle.",
    },
    {
        "id": "public_education_recruitment",
        "name": "Public Education Recruitment",
        "description": "Teaching, academic, research-support and education-administration recruitment by public schools, colleges, universities and education authorities.",
        "authority_scope": "public_education",
        "role_families": ("school_teaching", "higher_education", "technical_education", "education_administration", "research_support"),
        "source_expectation": "Official institution, education department or authorized recruitment notice.",
        "classification_caution": "Teacher eligibility, academic equivalence and professional registration must not be inferred.",
    },
    {
        "id": "public_health_recruitment",
        "name": "Public Health Recruitment",
        "description": "Clinical, public-health, laboratory, health-administration and allied roles employed by public health systems and institutions.",
        "authority_scope": "public_health_system",
        "role_families": ("clinical_services", "nursing", "allied_health", "laboratory_services", "public_health_administration"),
        "source_expectation": "Official public health authority, hospital, institution or recruitment body notice.",
        "classification_caution": "Professional licences, registration and scope of practice require independent jurisdictional validation.",
    },
    {
        "id": "public_safety_recruitment",
        "name": "Public Safety Recruitment",
        "description": "Recruitment for civilian public safety, policing, fire and rescue, emergency response and related public protection services.",
        "authority_scope": "public_safety_authority",
        "role_families": ("police_services", "fire_and_rescue", "emergency_response", "forensic_support", "public_protection"),
        "source_expectation": "Official public safety department or authorized recruiting body notice.",
        "classification_caution": "Physical, medical, background and training requirements are notice-specific.",
    },
    {
        "id": "public_defence_civilian_recruitment",
        "name": "Defence Civilian Recruitment",
        "description": "Civilian employment in defence ministries, departments, laboratories, logistics, maintenance and support establishments.",
        "authority_scope": "defence_civilian",
        "role_families": ("engineering", "research", "administration", "logistics", "maintenance_and_support"),
        "source_expectation": "Official defence department, establishment or recruiting-body notice.",
        "classification_caution": "This track covers civilian employment only; military enlistment and commissioned service require separate controls.",
    },
    {
        "id": "public_research_recruitment",
        "name": "Public Research and Scientific Recruitment",
        "description": "Scientific, technical, research, laboratory and innovation roles in publicly funded research institutions and government laboratories.",
        "authority_scope": "public_research",
        "role_families": ("scientist", "research_fellow", "laboratory_technician", "engineering", "research_administration"),
        "source_expectation": "Official research institution, laboratory or public funding authority notice.",
        "classification_caution": "Research fellowships, grants and student stipends are not automatically employment relationships.",
    },
    {
        "id": "public_judiciary_and_legal_recruitment",
        "name": "Judiciary and Public Legal Recruitment",
        "description": "Judicial, court administration, prosecution, public legal service and related public-sector legal support recruitment.",
        "authority_scope": "judicial_or_legal_authority",
        "role_families": ("judicial_services", "court_administration", "prosecution", "government_legal_counsel", "legal_research"),
        "source_expectation": "Official court, judicial commission, prosecution authority or government legal department notice.",
        "classification_caution": "Bar admission, judicial eligibility and appointment rules are jurisdiction-specific.",
    },
    {
        "id": "public_finance_and_audit_recruitment",
        "name": "Public Finance and Audit Recruitment",
        "description": "Public treasury, taxation, accounting, audit, procurement finance and financial oversight roles in public authorities.",
        "authority_scope": "public_finance_authority",
        "role_families": ("accounts", "audit", "tax_administration", "treasury", "public_procurement_finance"),
        "source_expectation": "Official finance department, audit institution or authorized recruiting body notice.",
        "classification_caution": "Keep civil-service posts distinct from roles in state-owned banks and public enterprises.",
    },
    {
        "id": "public_infrastructure_and_engineering_recruitment",
        "name": "Public Infrastructure and Engineering Recruitment",
        "description": "Engineering, project delivery, maintenance, utilities and infrastructure roles employed by public works departments and public authorities.",
        "authority_scope": "public_infrastructure_authority",
        "role_families": ("civil_engineering", "electrical_engineering", "mechanical_engineering", "project_management", "asset_maintenance"),
        "source_expectation": "Official public works department, utility or infrastructure authority notice.",
        "classification_caution": "A contractor delivering a public project is not necessarily a government employer.",
    },
    {
        "id": "public_sector_enterprise_recruitment",
        "name": "Public Sector Enterprise Recruitment",
        "description": "Recruitment by state-owned or government-controlled enterprises and corporations under the applicable ownership and control definition.",
        "authority_scope": "state_owned_or_controlled_enterprise",
        "role_families": ("management_trainee", "engineering", "operations", "finance", "commercial_and_sales"),
        "source_expectation": "Official enterprise career portal or authorized recruitment notice.",
        "classification_caution": "Enterprise employment is not automatically civil-service employment; record the employer's legal identity.",
    },
)

def list_tracks() -> list[dict]:
    return [{**track, "role_families": tuple(track["role_families"])} for track in GOVERNMENT_JOB_TRACKS]

def get_track(track_id: str) -> dict | None:
    for track in GOVERNMENT_JOB_TRACKS:
        if track["id"] == track_id:
            return {**track, "role_families": tuple(track["role_families"])}
    return None

def validate_tracks() -> dict:
    ids = [track["id"] for track in GOVERNMENT_JOB_TRACKS]
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    incomplete = [
        track["id"] for track in GOVERNMENT_JOB_TRACKS
        if not all(track.get(field) for field in ("name", "description", "authority_scope", "role_families", "source_expectation", "classification_caution"))
    ]
    return {
        "category_id": CATEGORY_ID,
        "track_count": len(GOVERNMENT_JOB_TRACKS),
        "duplicate_track_ids": duplicates,
        "incomplete_tracks": incomplete,
        "structurally_valid": not duplicates and not incomplete,
        "taxonomy_only": True,
        "live_vacancies_verified": False,
    }


# Independent specialization folders are the source of truth for job-family packages.
# Merge their definitions into the category catalogue so every real folder is discoverable.
from importlib import import_module as _import_module
from pkgutil import iter_modules as _iter_modules

_declared_list_tracks = list_tracks

def list_tracks():
    records = {item["id"]: dict(item) for item in _declared_list_tracks()}
    package = _import_module(__package__)
    for child in _iter_modules(package.__path__):
        if not child.ispkg or child.name in {"tests", "__pycache__"}:
            continue
        try:
            definition = _import_module(f"{__package__}.{child.name}.categories")
        except (ImportError, ModuleNotFoundError):
            continue
        specialization_id = getattr(definition, "JOB_FAMILY_ID", child.name)
        specialization_name = getattr(definition, "JOB_FAMILY_NAME", specialization_id.replace("_", " ").title())
        if specialization_id not in records:
            role_examples = tuple(getattr(definition, "ROLE_EXAMPLES", ()))
            records[specialization_id] = {
                "id": specialization_id,
                "name": specialization_name,
                "description": getattr(definition, "DESCRIPTION", f"{specialization_name} job and work family."),
                "role_families": role_examples,
                "source": "independent_specialization_package",
            }
    return list(records.values())

def get_track(track_id):
    return next((item for item in list_tracks() if item["id"] == track_id), None)

def search_tracks(query):
    needle = query.strip().casefold()
    if not needle:
        return []
    return [item for item in list_tracks() if needle in item.get("id", "").casefold() or needle in item.get("name", "").casefold() or needle in item.get("description", "").casefold()]

def validate_tracks():
    records = list_tracks()
    ids = [item.get("id", "") for item in records]
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    incomplete = [item.get("id", "") for item in records if not item.get("id") or not item.get("name") or not item.get("description")]
    return {"category_id": CATEGORY_ID, "track_count": len(records), "duplicate_track_ids": duplicates, "incomplete_tracks": incomplete, "structurally_valid": bool(records) and not duplicates and not incomplete, "taxonomy_only": True, "live_vacancies_verified": False}
