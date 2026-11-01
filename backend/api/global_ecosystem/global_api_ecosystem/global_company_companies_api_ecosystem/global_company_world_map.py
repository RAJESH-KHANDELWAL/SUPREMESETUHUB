"""Crosswalk between directory classes and their domain packages; not a live registry."""
GLOBAL_COMPANY_WORLD_MAP = (
 {"world_domain_id":"company-legal-entities","record_type":"company","module":"company_legal_entities_api_ecosystem","scope":"registered legal entities and formally constituted organizations"},
 {"world_domain_id":"business-enterprises","record_type":"business","module":"business_enterprises_api_ecosystem","scope":"operating businesses including MSMEs and startups"},
 {"world_domain_id":"independent-professionals","record_type":"freelancer","module":"freelancer_independent_professionals_api_ecosystem","scope":"independent professionals and individual service providers"},
)
def list_world_domains():
    return [dict(x) for x in GLOBAL_COMPANY_WORLD_MAP]
def get_world_domain(domain_id):
    return next((dict(x) for x in GLOBAL_COMPANY_WORLD_MAP if x["world_domain_id"] == domain_id), None)
