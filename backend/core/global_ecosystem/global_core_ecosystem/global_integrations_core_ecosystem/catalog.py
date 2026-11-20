"""Canonical provider-neutral integrations catalog; metadata only."""
from .constants import ECOSYSTEM_ID, MASTER_CATALOG_REF, STATUS
from .models import IntegrationDescriptor, ProviderDescriptor
from .registry import INTEGRATION_DOMAIN_ROWS, PROVIDER_ROWS
INTEGRATION_CATALOG=tuple(IntegrationDescriptor(
    integration_id=r["id"],display_name=r["name"],domain_id=r["id"],folder=r["folder"],
    category=r["category"],capabilities=tuple(r["capabilities"]),sensitivity=r["sensitivity"],
    age_restricted=r["age_restricted"],consent_required=r["consent_required"],status=STATUS
) for r in INTEGRATION_DOMAIN_ROWS)
PROVIDER_CATALOG=tuple(ProviderDescriptor(r["id"],r["name"],r["category"]) for r in PROVIDER_ROWS)
def get_integrations_catalog():
    return [x.to_dict() for x in INTEGRATION_CATALOG]
def get_integration(integration_id:str):
    q=integration_id.strip().casefold()
    if not q:return None
    return next((x.to_dict() for x in INTEGRATION_CATALOG if q in (x.integration_id.casefold(),x.display_name.casefold())),None)
def get_provider_catalog():
    return [x.to_dict() for x in PROVIDER_CATALOG]
def get_provider(provider_id:str):
    q=provider_id.strip().casefold()
    if not q:return None
    return next((x.to_dict() for x in PROVIDER_CATALOG if q in (x.provider_id.casefold(),x.display_name.casefold())),None)
def search_catalog(query:str):
    q=query.strip().casefold()
    if not q:return []
    return [x for x in get_integrations_catalog() if q in x["integration_id"].casefold() or q in x["display_name"].casefold() or q in x["category"].casefold() or any(q in c.casefold() for c in x["capabilities"])]
def get_catalog():
    domains,providers=get_integrations_catalog(),get_provider_catalog()
    return {"ecosystem_id":ECOSYSTEM_ID,"status":STATUS,"source_of_truth":MASTER_CATALOG_REF,
      "master_catalog_policy":MASTER_CATALOG_POLICY,"integration_domain_count":len(domains),
      "provider_family_count":len(providers),"integration_domains":domains,"provider_families":providers,
      "live_connections_verified":0,"api_calls_performed":0,"execution_enabled":False}
