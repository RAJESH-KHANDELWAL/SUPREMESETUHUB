"""Temporary Jobs tracks; taxonomy only."""
CATEGORY_ID="temporary_jobs"
CATEGORY_NAME="Temporary Jobs"
TRACKS=(
 {"id":"short_term_temporary_roles","name":"Short-Term Temporary Roles","description":"Roles intended to cover a short and limited period."},
 {"id":"seasonal_temporary_roles","name":"Seasonal Temporary Roles","description":"Temporary roles linked to seasonal demand."},
 {"id":"temporary_replacement_roles","name":"Temporary Replacement Roles","description":"Temporary cover for leave, absence or a vacancy pending permanent recruitment."},
 {"id":"agency_temporary_roles","name":"Agency Temporary Roles","description":"Temporary workers supplied through an agency; agency and end client should be distinguished."},
 {"id":"event_temporary_roles","name":"Event-Based Temporary Roles","description":"Temporary roles for a defined event, exhibition, campaign or production."},
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
