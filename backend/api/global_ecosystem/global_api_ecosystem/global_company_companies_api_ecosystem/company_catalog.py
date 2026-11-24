"""Unified Company Companies catalogue with compatibility exports."""
from .company_legal_entities_api_ecosystem.catalog import CATEGORY, ENTITY_TYPES, SUBCATEGORIES
from .domain_registry import DOMAIN_REGISTRY, list_domains, get_domain, search_domains, validate_domain_registry
from .classification_registry import list_record_classes
def get_company_catalogue_metadata():
 return {"ecosystem":"GLOBAL COMPANY AND COMPANIES API","record_classes":list_record_classes(),"domains":len(DOMAIN_REGISTRY),"subcategory_count":sum(x["subcategory_count"] for x in DOMAIN_REGISTRY),"catalogue_status":"taxonomy_only","live_data_verified":False}
__all__=["CATEGORY","ENTITY_TYPES","SUBCATEGORIES","DOMAIN_REGISTRY","list_domains","get_domain","search_domains","validate_domain_registry","list_record_classes","get_company_catalogue_metadata"]
