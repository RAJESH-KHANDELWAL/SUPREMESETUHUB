"""Recruitment service tracks; these are not job vacancies."""
CATEGORY_ID="recruitment"
CATEGORY_NAME="Recruitment"
TRACKS=(
 {"id":"in_house_recruitment","name":"In-House Recruitment","description":"Employer-operated sourcing, assessment and selection by internal hiring teams."},
 {"id":"executive_search","name":"Executive Search","description":"Specialist search services for senior leadership roles; scope and fee terms should be explicit."},
 {"id":"contingent_recruitment","name":"Contingent Recruitment","description":"Recruitment services where fees are contingent on a defined hiring outcome, if contractually stated."},
 {"id":"retained_search","name":"Retained Search","description":"Search engagements with a retainer-based fee structure where contractually stated."},
 {"id":"technical_and_specialist_recruitment","name":"Technical and Specialist Recruitment","description":"Recruitment focused on technical, professional or specialist talent."},
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
