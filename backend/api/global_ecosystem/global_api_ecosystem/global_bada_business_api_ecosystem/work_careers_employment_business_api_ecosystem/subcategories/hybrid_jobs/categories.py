"""Hybrid Jobs tracks; taxonomy only."""
CATEGORY_ID="hybrid_jobs"
CATEGORY_NAME="Hybrid Jobs"
TRACKS=(
 {"id":"office_remote_hybrid","name":"Office and Remote Hybrid Jobs","description":"Roles combining employer-site attendance and remote work."},
 {"id":"field_office_hybrid","name":"Field and Office Hybrid Jobs","description":"Roles combining field visits with office-based duties."},
 {"id":"fixed_day_hybrid","name":"Fixed-Day Hybrid Jobs","description":"Roles with a stated recurring office-day schedule."},
 {"id":"flexible_hybrid","name":"Flexible Hybrid Jobs","description":"Roles where office attendance is flexible but still subject to employer policy."},
 {"id":"multi_location_hybrid","name":"Multi-Location Hybrid Jobs","description":"Roles involving more than one worksite plus remote work."},
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
