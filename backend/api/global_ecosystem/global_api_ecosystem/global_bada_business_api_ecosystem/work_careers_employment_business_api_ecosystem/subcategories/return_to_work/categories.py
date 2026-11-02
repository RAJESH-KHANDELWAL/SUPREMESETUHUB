"""Return-to-Work Opportunities tracks; taxonomy only."""
CATEGORY_ID="return_to_work"
CATEGORY_NAME="Return-to-Work Opportunities"
TRACKS=(
 {"id":"returnship_programmes","name":"Returnship Programmes","description":"Structured employer programmes supporting professionals returning after a career break."},
 {"id":"career_reentry_roles","name":"Career Re-Entry Roles","description":"Roles explicitly open to applicants returning after time away from paid employment."},
 {"id":"flexible_reentry_jobs","name":"Flexible Re-Entry Jobs","description":"Return-to-work roles with stated flexible schedules or arrangements."},
 {"id":"refresher_and_retraining_pathways","name":"Refresher and Retraining Pathways","description":"Programmes offering documented refresher training or skills updates before or during re-entry."},
 {"id":"experienced_returner_roles","name":"Experienced Returner Roles","description":"Roles that value prior professional experience while allowing a career re-entry."},
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
