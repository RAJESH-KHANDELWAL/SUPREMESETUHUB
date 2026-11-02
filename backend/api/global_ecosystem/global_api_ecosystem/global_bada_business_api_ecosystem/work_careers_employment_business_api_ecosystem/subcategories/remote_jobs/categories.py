"""Remote Jobs tracks; taxonomy only, not a live vacancy feed."""
CATEGORY_ID = "remote_jobs"
CATEGORY_NAME = "Remote Jobs"
TRACKS = (
    {"id":"fully_remote_jobs","name":"Fully Remote Jobs","description":"Roles explicitly described as fully remote without routine office attendance."},
    {"id":"remote_first_companies","name":"Remote-First Companies","description":"Roles at organizations whose operating model is remote-first; verify policy from employer sources."},
    {"id":"work_from_home_jobs","name":"Work-from-Home Jobs","description":"Roles explicitly allowing work from the worker's home location."},
    {"id":"distributed_team_roles","name":"Distributed-Team Roles","description":"Roles in teams distributed across locations and time zones."},
    {"id":"location_restricted_remote_jobs","name":"Location-Restricted Remote Jobs","description":"Remote roles limited to specified countries, states or regions."},
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
