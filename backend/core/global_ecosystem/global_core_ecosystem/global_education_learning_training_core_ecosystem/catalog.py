from .domain_catalog import list_domains
CATALOG={"ecosystem_id":"GLOBAL-EDUCATION-LEARNING-TRAINING-CORE-ECOSYSTEM","name":"GLOBAL EDUCATION LEARNING TRAINING CORE ECOSYSTEM","version":"1.0.0","status":"REGISTERED","layer":"GLOBAL_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","domains":list_domains(),"capabilities":["EDUCATION_TAXONOMY","LEARNING_DISCOVERY","DELIVERY_MODE_CLASSIFICATION","QUALITY_METADATA"],"execution_enabled":False,"live_data_verified":False}
def get_catalog(): return {**CATALOG,"domains":[dict(x) for x in CATALOG["domains"]],"capabilities":list(CATALOG["capabilities"])}
