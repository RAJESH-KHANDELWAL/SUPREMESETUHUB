"""Corporate employer tracks; corporate structure is independent of ownership."""
CATEGORY_ID = "corporate_jobs"
CATEGORY_NAME = "Corporate Jobs"
CORPORATE_JOB_TRACKS = (
    {"id":"private_limited_companies","name":"Private Limited Companies","description":"Jobs with companies incorporated as private limited companies under applicable company law."},
    {"id":"public_listed_companies","name":"Public and Listed Companies","description":"Jobs with publicly held or stock-exchange-listed companies; listing status must be sourced."},
    {"id":"multinational_corporations","name":"Multinational Corporations","description":"Jobs with corporate groups operating in multiple countries; hiring legal entity and work country must be captured."},
    {"id":"corporate_groups","name":"Corporate Groups and Conglomerates","description":"Jobs with parent companies, subsidiaries, affiliates and diversified corporate groups; legal employer remains explicit."},
    {"id":"large_enterprises","name":"Large Corporate Enterprises","description":"Jobs with large organized enterprises; size classification requires a documented standard or source."},
    {"id":"corporate_head_offices","name":"Corporate Head Office Roles","description":"Central corporate functions such as finance, HR, legal, strategy, governance, compliance and administration."},
    {"id":"corporate_management","name":"Corporate Management and Leadership","description":"Management, director, executive and business-unit leadership roles in corporate organizations."},
    {"id":"government_owned_corporations","name":"Government-Owned Corporations","description":"Corporate-form employers owned or controlled by public authorities; ownership must remain classified as public-sector or state-owned."},
)
def list_tracks():
    return [dict(item) for item in CORPORATE_JOB_TRACKS]
def get_track(track_id):
    return next((dict(item) for item in CORPORATE_JOB_TRACKS if item["id"] == track_id), None)
def search_tracks(query):
    needle=query.strip().casefold()
    return [dict(item) for item in CORPORATE_JOB_TRACKS if needle and (needle in item["id"].casefold() or needle in item["name"].casefold() or needle in item["description"].casefold())]
def validate_tracks():
    ids=[item["id"] for item in CORPORATE_JOB_TRACKS]
    duplicates=sorted({item for item in ids if ids.count(item)>1})
    incomplete=[item["id"] for item in CORPORATE_JOB_TRACKS if not item.get("name") or not item.get("description")]
    return {"category_id":CATEGORY_ID,"track_count":len(CORPORATE_JOB_TRACKS),"duplicate_track_ids":duplicates,"incomplete_tracks":incomplete,"structurally_valid":not duplicates and not incomplete,"taxonomy_only":True,"live_vacancies_verified":False}


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
