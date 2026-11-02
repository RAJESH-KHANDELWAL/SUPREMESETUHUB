"""Contract Jobs tracks; taxonomy only."""
CATEGORY_ID="contract_jobs"
CATEGORY_NAME="Contract Jobs"
TRACKS=(
 {"id":"fixed_term_employee_roles","name":"Fixed-Term Employee Roles","description":"Employment under a fixed-duration employment contract."},
 {"id":"independent_contractor_roles","name":"Independent Contractor Roles","description":"Services engagements where the worker is classified as an independent contractor by contract and applicable law."},
 {"id":"agency_contract_roles","name":"Agency Contract Roles","description":"Contract roles supplied through a staffing or employment agency; legal employer must be identified."},
 {"id":"project_based_contracts","name":"Project-Based Contracts","description":"Time-bounded engagements tied to defined project deliverables."},
 {"id":"consulting_contracts","name":"Consulting Contracts","description":"Professional consulting engagements with scope, deliverables and client terms recorded."},
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
