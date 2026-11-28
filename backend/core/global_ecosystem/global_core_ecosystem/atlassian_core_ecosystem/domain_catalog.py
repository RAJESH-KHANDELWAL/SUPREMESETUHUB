"""Atlassian Core domain taxonomy, package routing and offering inventory."""
from __future__ import annotations
from typing import Any
from .product_catalog import list_atlassian_offerings
DOMAIN_DEFINITIONS={
 "PROVIDER_GOVERNANCE":{"name":"Provider Governance","purpose":"Provider registry, product lifecycle, catalog ownership, discovery and readiness.","package":"atlassian_provider_governance_core_ecosystem"},
 "IDENTITY_AND_ORGANIZATION":{"name":"Identity and Organization","purpose":"Organization administration, identity, users, groups, access and provisioning metadata.","package":"atlassian_identity_and_organization_core_ecosystem"},
 "DEVELOPER_AND_SOURCE_CONTROL":{"name":"Developer and Source Control","purpose":"Bitbucket repositories, branches, pull requests, pipelines and developer workflow metadata.","package":"atlassian_developer_and_source_control_core_ecosystem"},
 "KNOWLEDGE_AND_COLLABORATION":{"name":"Knowledge and Collaboration","purpose":"Confluence spaces, pages, content discovery, permissions and collaboration metadata.","package":"atlassian_knowledge_and_collaboration_core_ecosystem"},
 "WORK_MANAGEMENT_AND_PLANNING":{"name":"Work Management and Planning","purpose":"Jira projects, issues, boards, sprints, workflows and planning metadata.","package":"atlassian_work_management_and_planning_core_ecosystem"},
 "IT_SERVICE_AND_OPERATIONS":{"name":"IT Service and Operations","purpose":"Jira Service Management service projects, requests, incidents, changes, assets and SLAs.","package":"atlassian_it_service_and_operations_core_ecosystem"},
 "GOVERNANCE_AND_SECURITY":{"name":"Governance and Security","purpose":"Cross-product access, audit, policy, compliance and security capability metadata.","package":"atlassian_governance_and_security_core_ecosystem"},
 "INTEGRATION_AND_AUTOMATION":{"name":"Integration and Automation","purpose":"Cross-product automation, webhooks, integrations, delivery coordination and orchestration metadata.","package":"atlassian_integration_and_automation_core_ecosystem"},
}
DOMAINS=[{"domain_id":key,**value} for key,value in DOMAIN_DEFINITIONS.items()]
DOMAIN_FAMILY_MAP={"ADMIN-IDENTITY":["PROVIDER_GOVERNANCE","IDENTITY_AND_ORGANIZATION","GOVERNANCE_AND_SECURITY"],"BITBUCKET":["PROVIDER_GOVERNANCE","DEVELOPER_AND_SOURCE_CONTROL","GOVERNANCE_AND_SECURITY","INTEGRATION_AND_AUTOMATION"],"CONFLUENCE":["PROVIDER_GOVERNANCE","KNOWLEDGE_AND_COLLABORATION","GOVERNANCE_AND_SECURITY"],"JIRA":["PROVIDER_GOVERNANCE","WORK_MANAGEMENT_AND_PLANNING","DEVELOPER_AND_SOURCE_CONTROL","INTEGRATION_AND_AUTOMATION"],"JIRA-SERVICE-MANAGEMENT":["PROVIDER_GOVERNANCE","IT_SERVICE_AND_OPERATIONS","WORK_MANAGEMENT_AND_PLANNING","GOVERNANCE_AND_SECURITY","INTEGRATION_AND_AUTOMATION"]}
def list_atlassian_domain_inventory()->list[dict[str,Any]]:
 results=[]
 for item in list_atlassian_offerings():
  for domain_id in DOMAIN_FAMILY_MAP.get(item["family"],[]): results.append({**item,"core_domain_id":domain_id})
 return results
def atlassian_domain_summary()->dict[str,Any]:
 offerings=list_atlassian_offerings(); inventory=list_atlassian_domain_inventory()
 domains=[{**definition,"offering_count":len({item["id"] for item in inventory if item["core_domain_id"]==domain_id})} for domain_id,definition in DOMAIN_DEFINITIONS.items()]
 return {"success":True,"domain_count":len(domains),"offering_count":len(offerings),"live_connections_verified":0,"domains":domains}
__all__=["DOMAIN_DEFINITIONS","DOMAINS","DOMAIN_FAMILY_MAP","list_atlassian_domain_inventory","atlassian_domain_summary"]
