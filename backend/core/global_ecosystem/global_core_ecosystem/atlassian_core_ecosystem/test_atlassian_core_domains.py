"""Structural and behavioral tests for Atlassian Core domain and package managers."""
import importlib
import re
from pathlib import Path
from .domain_catalog import DOMAIN_DEFINITIONS,atlassian_domain_summary
from .domain_runtime import AtlassianCoreDomainManager
DOMAIN_PACKAGES={
 "PROVIDER_GOVERNANCE":"atlassian_provider_governance_core_ecosystem",
 "IDENTITY_AND_ORGANIZATION":"atlassian_identity_and_organization_core_ecosystem",
 "DEVELOPER_AND_SOURCE_CONTROL":"atlassian_developer_and_source_control_core_ecosystem",
 "KNOWLEDGE_AND_COLLABORATION":"atlassian_knowledge_and_collaboration_core_ecosystem",
 "WORK_MANAGEMENT_AND_PLANNING":"atlassian_work_management_and_planning_core_ecosystem",
 "IT_SERVICE_AND_OPERATIONS":"atlassian_it_service_and_operations_core_ecosystem",
 "GOVERNANCE_AND_SECURITY":"atlassian_governance_and_security_core_ecosystem",
 "INTEGRATION_AND_AUTOMATION":"atlassian_integration_and_automation_core_ecosystem",
}
def test_domain_mapping_complete(): assert len(DOMAIN_DEFINITIONS)==8 and set(DOMAIN_PACKAGES)==set(DOMAIN_DEFINITIONS)
def test_domain_packages_export_managers():
 package_root="backend.core.global_ecosystem.global_core_ecosystem.atlassian_core_ecosystem"
 for domain_id,package_name in DOMAIN_PACKAGES.items():
  module=importlib.import_module(f"{package_root}.{package_name}"); manager=module.get_manager()
  assert manager.DOMAIN_ID==domain_id and manager.status()["domain_id"]==domain_id and manager.list_offerings()["success"]
def test_inventory_counts_match_summary():
 summary=atlassian_domain_summary(); assert summary["domain_count"]==8
 for domain in summary["domains"]: assert AtlassianCoreDomainManager(domain["domain_id"]).list_offerings()["count"]==domain["offering_count"]
def test_canonical_manager_contract():
 from .manager import get_manager
 manager=get_manager()
 assert manager.status()["success"] and manager.health()["product_family_count"]==5
 assert manager.list_products()["count"]==5 and manager.list_offerings()["count"]==5 and manager.list_domains()["domain_count"]==8
def test_package_directory_names_follow_provider_standard():
 root=Path(__file__).parent
 pattern=re.compile(r"^atlassian_(?:shared_[a-z0-9_]+|[a-z0-9_]+)_core_ecosystem$")
 exceptions={"php","tests"}
 packages=[item.name for item in root.iterdir() if item.is_dir() and item.name not in exceptions]
 assert packages and all(pattern.fullmatch(name) for name in packages)
