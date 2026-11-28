"""IBM Core catalog, boundary, namespace and master-catalog tests."""
import json
import unittest
from pathlib import Path
from . import get_manager
from .product_catalog import list_products
from .domain_catalog import list_domains,get_domain
from .policy import IBMCorePolicy
from .contracts import TenantContext

class IBMCoreTests(unittest.TestCase):
    def test_manager_identity_and_status(self):
        m=get_manager()
        self.assertEqual(m.ECOSYSTEM_ID,"IBM-CORE-ECOSYSTEM")
        self.assertEqual(m.status()["status"],"CORE_CATALOG_ONLY")
    def test_sixteen_existing_product_families_are_unique(self):
        items=list_products()
        self.assertEqual(len(items),16)
        ids=[x["product_id"] for x in items]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertTrue(all(x["live_connection_verified"] is False for x in items))
        self.assertTrue(all(x["api_path"] and x["engine_path"] for x in items))
    def test_eighteen_domains_are_unique(self):
        items=list_domains()
        ids=[x["domain_id"] for x in items]
        self.assertEqual(len(items),18)
        self.assertEqual(len(ids),len(set(ids)))
        self.assertIsNotNone(get_domain("WATSONX_AI_MODELS_INFERENCE"))
    def test_domain_to_product_mapping_covers_all_registered_families(self):
        product_ids={x["product_id"] for x in list_products()}
        mapped={product_id for domain in list_domains() for product_id in domain["product_ids"]}
        self.assertEqual(mapped,product_ids)
    def test_all_product_packages_import(self):
        import importlib
        slugs=["api_connect_gateway","billing_usage_cost","cloud_object_storage","cloud_platform","cloudant","code_engine_serverless","db2_database","iam_identity","kubernetes_containers","monitoring_activity_tracker","resource_controller_catalog","secrets_manager","security_key_protect","vpc_compute_networking","watsonx_ai","watsonx_data"]
        for slug in slugs:
            module=importlib.import_module(f"{__package__}.ibm_{slug}_core_ecosystem")
            self.assertTrue(any(name.endswith("CoreManager") for name in module.__all__))
            manager_class=getattr(module,module.__all__[0])
            self.assertTrue(manager_class.PRODUCT_ID.startswith("ibm_"))
    def test_all_domain_packages_import(self):
        import importlib
        slugs=["provider_governance","cloud_account_resource_governance","iam_identity_access","compute_vpc_networking","kubernetes_containers","serverless_code_engine","object_storage_artifacts","databases_cloudant","watsonx_ai_models_inference","watsonx_data_analytics","api_management_gateway","secrets_management","key_management_cryptography","monitoring_observability","activity_tracking_audit","resource_catalog_lifecycle","billing_usage_cost","tenancy_region_quota_compliance"]
        for slug in slugs:
            module=importlib.import_module(f"{__package__}.ibm_{slug}_domain_core_ecosystem")
            self.assertTrue(any(name.endswith("CoreManager") for name in module.__all__))
    def test_master_catalog_alignment_is_read_only_and_exact(self):
        path=Path(__file__).resolve().parents[4]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
        data=json.loads(path.read_text(encoding="utf-8"))
        ids={entry["entry_id"] for section in data["sections"] for entry in section["entries"]}
        expected=["S09_software","S09_cloud_computing","S09_artificial_intelligence","S09_machine_learning","S09_database","S09_data_analytics","S09_cybersecurity","S10_global_database","S10_global_security","S10_global_data_core"]
        self.assertTrue(set(expected).issubset(ids))
        self.assertFalse(any("ibm" in x.lower() for x in ids))
        self.assertEqual(get_manager().catalog()["master_catalog_alignment"],"RELATED_CANONICAL_TECHNOLOGY_TOPICS_NO_IBM_SPECIFIC_ENTRY")
    def test_parent_global_core_registration(self):
        from backend.core.global_ecosystem.global_core_ecosystem.manager import get_catalog as get_global_catalog
        records=[x for x in get_global_catalog() if x["ecosystem_id"]=="IBM-CORE-ECOSYSTEM"]
        self.assertEqual(len(records),1)
        self.assertEqual(records[0]["parent_id"],"GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(records[0]["metadata"]["product_count"],16)
    def test_api_engine_and_live_boundaries(self):
        m=get_manager()
        self.assertFalse(m.catalog()["live_connection_verified"])
        self.assertFalse(m.catalog()["remote_operations_enabled"])
        self.assertEqual(m.health()["api_calls_performed"],0)
        self.assertEqual(len(m.dependency_map()["edges"]),16)
    def test_policy_and_tenant_contract(self):
        m=get_manager()
        product=m.get_product("ibm_iam_identity")
        self.assertEqual(IBMCorePolicy.classify_capability("IAM_ADMIN"),"SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION")
        with self.assertRaises(PermissionError): IBMCorePolicy.require_tenant_context(None)
        self.assertEqual(m.get_product_manager("ibm_iam_identity").authorize_capability("IDENTITY_ACCESS",TenantContext("t1","a1"))["success"],True)
        with self.assertRaises(LookupError): m.get_product_manager("not-real")
    def test_unknown_domain_rejected(self):
        with self.assertRaises(ValueError): get_manager().get_domain_manager("NOT_A_DOMAIN")

if __name__=="__main__": unittest.main()
