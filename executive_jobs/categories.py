"""Executive Jobs tracks; taxonomy only."""
CATEGORY_ID="executive_jobs"
CATEGORY_NAME="Executive Jobs"
TRACKS=(
 {"id":"director_and_vp_roles","name":"Director and Vice-President Roles","description":"Senior functional or business-unit leadership roles with documented remit."},
 {"id":"c_suite_roles","name":"C-Suite Roles","description":"Chief executive, finance, technology, operating and other executive leadership roles."},
 {"id":"managing_director_roles","name":"Managing Director Roles","description":"Managing director positions with legal entity and governance responsibilities verified."},
 {"id":"board_and_non_executive_roles","name":"Board and Non-Executive Roles","description":"Board appointments and non-executive director roles; distinguish employment from governance appointments."},
 {"id":"business_unit_executive_roles","name":"Business-Unit Executive Roles","description":"Executive leadership of a defined business unit, region or operating division."},
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
