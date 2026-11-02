"""Full-Time Jobs tracks; taxonomy only."""
CATEGORY_ID="full_time_jobs"
CATEGORY_NAME="Full-Time Jobs"
TRACKS=(
 {"id":"permanent_full_time","name":"Permanent Full-Time Jobs","description":"Ongoing full-time employment, subject to the employer's stated terms and applicable law."},
 {"id":"fixed_term_full_time","name":"Fixed-Term Full-Time Jobs","description":"Full-time employment for a stated or contractually bounded term."},
 {"id":"graduate_full_time","name":"Graduate Full-Time Jobs","description":"Full-time roles explicitly designed for graduates or early-career applicants."},
 {"id":"professional_full_time","name":"Professional Full-Time Jobs","description":"Full-time roles requiring professional skills or prior experience."},
 {"id":"operations_full_time","name":"Operations Full-Time Jobs","description":"Full-time roles in operations, delivery, production and service functions."},
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
