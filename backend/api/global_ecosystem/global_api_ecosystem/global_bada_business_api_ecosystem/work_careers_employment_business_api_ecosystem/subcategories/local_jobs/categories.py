"""Local Jobs tracks; taxonomy only, not a live vacancy feed."""
CATEGORY_ID = "local_jobs"
CATEGORY_NAME = "Local Jobs"
TRACKS = (
    {"id": "city_jobs", "name": "City Jobs", "description": "Roles located within a named city and its defined commuting area."},
    {"id": "district_jobs", "name": "District Jobs", "description": "Roles located within a named administrative district."},
    {"id": "neighborhood_jobs", "name": "Neighborhood Jobs", "description": "Roles tied to a specific neighborhood or local service area."},
    {"id": "rural_and_village_jobs", "name": "Rural and Village Jobs", "description": "Roles based in rural areas and villages, with normalized locality data."},
    {"id": "commuting_area_jobs", "name": "Commuting-Area Jobs", "description": "Roles within a documented commuting region; do not infer travel time without route data."},
)
def list_tracks(): return [dict(x) for x in TRACKS]
def get_track(track_id): return next((dict(x) for x in TRACKS if x["id"] == track_id), None)
def search_tracks(query):
    q=query.strip().casefold()
    return [dict(x) for x in TRACKS if q and (q in x["id"].casefold() or q in x["name"].casefold() or q in x["description"].casefold())]
def validate_tracks():
    ids=[x["id"] for x in TRACKS]
    dup=sorted({x for x in ids if ids.count(x)>1})
    incomplete=[x["id"] for x in TRACKS if not x.get("name") or not x.get("description")]
    return {"category_id":CATEGORY_ID,"track_count":len(TRACKS),"duplicate_track_ids":dup,"incomplete_tracks":incomplete,"structurally_valid":not dup and not incomplete,"taxonomy_only":True,"live_vacancies_verified":False}
