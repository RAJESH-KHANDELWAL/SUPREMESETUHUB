"""Canonical governance, compliance, standards and service/work taxonomy."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

DOMAIN_DEFINITIONS: dict[str, dict[str, Any]] = {
 "BUSINESS_GOVERNANCE": {"name":"Business Governance","purpose":"Accountability, decision rights, ownership, oversight, policies and controls.","capabilities":["OWNERSHIP_AND_ACCOUNTABILITY","BOARD_AND_EXECUTIVE_OVERSIGHT","POLICY_MANAGEMENT","RISK_MANAGEMENT","INTERNAL_CONTROLS","ETHICS_AND_CONFLICTS"],"namespace":"governance"},
 "BUSINESS_COMPLIANCE": {"name":"Business Compliance","purpose":"Obligation registers, regulatory evidence, licensing and compliance review metadata.","capabilities":["REGULATORY_OBLIGATIONS","LICENSING_AND_PERMITS","TAX_AND_STATUTORY_RECORDS","PRIVACY_AND_DATA_PROTECTION","LABOUR_AND_WORKPLACE","AML_AND_FINANCIAL_CONTROLS","AUDIT_AND_DISCLOSURES"],"namespace":"global_business_compliance_core_ecosystem"},
 "CLASSIFICATION_AND_STANDARDS": {"name":"Business Classification and Standards","purpose":"Industry/activity classifications, standards references, source versions and code crosswalks.","capabilities":["INDUSTRY_CLASSIFICATION","PRODUCT_AND_SERVICE_CLASSIFICATION","OCCUPATION_AND_WORK_CLASSIFICATION","STANDARDS_REFERENCES","JURISDICTION_CROSSWALKS"],"namespace":"global_classification_standards_business_core_ecosystem"},
 "GOVERNMENT_PUBLIC_SERVICES_AND_SOCIAL_IMPACT": {"name":"Government, Public Services and Social Impact","purpose":"Public procurement, public-service workflows, grants and social-impact programme metadata.","capabilities":["PUBLIC_PROCUREMENT_METADATA","PUBLIC_SERVICE_DELIVERY","PERMITS_AND_PUBLIC_APPLICATIONS","GRANTS_AND_SCHEMES","SOCIAL_IMPACT_AND_NONPROFIT"],"namespace":"government_public_services_social_impact"},
 "BUSINESS_SERVICES_AND_OPERATIONS": {"name":"Business Services and Operations","purpose":"B2B services, operating models, service catalogues, delivery and service levels.","capabilities":["BUSINESS_SERVICE_CATALOGUE","OPERATING_MODEL_METADATA","SERVICE_LEVEL_METADATA","CUSTOMER_AND_VENDOR_SERVICE_BOUNDARIES","PROCESS_AND_QUALITY_MANAGEMENT"],"namespace":None},
 "PROFESSIONAL_WORK_AND_ENGAGEMENTS": {"name":"Professional Work and Engagements","purpose":"Professional engagements, project/work packages, deliverables, roles and acceptance criteria.","capabilities":["PROFESSIONAL_ENGAGEMENT_METADATA","WORK_PACKAGE_CLASSIFICATION","DELIVERABLE_AND_ACCEPTANCE_METADATA","ROLE_AND_RESPONSIBILITY_METADATA","CONTRACT_AND_SCOPE_REFERENCES"],"namespace":None}
}
def list_domains() -> list[dict[str, Any]]:
    return [{"domain_id": key, **deepcopy(value)} for key, value in DOMAIN_DEFINITIONS.items()]
def get_domain(domain_id: str) -> dict[str, Any] | None:
    if not isinstance(domain_id, str): return None
    key = domain_id.strip().upper()
    value = DOMAIN_DEFINITIONS.get(key)
    return {"domain_id": key, **deepcopy(value)} if value else None
def list_capabilities() -> list[str]:
    return sorted({item for domain in DOMAIN_DEFINITIONS.values() for item in domain["capabilities"]})
