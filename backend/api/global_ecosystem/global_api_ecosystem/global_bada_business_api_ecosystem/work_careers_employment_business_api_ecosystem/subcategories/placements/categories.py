"""Job Placement Services tracks; service taxonomy, not vacancies."""
CATEGORY_ID="placements"
CATEGORY_NAME="Job Placement Services"
TRACKS=(
 {"id":"campus_placement_services","name":"Campus Placement Services","description":"Institutional placement-cell services connecting students or graduates with employers."},
 {"id":"graduate_placement_programmes","name":"Graduate Placement Programmes","description":"Structured programmes supporting graduate recruitment and placement."},
 {"id":"employment_agency_placements","name":"Employment Agency Placements","description":"Candidate-employer matching services provided by employment agencies."},
 {"id":"workforce_programme_placements","name":"Workforce Programme Placements","description":"Placement pathways connected to public, nonprofit or workforce-development programmes."},
 {"id":"professional_placement_services","name":"Professional Placement Services","description":"Placement services for experienced or specialist professionals."},
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
