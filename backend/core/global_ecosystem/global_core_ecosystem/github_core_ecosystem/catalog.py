"""Canonical GitHub CORE registry; catalog metadata only."""
from copy import deepcopy
_CATALOG={"ecosystem_id":"GITHUB-CORE-ECOSYSTEM","name":"GITHUB CORE ECOSYSTEM","provider":"github","ecosystem_type":"PROVIDER_CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","status":"REGISTERED","enabled":True,"api_catalog_ref":"backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem","api_transport_ref":"backend/integration/provider/github.py","api_routes_ref":"backend/api/connectors.py","capabilities":["PROVIDER_REGISTRY","FAMILY_DISCOVERY","TENANT_CONTEXT_CONTRACT","CAPABILITY_POLICY_METADATA","LIFECYCLE_METADATA","READINESS_AND_HEALTH","CROSS_FAMILY_ORCHESTRATION"],"children":[
  {
    "ecosystem_id": "GITHUB-ACTIONS-CORE-ECOSYSTEM",
    "family": "actions",
    "name": "GITHUB ACTIONS CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_actions_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_actions_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "ACTIONS_DISCOVERY",
      "ACTIONS_METADATA",
      "ACTIONS_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-APPS-CORE-ECOSYSTEM",
    "family": "apps",
    "name": "GITHUB APPS CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_apps_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_apps_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "APPS_DISCOVERY",
      "APPS_METADATA",
      "APPS_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-AUTHENTICATION-CORE-ECOSYSTEM",
    "family": "authentication",
    "name": "GITHUB AUTHENTICATION CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_authentication_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_authentication_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "AUTHENTICATION_DISCOVERY",
      "AUTHENTICATION_METADATA",
      "AUTHENTICATION_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": True,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-CHECKS-CORE-ECOSYSTEM",
    "family": "checks",
    "name": "GITHUB CHECKS CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_checks_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_checks_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "CHECKS_DISCOVERY",
      "CHECKS_METADATA",
      "CHECKS_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-GRAPHQL-CORE-ECOSYSTEM",
    "family": "graphql",
    "name": "GITHUB GRAPHQL CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_graphql_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_graphql_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "GRAPHQL_DISCOVERY",
      "GRAPHQL_METADATA",
      "GRAPHQL_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-ISSUES-CORE-ECOSYSTEM",
    "family": "issues",
    "name": "GITHUB ISSUES CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_issues_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_issues_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "ISSUES_DISCOVERY",
      "ISSUES_METADATA",
      "ISSUES_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-ORGANIZATIONS-CORE-ECOSYSTEM",
    "family": "organizations",
    "name": "GITHUB ORGANIZATIONS CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_organizations_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_organizations_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "ORGANIZATIONS_DISCOVERY",
      "ORGANIZATIONS_METADATA",
      "ORGANIZATIONS_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-PULL_REQUESTS-CORE-ECOSYSTEM",
    "family": "pull_requests",
    "name": "GITHUB PULL REQUESTS CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_pull_requests_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_pull_requests_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "PULL_REQUESTS_DISCOVERY",
      "PULL_REQUESTS_METADATA",
      "PULL_REQUESTS_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-REPOSITORIES-CORE-ECOSYSTEM",
    "family": "repositories",
    "name": "GITHUB REPOSITORIES CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_repositories_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_repositories_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "REPOSITORIES_DISCOVERY",
      "REPOSITORIES_METADATA",
      "REPOSITORIES_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": True,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-REST-CORE-ECOSYSTEM",
    "family": "rest",
    "name": "GITHUB REST CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_rest_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_rest_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "REST_DISCOVERY",
      "REST_METADATA",
      "REST_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-SECURITY-CORE-ECOSYSTEM",
    "family": "security",
    "name": "GITHUB SECURITY CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_security_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_security_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "SECURITY_DISCOVERY",
      "SECURITY_METADATA",
      "SECURITY_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  },
  {
    "ecosystem_id": "GITHUB-WEBHOOKS-CORE-ECOSYSTEM",
    "family": "webhooks",
    "name": "GITHUB WEBHOOKS CORE ECOSYSTEM",
    "core_module": "backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/github_webhooks_core_ecosystem",
    "api_catalog_ref": "backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_webhooks_api_ecosystem",
    "shared_api_transport_ref": "backend/integration/provider/github.py",
    "capabilities": [
      "WEBHOOKS_DISCOVERY",
      "WEBHOOKS_METADATA",
      "WEBHOOKS_LIFECYCLE"
    ],
    "status": "CORE_CATALOG_ONLY",
    "family_api_routes_implemented": False,
    "live_connection_verified": False
  }
]}
def get_github_core_catalog(): return deepcopy(_CATALOG)
def list_github_families(): return deepcopy(_CATALOG["children"])
