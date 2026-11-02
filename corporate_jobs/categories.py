"""Corporate employer tracks; corporate structure is independent of ownership."""
CATEGORY_ID = "corporate_jobs"
CATEGORY_NAME = "Corporate Jobs"
CORPORATE_JOB_TRACKS = (
    {"id":"private_limited_companies","name":"Private Limited Companies","description":"Jobs with companies incorporated as private limited companies under applicable company law."},
    {"id":"public_listed_companies","name":"Public and Listed Companies","description":"Jobs with publicly held or stock-exchange-listed companies; listing status must be sourced."},
    {"id":"multinational_corporations","name":"Multinational Corporations","description":"Jobs with corporate groups operating in multiple countries; hiring legal entity and work country must be captured."},
    {"id":"corporate_groups","name":"Corporate Groups and Conglomerates","description":"Jobs with parent companies, subsidiaries, affiliates and diversified corporate groups; legal employer remains explicit."},
    {"id":"large_enterprises","name":"Large Corporate Enterprises","description":"Jobs with large organized enterprises; size classification requires a documented standard or source."},
    {"id":"corporate_head_offices","name":"Corporate Head Office Roles","description":"Central corporate functions such as finance, HR, legal, strategy, governance, compliance and administration."},
    {"id":"corporate_management","name":"Corporate Management and Leadership","description":"Management, director, executive and business-unit leadership roles in corporate organizations."},
    {"id":"government_owned_corporations","name":"Government-Owned Corporations","description":"Corporate-form employers owned or controlled by public authorities; ownership must remain classified as public-sector or state-owned."},
)
def list_tracks():
    return [dict(item) for item in CORPORATE_JOB_TRACKS]
def get_track(track_id):
    return next((dict(item) for item in CORPORATE_JOB_TRACKS if item["id"] == track_id), None)
def search_tracks(query):
    needle=query.strip().casefold()
    return [dict(item) for item in CORPORATE_JOB_TRACKS if needle and (needle in item["id"].casefold() or needle in item["name"].casefold() or needle in item["description"].casefold())]
def validate_tracks():
    ids=[item["id"] for item in CORPORATE_JOB_TRACKS]
    duplicates=sorted({item for item in ids if ids.count(item)>1})
    incomplete=[item["id"] for item in CORPORATE_JOB_TRACKS if not item.get("name") or not item.get("description")]
    return {"category_id":CATEGORY_ID,"track_count":len(CORPORATE_JOB_TRACKS),"duplicate_track_ids":duplicates,"incomplete_tracks":incomplete,"structurally_valid":not duplicates and not incomplete,"taxonomy_only":True,"live_vacancies_verified":False}
