"""Public Sector Jobs tracks; taxonomy only, not a live vacancy feed."""
CATEGORY_ID = "public_sector_jobs"
CATEGORY_NAME = "Public Sector Jobs"
TRACKS = (
    {"id": "central_public_sector_enterprises", "name": "Central Public Sector Enterprises", "description": "Central-government-owned or controlled commercial and industrial enterprises; ownership and control evidence must be recorded."},
    {"id": "state_public_sector_enterprises", "name": "State Public Sector Enterprises", "description": "State-government-owned or controlled enterprises, classified by the relevant state and ownership basis."},
    {"id": "public_sector_banking", "name": "Public Sector Banking", "description": "Roles with government-owned or controlled banks; bank ownership and legal employer must be verified."},
    {"id": "public_sector_insurance", "name": "Public Sector Insurance", "description": "Roles with public-sector insurance companies and institutions; distinguish statutory bodies from companies."},
    {"id": "government_owned_corporations", "name": "Government-Owned Corporations", "description": "Incorporated entities owned or controlled by government; may overlap with Corporate Jobs."},
    {"id": "public_utilities_and_infrastructure", "name": "Public Utilities and Infrastructure", "description": "Employment in public utilities and infrastructure operators, with ownership and regulatory status captured."},
    {"id": "public_education_and_research_institutions", "name": "Public Education and Research Institutions", "description": "Roles with public universities, publicly funded research bodies and education institutions."},
    {"id": "public_health_institutions", "name": "Public Health Institutions", "description": "Roles with government-owned hospitals, health authorities and public healthcare institutions."},
)
def list_tracks(): return [dict(x) for x in TRACKS]
def get_track(track_id): return next((dict(x) for x in TRACKS if x["id"] == track_id), None)
def search_tracks(query):
    q=query.strip().casefold()
    return [dict(x) for x in TRACKS if q and (q in x["id"].casefold() or q in x["name"].casefold() or q in x["description"].casefold())]
def validate_tracks():
    ids=[x["id"] for x in TRACKS]
    dup=sorted({x for x in ids if ids.count(x)>1})
    incomplete=[x["id"] for x in TRACKS if not x.get("name") or not x.get("description")]
    return {"category_id":CATEGORY_ID,"track_count":len(TRACKS),"duplicate_track_ids":dup,"incomplete_tracks":incomplete,"structurally_valid":not dup and not incomplete,"taxonomy_only":True,"live_vacancies_verified":False}
