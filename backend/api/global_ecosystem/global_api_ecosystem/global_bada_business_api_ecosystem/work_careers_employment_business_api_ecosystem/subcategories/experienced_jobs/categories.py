"""Experienced Professional Jobs tracks; taxonomy only."""
CATEGORY_ID="experienced_jobs"
CATEGORY_NAME="Experienced Professional Jobs"
TRACKS=(
 {"id":"mid_level_professional_roles","name":"Mid-Level Professional Roles","description":"Roles requiring established professional experience and independent delivery."},
 {"id":"senior_specialist_roles","name":"Senior Specialist Roles","description":"Roles requiring deep specialist expertise and a demonstrated track record."},
 {"id":"technical_expert_roles","name":"Technical Expert Roles","description":"Experienced technical roles with defined domain expertise and responsibility."},
 {"id":"team_lead_roles","name":"Team Lead Roles","description":"Roles with responsibility for coordinating or supervising a team."},
 {"id":"career_progression_roles","name":"Career Progression Roles","description":"Experienced roles representing a documented step up in scope or responsibility."},
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
