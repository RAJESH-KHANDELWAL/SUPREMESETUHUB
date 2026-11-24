from .domain_catalog import list_domains,get_domain,search_domains,validate_mappings
def status(): return {"status":"CATALOG_READY","business_domain_count":len(list_domains()),"mapping_integrity":validate_mappings()["valid"],"mode":"CLASSIFICATION_ONLY"}
def classify(domain_id,service_type):
 item=get_domain(domain_id)
 if item is None: return {"valid":False,"reason":"UNKNOWN_BUSINESS_DOMAIN"}
 kind=service_type.strip().upper()
 if kind not in {"SERVICE","WORK","BUSINESS","PROJECT","PRODUCT","ADVISORY","EMPLOYMENT"}: return {"valid":False,"reason":"UNSUPPORTED_SERVICE_TYPE"}
 return {"valid":True,"business_domain":item,"service_type":kind,"execution_enabled":False}
