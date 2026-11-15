"""Company-data provider directory; no live adapters are implied."""
from .registry import PROVIDER_ECOSYSTEM_STATUS
PROVIDER_CATALOG=(
{"provider_id":"apple","name":"Apple","provider_type":"technology_company","data_scope":"public_company_information","adapter_status":"not_connected"},
{"provider_id":"aws","name":"Amazon Web Services","provider_type":"cloud_platform","data_scope":"infrastructure_not_company_registry","adapter_status":"not_connected"},
{"provider_id":"google","name":"Google","provider_type":"technology_company","data_scope":"public_company_information","adapter_status":"not_connected"},
{"provider_id":"microsoft","name":"Microsoft","provider_type":"technology_company","data_scope":"public_company_information","adapter_status":"not_connected"})
def list_providers(): return [dict(x) for x in PROVIDER_CATALOG]
def get_provider(provider_id):
 key=(provider_id or "").strip().casefold()
 return next((dict(x) for x in PROVIDER_CATALOG if x["provider_id"]==key),None)
def get_provider_status():
 return {**PROVIDER_ECOSYSTEM_STATUS,"provider_count":len(PROVIDER_CATALOG),"adapter_count":0,"live_company_data_connected":False}
