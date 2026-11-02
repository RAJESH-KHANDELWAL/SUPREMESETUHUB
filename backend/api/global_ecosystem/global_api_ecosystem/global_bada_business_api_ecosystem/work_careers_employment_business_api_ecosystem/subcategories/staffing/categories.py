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
