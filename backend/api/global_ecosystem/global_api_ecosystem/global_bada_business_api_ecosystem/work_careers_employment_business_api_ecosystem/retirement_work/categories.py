"""Retirement-Age Work tracks; taxonomy only."""
CATEGORY_ID="retirement_work"
CATEGORY_NAME="Retirement-Age Work Opportunities"
TRACKS=(
 {"id":"phased_retirement_roles","name":"Phased-Retirement Roles","description":"Roles with a documented reduced-hours or staged transition arrangement."},
 {"id":"retired_professional_consulting","name":"Retired Professional Consulting","description":"Consulting engagements drawing on prior professional experience."},
 {"id":"part_time_experienced_roles","name":"Part-Time Experienced Roles","description":"Part-time roles requiring established experience or specialist skills."},
 {"id":"mentor_and_advisor_roles","name":"Mentor and Advisor Roles","description":"Mentoring and advisory opportunities with defined scope and engagement terms."},
 {"id":"flexible_expert_contracts","name":"Flexible Expert Contracts","description":"Flexible fixed-term or contract engagements for experienced specialists."},
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
