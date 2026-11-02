"""Entry-Level Jobs tracks; taxonomy only."""
CATEGORY_ID="entry_level_jobs"
CATEGORY_NAME="Entry-Level Jobs"
TRACKS=(
 {"id":"fresher_jobs","name":"Fresher Jobs","description":"Roles open to applicants with limited or no prior relevant work experience where explicitly stated."},
 {"id":"graduate_trainee_jobs","name":"Graduate Trainee Jobs","description":"Structured trainee roles for recent graduates."},
 {"id":"apprenticeships","name":"Apprenticeships","description":"Formal apprenticeship pathways; preserve programme rules and jurisdiction-specific status."},
 {"id":"internships","name":"Internships","description":"Time-limited supervised work experience or learning placements."},
 {"id":"junior_associate_jobs","name":"Junior Associate Jobs","description":"Junior roles with limited experience requirements stated by the employer."},
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
