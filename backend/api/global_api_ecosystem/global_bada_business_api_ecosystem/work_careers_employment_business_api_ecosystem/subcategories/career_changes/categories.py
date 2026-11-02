"""Career Change Opportunities tracks; taxonomy only."""
CATEGORY_ID="career_changes"
CATEGORY_NAME="Career Change Opportunities"
TRACKS=(
 {"id":"industry_transition_jobs","name":"Industry Transition Jobs","description":"Roles supporting a move between industries with transferable skills."},
 {"id":"occupation_change_pathways","name":"Occupation Change Pathways","description":"Structured pathways into a different occupation, including documented retraining requirements."},
 {"id":"reskilling_and_upskilling_roles","name":"Reskilling and Upskilling Opportunities","description":"Roles or programmes linked to explicitly stated reskilling or upskilling."},
 {"id":"second_career_opportunities","name":"Second-Career Opportunities","description":"Employment pathways for people pursuing a new professional direction."},
 {"id":"career_pivot_entry_roles","name":"Career-Pivot Entry Roles","description":"Entry routes into a new field where prior transferable experience may be relevant."},
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
