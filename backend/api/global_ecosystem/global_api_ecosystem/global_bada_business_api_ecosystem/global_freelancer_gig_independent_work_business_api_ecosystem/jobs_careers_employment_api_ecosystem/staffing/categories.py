"""Staffing Services tracks; service taxonomy, not job vacancies."""
CATEGORY_ID="staffing"
CATEGORY_NAME="Staffing Services"
TRACKS=(
 {"id":"temporary_staffing","name":"Temporary Staffing","description":"Supply of temporary workers for time-limited workforce needs."},
 {"id":"contract_staffing","name":"Contract Staffing","description":"Supply or administration of contract workers; legal employer and end client must be distinguished."},
 {"id":"permanent_staffing","name":"Permanent Staffing","description":"Workforce sourcing and staffing services for ongoing employment positions."},
 {"id":"managed_workforce_services","name":"Managed Workforce Services","description":"Managed services for workforce planning, supply or administration under defined service terms."},
 {"id":"employer_of_record_services","name":"Employer-of-Record Services","description":"Services where a provider acts as legal employer in a jurisdiction, subject to local law and verified contractual arrangements."},
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
