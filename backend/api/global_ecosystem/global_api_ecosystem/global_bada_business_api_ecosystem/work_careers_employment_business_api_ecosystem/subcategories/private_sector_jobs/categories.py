"""Private Jobs employer tracks; taxonomy only, not live vacancies."""
CATEGORY_ID = "private_sector_jobs"
CATEGORY_NAME = "Private Jobs"
PRIVATE_JOB_TRACKS = (
    {"id":"private_companies","name":"Private Companies","description":"Jobs with privately owned incorporated companies and registered private businesses."},
    {"id":"small_and_medium_businesses","name":"Small and Medium Businesses","description":"Jobs with privately owned small and medium businesses; size labels need a documented jurisdictional standard."},
    {"id":"proprietorships","name":"Proprietorships","description":"Jobs with sole proprietorship businesses and individual business owners."},
    {"id":"partnership_firms","name":"Partnership Firms","description":"Jobs with privately owned partnership firms and partnership businesses."},
    {"id":"startups","name":"Startups","description":"Jobs with early-stage privately owned ventures; stage and funding claims must be sourced."},
    {"id":"family_owned_businesses","name":"Family-Owned Businesses","description":"Jobs with family-owned private businesses; family ownership is an employer attribute."},
    {"id":"private_professional_firms","name":"Private Professional Firms","description":"Jobs with privately owned professional and specialist service firms."},
    {"id":"private_retail_and_service_businesses","name":"Private Retail and Service Businesses","description":"Jobs with privately owned retail, hospitality, local service and customer-facing businesses."},
)
def list_tracks():
    return [dict(item) for item in PRIVATE_JOB_TRACKS]
def get_track(track_id):
    return next((dict(item) for item in PRIVATE_JOB_TRACKS if item["id"] == track_id), None)
def search_tracks(query):
    needle=query.strip().casefold()
    return [dict(item) for item in PRIVATE_JOB_TRACKS if needle and (needle in item["id"].casefold() or needle in item["name"].casefold() or needle in item["description"].casefold())]
def validate_tracks():
    ids=[item["id"] for item in PRIVATE_JOB_TRACKS]
    duplicates=sorted({item for item in ids if ids.count(item)>1})
    incomplete=[item["id"] for item in PRIVATE_JOB_TRACKS if not item.get("name") or not item.get("description")]
    return {"category_id":CATEGORY_ID,"track_count":len(PRIVATE_JOB_TRACKS),"duplicate_track_ids":duplicates,"incomplete_tracks":incomplete,"structurally_valid":not duplicates and not incomplete,"taxonomy_only":True,"live_vacancies_verified":False}
