"""International Jobs tracks; taxonomy only, not a live vacancy feed."""
CATEGORY_ID = "international_jobs"
CATEGORY_NAME = "International Jobs"
TRACKS = (
    {"id": "overseas_employment", "name": "Overseas Employment", "description": "Employment where the worker is hired to work in a country other than their ordinary residence."},
    {"id": "international_organizations", "name": "International Organizations", "description": "Roles with intergovernmental and international organizations; employer status and duty station must be sourced."},
    {"id": "cross_border_remote_roles", "name": "Cross-Border Remote Roles", "description": "Remote roles with explicit cross-border hiring eligibility; work authorization and payroll country remain separate."},
    {"id": "expatriate_assignments", "name": "Expatriate Assignments", "description": "Employer-sponsored international assignments with assignment duration, host location and terms recorded."},
    {"id": "relocation_supported_roles", "name": "Relocation-Supported Roles", "description": "Roles where the employer explicitly describes relocation assistance; never infer visa sponsorship."},
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
