"""Shift Work tracks; taxonomy only."""
CATEGORY_ID="shift_work"
CATEGORY_NAME="Shift Work"
TRACKS=(
 {"id":"day_shift_jobs","name":"Day-Shift Jobs","description":"Roles scheduled primarily in daytime hours as published by the employer."},
 {"id":"evening_shift_jobs","name":"Evening-Shift Jobs","description":"Roles scheduled primarily in evening hours."},
 {"id":"night_shift_jobs","name":"Night-Shift Jobs","description":"Roles scheduled primarily overnight; record stated hours and applicable allowances."},
 {"id":"rotational_shift_jobs","name":"Rotational-Shift Jobs","description":"Roles rotating between two or more stated shifts."},
 {"id":"continuous_operations_shift_jobs","name":"Continuous-Operations Shift Jobs","description":"Roles supporting continuous or round-the-clock operations."},
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
