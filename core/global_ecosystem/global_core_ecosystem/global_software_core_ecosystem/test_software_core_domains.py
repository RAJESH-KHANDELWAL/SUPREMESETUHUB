"""Structural and behavior tests for Global Software Core."""
from importlib import import_module
from .catalog import get_software_core_catalog
from .domain_catalog import DOMAIN_DEFINITIONS, software_domain_summary
from .manager import get_manager

def test_provider_catalog_is_unique_and_has_no_claimed_live_connections():
    catalog=get_software_core_catalog(); providers=catalog["providers"]
    assert len(providers)==6
    assert len({p["provider"] for p in providers})==len(providers)
    assert all(p["connected"] is False and p["live_connection_verified"] is False for p in providers)

def test_domain_packages_export_working_managers():
    package_root="backend.core.global_ecosystem.global_core_ecosystem.global_software_core_ecosystem"
    for domain_id, package_name in DOMAIN_PACKAGES.items():
        module=import_module(f"{package_root}.{package_name}")
        manager=module.get_manager()
        assert manager.DOMAIN_ID==domain_id
        assert manager.status()["success"] is True

def test_manager_health_matches_catalog():
    manager=get_manager(); health=manager.health()
    assert health["provider_count"]==6
    assert health["domain_count"]==len(DOMAIN_DEFINITIONS)
    assert health["live_connections_verified"]==0
    assert software_domain_summary()["domain_count"]==len(DOMAIN_DEFINITIONS)

DOMAIN_PACKAGES={
  "SOFTWARE_GOVERNANCE": "global_software_governance_core_ecosystem",
  "OPERATING_SYSTEMS": "global_operating_systems_core_ecosystem",
  "DESKTOP_AND_PRODUCTIVITY": "global_desktop_and_productivity_core_ecosystem",
  "BUSINESS_AND_ENTERPRISE": "global_business_and_enterprise_core_ecosystem",
  "DEVELOPMENT_AND_IDE": "global_development_and_ide_core_ecosystem",
  "DEVOPS_AND_DELIVERY": "global_devops_and_delivery_core_ecosystem",
  "CLOUD_AND_INFRASTRUCTURE": "global_cloud_and_infrastructure_core_ecosystem",
  "DATABASE_AND_DATA": "global_database_and_data_core_ecosystem",
  "AI_AND_MACHINE_LEARNING": "global_ai_and_machine_learning_core_ecosystem",
  "SECURITY_AND_PRIVACY": "global_security_and_privacy_core_ecosystem",
  "DESIGN_AND_CREATIVE": "global_design_and_creative_core_ecosystem",
  "WEB_AND_CONTENT": "global_web_and_content_core_ecosystem",
  "COMMUNICATION_AND_COLLABORATION": "global_communication_and_collaboration_core_ecosystem",
  "ANALYTICS_AND_OBSERVABILITY": "global_analytics_and_observability_core_ecosystem",
  "NETWORKING_AND_SYSTEMS": "global_networking_and_systems_core_ecosystem",
  "MOBILE_AND_APPLICATIONS": "global_mobile_and_applications_core_ecosystem",
  "GAMING_AND_INTERACTIVE": "global_gaming_and_interactive_core_ecosystem",
  "LICENSING_SUPPORT_AND_INTEROPERABILITY": "global_licensing_support_and_interoperability_core_ecosystem"
}
