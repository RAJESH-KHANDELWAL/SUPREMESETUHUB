from copy import deepcopy
from .constants import *
from .product_catalog import list_products,summary
from .domain_catalog import list_domains
def get_catalog():
 p=list_products();d=list_domains();return {"ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"provider":"NVIDIA","provider_id":PROVIDER_ID,"parent_id":PARENT_ID,"ecosystem_type":"PROVIDER_CORE","status":"CORE_CATALOG_ONLY","enabled":True,"capabilities":["PROVIDER_IDENTITY","PRODUCT_DISCOVERY","DOMAIN_TAXONOMY","CAPABILITY_METADATA","READINESS","POLICY","DEPENDENCY_DISCOVERY","TENANT_SECRET_REFERENCE_BOUNDARY"],"products":p,**summary(),"domains":d,"domain_count":len(d),"master_catalog":{"path":MASTER_PATH,"target_unique_entries":2468,"access_mode":"READ_ONLY_ON_DEMAND","canonical_entry_ids":["S09_artificial_intelligence","S09_machine_learning","S09_software","S09_cloud_computing","S09_data_analytics","S09_cybersecurity","S10_global_data_core","S10_global_security"],"catalog_entries_added":0},"api_catalog_ref":API_REF,"engine_ref":ENGINE_REF,"live_connection_verified":False,"api_calls_performed":0,"remote_operations_enabled":False}
def get_nvidia_core_catalog():return deepcopy(get_catalog())
