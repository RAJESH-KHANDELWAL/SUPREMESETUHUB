"""Recruitment service tracks; these are not job vacancies."""
CATEGORY_ID="recruitment"
CATEGORY_NAME="Recruitment"
TRACKS=(
 {"id":"in_house_recruitment","name":"In-House Recruitment","description":"Employer-operated sourcing, assessment and selection by internal hiring teams."},
 {"id":"executive_search","name":"Executive Search","description":"Specialist search services for senior leadership roles; scope and fee terms should be explicit."},
 {"id":"contingent_recruitment","name":"Contingent Recruitment","description":"Recruitment services where fees are contingent on a defined hiring outcome, if contractually stated."},
 {"id":"retained_search","name":"Retained Search","description":"Search engagements with a retainer-based fee structure where contractually stated."},
 {"id":"technical_and_specialist_recruitment","name":"Technical and Specialist Recruitment","description":"Recruitment focused on technical, professional or specialist talent."},
)
def list_tracks(): return [dict(x) for x in TRACKS]
def get_track(track_id): return next((dict(x) for x in TRACKS if x["id"]==track_id),None)
def search_tracks(query):
 q=query.strip().casefold()
 return [dict(x) for x in TRACKS if q and (q in x["id"].casefold() or q in x["name"].casefold() or q in x["description"].casefold())]
def validate_tracks():
 ids=[x["id"] for x in TRACKS]; dup=sorted({x for x in ids if ids.count(x)>1})
 incomplete=[x["id"] for x in TRACKS if not x.get("name") or not x.get("description")]
 return {"category_id":CATEGORY_ID,"track_count":len(TRACKS),"duplicate_track_ids":dup,"incomplete_tracks":incomplete,"structurally_valid":not dup and not incomplete,"taxonomy_only":True,"live_vacancies_verified":False}


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
