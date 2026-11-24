"""HTTP routes for the independent Global Organizations API ecosystem."""
from fastapi import APIRouter, HTTPException, Query
from .catalog import LEGAL_FORM_DIMENSIONS, GOVERNANCE_MODELS, GEOGRAPHIC_SCOPES, VERIFICATION_STATES
from .organization_domain_api_ecosystems.registry import ORGANIZATION_DOMAINS
from .organization_type_api_ecosystems.registry import ORGANIZATION_TYPES, ORGANIZATION_TYPE_GROUPS
from .schemas import OrganizationApiStatus, OrganizationListResponse
from .service import get_ecosystem_status, search_organizations, get_organization
from .country_api_ecosystems.registry import COUNTRY_ECOSYSTEM_STATUS
from .classification_standards_api_ecosystem.registry import CLASSIFICATION_STANDARDS_STATUS
from .integrations.catalog import INTEGRATION_CATALOG
from .services.catalog import ORGANIZATION_SERVICES
from .tools.catalog import ORGANIZATION_TOOLS

router = APIRouter(tags=["GLOBAL ORGANIZATIONS API ECOSYSTEM"])

@router.get("/global/organizations/status", response_model=OrganizationApiStatus)
def organization_status():
    return get_ecosystem_status()

@router.get("/global/organizations/architecture")
def organization_architecture():
    return {"success":True,"ecosystem":"GLOBAL ORGANIZATIONS API ECOSYSTEM","architecture_pattern":"independent_organization_directory_with_shared_relationships","canonical_entity":"organization","identity_dimensions":["organization_type","domain","legal_form","governance_model","geographic_scope","country","verification_status"],"profile_storage":"local_json_read_only","taxonomy_source":"curated_metadata","live_external_connections":False,"integration_contracts":{"company_companies":"Reference canonical company_id when an organization is also a registered company; do not duplicate its legal-company profile.","bada_business":"Use stable business category and industry crosswalk IDs where applicable; do not copy business catalogue records.","platforms":"Reference canonical platform IDs for platforms owned, operated, published, or used by an organization.","entity_relationships":"Store cross-ecosystem owns, operates, member_of, affiliated_with, funds, regulates, and similar edges in the shared relationship ecosystem; do not duplicate relationship storage."},"coverage_claim":"No complete worldwide coverage is claimed."}

@router.get("/global/organizations/domains")
def organization_domains():
    return {"success":True,"count":len(ORGANIZATION_DOMAINS),"domains":ORGANIZATION_DOMAINS}

@router.get("/global/organizations/types")
def organization_types():
    return {"success":True,"count":len(ORGANIZATION_TYPES),"groups":ORGANIZATION_TYPE_GROUPS,"types":ORGANIZATION_TYPES}

@router.get("/global/organizations/country-sources/status")
def organization_country_sources_status():
    return COUNTRY_ECOSYSTEM_STATUS

@router.get("/global/organizations/standards/status")
def organization_standards_status():
    return CLASSIFICATION_STANDARDS_STATUS

@router.get("/global/organizations/integrations")
def organization_integrations():
    return {"success":True,"count":len(INTEGRATION_CATALOG),"live_connections":False,"items":INTEGRATION_CATALOG}

@router.get("/global/organizations/services")
def organization_services():
    return {"success":True,"count":len(ORGANIZATION_SERVICES),"items":ORGANIZATION_SERVICES}

@router.get("/global/organizations/tools")
def organization_tools():
    return {"success":True,"count":len(ORGANIZATION_TOOLS),"items":ORGANIZATION_TOOLS}

@router.get("/global/organizations/classification")
def organization_classification():
    return {"organization_types":ORGANIZATION_TYPES,"organization_domains":ORGANIZATION_DOMAINS,"legal_form_dimensions":LEGAL_FORM_DIMENSIONS,"governance_models":GOVERNANCE_MODELS,"geographic_scopes":GEOGRAPHIC_SCOPES,"verification_states":VERIFICATION_STATES,"note":"Classification is descriptive metadata, not legal advice, registration validation, accreditation, or regulatory approval."}

def _search(q, domain, country, organization_type, verification_status, limit, offset):
    try:
        return search_organizations(q, domain, country, organization_type, verification_status, limit, offset)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.get("/global/organizations", response_model=OrganizationListResponse)
@router.get("/global/organizations/search", response_model=OrganizationListResponse)
def organization_search(q: str | None = Query(default=None), domain: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2), organization_type: str | None = Query(default=None), verification_status: str | None = Query(default=None), limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    return _search(q, domain, country, organization_type, verification_status, limit, offset)

@router.get("/global/organizations/{organization_id}")
def organization_details(organization_id: str):
    item = get_organization(organization_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {"success":True,"item":item}
