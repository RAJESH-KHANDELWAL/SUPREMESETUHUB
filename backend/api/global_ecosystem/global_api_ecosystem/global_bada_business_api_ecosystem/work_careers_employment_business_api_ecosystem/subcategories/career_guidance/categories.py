"""Career Guidance service tracks; not job vacancies."""
CATEGORY_ID="career_guidance"
CATEGORY_NAME="Career Guidance"
TRACKS=(
 {"id":"career_counselling","name":"Career Counselling","description":"One-to-one or group career counselling services with provider qualifications stated where relevant."},
 {"id":"career_assessment","name":"Career Assessment","description":"Assessment services supporting career exploration; describe tools and limitations accurately."},
 {"id":"career_coaching","name":"Career Coaching","description":"Coaching services supporting career goals, planning and professional development."},
 {"id":"career_mentoring","name":"Career Mentoring","description":"Mentoring relationships connecting learners or professionals with experienced practitioners."},
 {"id":"education_and_career_planning","name":"Education and Career Planning","description":"Guidance connecting education choices, skills development and career pathways."},
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
