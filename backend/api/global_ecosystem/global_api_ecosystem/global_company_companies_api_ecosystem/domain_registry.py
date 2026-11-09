"""Company-specific domain registry; taxonomy metadata only."""
from .company_legal_entities_api_ecosystem.subcategories import SUBCATEGORY_IDS as COMPANY_SUBS
from .business_enterprises_api_ecosystem.subcategories import SUBCATEGORY_IDS as ENTERPRISE_SUBS
from .corporate_groups_api_ecosystem import DOMAIN_ID as GROUP_ID, DOMAIN_NAME as GROUP_NAME, SUBCATEGORY_IDS as GROUP_SUBS
_DEFINITIONS=(("company_legal_entities","Company Legal Entities",COMPANY_SUBS,"company"),("business_enterprises","Business Enterprises",ENTERPRISE_SUBS,"enterprise"),(GROUP_ID,GROUP_NAME,GROUP_SUBS,"corporate_group"))
DOMAIN_REGISTRY=tuple({"id":i,"name":n,"record_type":t,"subcategory_ids":tuple(s),"subcategory_count":len(s),"coverage_scope":("india","global"),"registry_status":"taxonomy_only"} for i,n,s,t in _DEFINITIONS)
def list_domains(): return [{**x,"subcategory_ids":list(x["subcategory_ids"]),"coverage_scope":list(x["coverage_scope"])} for x in DOMAIN_REGISTRY]
def get_domain(domain_id): return next((x for x in list_domains() if x["id"]==domain_id),None)
def search_domains(query):
 q=(query or "").strip().casefold()
 if not q:return []
 return [{"domain_id":x["id"],"domain_name":x["name"],"record_type":x["record_type"],"subcategory_id":s,"subcategory_name":s.replace("_"," ").title()} for x in DOMAIN_REGISTRY for s in x["subcategory_ids"] if q in x["id"].casefold() or q in x["name"].casefold() or q in s.casefold()]
def validate_domain_registry():
 ids=[x["id"] for x in DOMAIN_REGISTRY]; duplicates=sorted({x for x in ids if ids.count(x)>1}); empty=[x["id"] for x in DOMAIN_REGISTRY if not x["subcategory_ids"]]
 return {"structurally_valid":not duplicates and not empty,"domain_count":len(DOMAIN_REGISTRY),"subcategory_count":sum(x["subcategory_count"] for x in DOMAIN_REGISTRY),"duplicate_domain_ids":duplicates,"empty_domains":empty,"registry_status":"taxonomy_only","live_data_verified":False}
