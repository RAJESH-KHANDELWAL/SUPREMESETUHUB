"""Meta Core catalog, package, security and master-catalog tests."""
import json
import unittest
from pathlib import Path
from . import get_manager
from .product_catalog import list_meta_products
from .domain_catalog import list_meta_domain_inventory
from .policy import MetaCorePolicy
from .contracts import TenantContext
from backend.api.global_ecosystem.global_api_ecosystem.meta_api_ecosystem.meta_api_ecosystem import META_API_ECOSYSTEM

class MetaCoreTests(unittest.TestCase):
    def test_manager_identity_and_parent_status(self):
        manager=get_manager()
        self.assertEqual(manager.ECOSYSTEM_ID,"META-CORE-ECOSYSTEM")
        self.assertEqual(manager.status()["status"],"CORE_CATALOG_ONLY")
        self.assertTrue(manager.status()["registry_status"])
    def test_exact_api_catalog_family_parity(self):
        api_ids={x["id"] for x in META_API_ECOSYSTEM["children"]}
        core_ids={x["family_id"] for x in list_meta_products()}
        self.assertEqual(core_ids,api_ids)
        self.assertEqual(len(core_ids),12)
    def test_api_and_engine_paths_are_real_layer_references(self):
        products=list_meta_products()
        self.assertTrue(all(x["api_path"].startswith("backend/api/") for x in products))
        self.assertTrue(all(x["engine_path"].startswith("backend/engine/") for x in products))
        self.assertTrue(all(x["api_module"] and x["engine_module"] for x in products))
    def test_meta_ai_is_discovery_only(self):
        item=get_manager().get_product("meta_ai")
        self.assertEqual(item["status"],"DISCOVERY_ONLY")
        result=get_manager().get_product_manager("meta_ai").authorize_capability("META_AI_DISCOVERY_ONLY",TenantContext("t1","a1"))
        self.assertFalse(result["success"])
    def test_eighteen_domains_unique_and_mapped(self):
        domains=list_meta_domain_inventory()
        self.assertEqual(len(domains),18)
        ids=[x["domain_id"] for x in domains]
        self.assertEqual(len(ids),len(set(ids)))
        product_ids={x["product_id"] for x in list_meta_products()}
        mapped={p for d in domains for p in d["product_ids"]}
        self.assertEqual(mapped,product_ids)
    def test_product_and_domain_packages_import(self):
        import importlib
        product_packages=["graph","facebook_pages","instagram","whatsapp_business","messenger","threads","marketing_ads","login_identity","business_management","webhooks","ai","sdk_developer_tools"]
        domain_packages=["provider_governance","graph_platform_and_object_model","facebook_pages_and_publishing","instagram_creator_and_professional","whatsapp_business_messaging","messenger_conversations","threads_social_network","marketing_advertising_campaigns","business_portfolio_assets","login_oauth_identity","webhook_event_delivery","meta_ai_discovery","social_content_publishing","audience_insights_analytics","media_asset_management","privacy_data_protection","app_review_permission_compliance","tenant_account_asset_governance"]
        for slug in product_packages:
            module=importlib.import_module(f"{__package__}.meta_{slug}_core_ecosystem")
            cls=getattr(module,module.__all__[0])
            self.assertEqual(cls.PRODUCT_ID,"meta_"+("graph_core" if slug=="graph" else slug))
        for slug in domain_packages:
            module=importlib.import_module(f"{__package__}.meta_{slug}_domain_core_ecosystem")
            cls=getattr(module,module.__all__[0])
            self.assertTrue(callable(cls))
    def test_master_catalog_alignment_is_exact_and_read_only(self):
        path=Path(__file__).resolve().parents[4]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
        data=json.loads(path.read_text(encoding="utf-8"))
        ids={entry["entry_id"] for section in data["sections"] for entry in section["entries"]}
        expected=["S07_privacy_and_data_protection","S09_artificial_intelligence","S09_cybersecurity","S09_data_analytics","S09_digital_identity","S11_privacy_law","S08_individual_business","S08_small_business","S08_medium_business","S08_digital_business","S08_international_business"]
        self.assertTrue(set(expected).issubset(ids))
        self.assertFalse(any("meta" in value.lower() for value in ids))
        self.assertEqual(get_manager().catalog()["master_catalog_alignment"],"EXISTING_RELATED_TOPICS_ONLY_NO_META_SPECIFIC_ENTRY")
    def test_parent_global_core_registration(self):
        from backend.core.global_ecosystem.global_core_ecosystem.manager import get_catalog as get_global_catalog
        records=[x for x in get_global_catalog() if x["ecosystem_id"]=="META-CORE-ECOSYSTEM"]
        self.assertEqual(len(records),1)
        self.assertEqual(records[0]["parent_id"],"GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(records[0]["metadata"]["product_count"],12)
    def test_layer_boundaries_and_dependency_map(self):
        manager=get_manager()
        self.assertFalse(manager.catalog()["live_connection_verified"])
        self.assertFalse(manager.catalog()["oauth_exchange_in_core"])
        self.assertEqual(manager.health()["api_calls_performed"],0)
        self.assertEqual(len(manager.dependency_map()["edges"]),12)
    def test_policy_tenant_and_secret_redaction(self):
        self.assertEqual(MetaCorePolicy.classify_capability("SEND_MESSAGE"),"SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION")
        with self.assertRaises(PermissionError): MetaCorePolicy.require_tenant_context(None)
        self.assertEqual(MetaCorePolicy.sanitize({"name":"x","access_token":"secret","nested":{"app_secret":"x","ok":1}}),{"name":"x","nested":{"ok":1}})
        result=get_manager().get_product_manager("facebook_pages").authorize_capability("PAGE_CONTENT_PUBLISHING",TenantContext("t1","a1"))
        self.assertTrue(result["success"])
    def test_unknown_product_and_domain_rejected(self):
        with self.assertRaises(LookupError): get_manager().get_product_manager("unknown")
        with self.assertRaises(ValueError): get_manager().get_domain_manager("unknown")
if __name__=="__main__": unittest.main()
