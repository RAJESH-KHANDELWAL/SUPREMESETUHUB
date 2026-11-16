"""Canonical Atlassian Core provider and family catalog."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ATLASSIAN_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": "ATLASSIAN-CORE-ECOSYSTEM",
    "name": "ATLASSIAN CORE ECOSYSTEM",
    "provider": "atlassian",
    "ecosystem_type": "PROVIDER_CORE",
    "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    "status": "REGISTERED",
    "enabled": True,
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem",
    "capabilities": ["ATLASSIAN_PROVIDER_REGISTRY", "PRODUCT_FAMILY_DISCOVERY", "TENANT_SCOPED_CAPABILITY_METADATA", "POLICY_AND_LIFECYCLE_METADATA"],
    "children": [
    {"ecosystem_id":"ATLASSIAN-ADMIN-IDENTITY-CORE-ECOSYSTEM","name":"ATLASSIAN ATLASSIAN ADMINISTRATION AND IDENTITY CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"ATLASSIAN-CORE-ECOSYSTEM","core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_admin_identity_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_admin_identity_api_ecosystem","capabilities":["ORGANIZATION_DIRECTORY_METADATA","USER_AND_GROUP_ADMINISTRATION_BOUNDARY","SCIM_PROVISIONING_METADATA","ACCESS_POLICY_METADATA"],"domains":["IDENTITY_AND_ORGANIZATION","GOVERNANCE_AND_SECURITY"],"status":"CORE_CATALOG_ONLY","connected":False,"live_connection_verified":False,"api_available":None},
    {"ecosystem_id":"ATLASSIAN-BITBUCKET-CORE-ECOSYSTEM","name":"ATLASSIAN BITBUCKET CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"ATLASSIAN-CORE-ECOSYSTEM","core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_bitbucket_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_bitbucket_api_ecosystem","capabilities":["REPOSITORY_METADATA","PULL_REQUEST_LIFECYCLE_BOUNDARY","PIPELINE_CONFIGURATION_METADATA","WORKSPACE_ACCESS_POLICY"],"domains":["DEVELOPER_AND_SOURCE_CONTROL","GOVERNANCE_AND_SECURITY"],"status":"CORE_CATALOG_ONLY","connected":False,"live_connection_verified":False,"api_available":None},
    {"ecosystem_id":"ATLASSIAN-CONFLUENCE-CORE-ECOSYSTEM","name":"ATLASSIAN CONFLUENCE CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"ATLASSIAN-CORE-ECOSYSTEM","core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_confluence_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_confluence_api_ecosystem","capabilities":["SPACE_METADATA","PAGE_LIFECYCLE_BOUNDARY","CONTENT_PERMISSION_METADATA","CONTENT_DISCOVERY_METADATA"],"domains":["KNOWLEDGE_AND_COLLABORATION","GOVERNANCE_AND_SECURITY"],"status":"CORE_CATALOG_ONLY","connected":False,"live_connection_verified":False,"api_available":None},
    {"ecosystem_id":"ATLASSIAN-JIRA-CORE-ECOSYSTEM","name":"ATLASSIAN JIRA CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"ATLASSIAN-CORE-ECOSYSTEM","core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_jira_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_jira_api_ecosystem","capabilities":["PROJECT_METADATA","ISSUE_LIFECYCLE_BOUNDARY","WORKFLOW_CONFIGURATION_METADATA","BOARD_AND_SPRINT_METADATA"],"domains":["WORK_MANAGEMENT_AND_PLANNING","DEVELOPER_AND_SOURCE_CONTROL"],"status":"CORE_CATALOG_ONLY","connected":False,"live_connection_verified":False,"api_available":None},
    {"ecosystem_id":"ATLASSIAN-JIRA-SERVICE-MANAGEMENT-CORE-ECOSYSTEM","name":"ATLASSIAN JIRA SERVICE MANAGEMENT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","parent_id":"ATLASSIAN-CORE-ECOSYSTEM","core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_jira_service_management_core_ecosystem","api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_jira_service_management_api_ecosystem","capabilities":["SERVICE_PROJECT_METADATA","REQUEST_AND_INCIDENT_LIFECYCLE_BOUNDARY","SERVICE_LEVEL_METADATA","ASSET_AND_CHANGE_GOVERNANCE_BOUNDARY"],"domains":["IT_SERVICE_AND_OPERATIONS","WORK_MANAGEMENT_AND_PLANNING"],"status":"CORE_CATALOG_ONLY","connected":False,"live_connection_verified":False,"api_available":None}
    ],
}

def get_atlassian_core_catalog() -> dict[str, Any]:
    return deepcopy(ATLASSIAN_CORE_ECOSYSTEM)

def list_atlassian_core_modules() -> list[dict[str, Any]]:
    return deepcopy(ATLASSIAN_CORE_ECOSYSTEM["children"])
