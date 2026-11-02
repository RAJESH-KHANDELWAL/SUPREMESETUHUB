"""Part-Time Jobs tracks; taxonomy only."""
CATEGORY_ID="part_time_jobs"
CATEGORY_NAME="Part-Time Jobs"
TRACKS=(
 {"id":"regular_part_time","name":"Regular Part-Time Jobs","description":"Roles with a recurring schedule below the employer's ordinary full-time schedule."},
 {"id":"student_part_time","name":"Student Part-Time Jobs","description":"Part-time roles suitable for students where eligibility and schedule are explicitly stated."},
 {"id":"weekend_part_time","name":"Weekend Part-Time Jobs","description":"Roles whose published schedule is primarily on weekends."},
 {"id":"evening_part_time","name":"Evening Part-Time Jobs","description":"Roles scheduled for evening hours as stated by the employer."},
 {"id":"flexible_hours_part_time","name":"Flexible-Hours Part-Time Jobs","description":"Part-time roles with employer-defined flexible scheduling."},
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
