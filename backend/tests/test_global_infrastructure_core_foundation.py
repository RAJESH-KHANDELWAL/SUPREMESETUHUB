from backend.core.global_ecosystem.global_core_ecosystem.global_infrastructure_core_ecosystem import GlobalInfrastructureCoreOrchestrator,GlobalInfrastructureCoreService,get_domain_catalog,get_provider_catalog
def test_catalog_is_provider_neutral_and_read_only():
 c=GlobalInfrastructureCoreOrchestrator().catalog()
 assert c["ecosystem_id"]=="GLOBAL-INFRASTRUCTURE-CORE-ECOSYSTEM"
 assert len(c["domains"])==20
 assert all(p["live_connection_verified"] is False for p in c["providers"])
def test_catalog_returns_independent_data():
 d=get_domain_catalog(); d[0]["name"]="MUTATED"
 assert get_domain_catalog()[0]["name"]!="MUTATED"
def test_existing_resource_validation_is_preserved():
 s=GlobalInfrastructureCoreService()
 assert s.validate_resource({"resource_id":"srv-001","resource_type":"vps","category":"compute"})["success"] is True
 assert s.validate_resource({"resource_id":"","resource_type":"vps"})["success"] is False
def test_core_health_does_not_claim_provider_execution():
 h=GlobalInfrastructureCoreOrchestrator().health()
 assert h["status"]=="HEALTHY" and h["provider_operations_enabled"] is False
def test_provider_catalog_is_metadata_only():
 assert all(p["status"]=="CATALOG_ONLY" for p in get_provider_catalog())
