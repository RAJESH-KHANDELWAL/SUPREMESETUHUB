from .domain_catalog import list_domains,get_domain,search_domains,validate_domains
def status(): return {"status":"CATALOG_READY","domain_count":len(list_domains()),"integrity":validate_domains()["valid"],"mode":"METADATA_ONLY"}
