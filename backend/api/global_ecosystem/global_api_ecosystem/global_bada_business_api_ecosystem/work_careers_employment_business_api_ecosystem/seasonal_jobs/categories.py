"""Seasonal Jobs tracks; taxonomy only."""
CATEGORY_ID="seasonal_jobs"
CATEGORY_NAME="Seasonal Jobs"
TRACKS=(
 {"id":"agriculture_harvest_jobs","name":"Agriculture and Harvest Jobs","description":"Seasonal agricultural, crop, harvest and allied work."},
 {"id":"tourism_and_hospitality_seasonal","name":"Tourism and Hospitality Seasonal Jobs","description":"Seasonal roles driven by tourism, travel and hospitality demand."},
 {"id":"retail_festival_seasonal","name":"Retail and Festival Seasonal Jobs","description":"Retail, sales and support roles tied to festival or holiday periods."},
 {"id":"logistics_peak_seasonal","name":"Logistics Peak-Season Jobs","description":"Warehouse, delivery and logistics roles for documented peak periods."},
 {"id":"summer_and_winter_seasonal","name":"Summer and Winter Seasonal Jobs","description":"Roles tied to a stated summer, winter or other recurring season."},
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
