"""Service-business classification vocabularies."""
from .domain_catalog import DOMAINS,list_domains,list_topics
SERVICE_MODELS=("CONSULTING","MANAGED_SERVICE","PROJECT_BASED","SUBSCRIPTION","TRANSACTIONAL","OUTSOURCING","SOFTWARE_ENABLED")
CLIENT_TYPES=("GOVERNMENT","PUBLIC_SECTOR_ENTERPRISE","PRIVATE_COMPANY","MSME_SME","STARTUP","NONPROFIT","EDUCATIONAL_INSTITUTION","HEALTHCARE_PROVIDER","INDIVIDUAL_CANDIDATE")
DELIVERY_MODES=("ON_SITE","REMOTE","HYBRID","DIGITAL","FIELD")
def get_catalog(): return {"ecosystem_id":"GLOBAL-GOVERNMENT-PRIVATE-JOBS-CAREERS-EMPLOYMENT-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM","domain_count":len(DOMAINS),"topic_count":len(list_topics()),"domains":list_domains(),"service_models":list(SERVICE_MODELS),"client_types":list(CLIENT_TYPES),"delivery_modes":list(DELIVERY_MODES),"live_services_verified":False}
