"""Hugging Face CORE catalog and boundary tests."""
import unittest
from . import get_manager
from .product_catalog import list_products
from .domain_catalog import list_domains, get_domain
from .policy import HuggingFaceCorePolicy

class HuggingFaceCoreTests(unittest.TestCase):
    def test_manager_and_identity(self):
        m=get_manager()
        self.assertEqual(m.ECOSYSTEM_ID,"HUGGINGFACE-CORE-ECOSYSTEM")
        self.assertEqual(m.status()["status"],"CORE_CATALOG_ONLY")
    def test_existing_fifteen_products_are_registered_once(self):
        items=list_products()
        ids=[x["product_id"] for x in items]
        self.assertEqual(len(items),15)
        self.assertEqual(len(ids),len(set(ids)))
        self.assertTrue(all(x["live_connection_verified"] is False for x in items))
    def test_domain_taxonomy_and_product_managers(self):
        domains=list_domains()
        ids=[x["domain_id"] for x in domains]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertGreaterEqual(len(domains),18)
        self.assertIsNotNone(get_manager().get_product_manager("huggingface_models").describe()["product"])
        self.assertIsNotNone(get_domain("MODEL_DISCOVERY"))
    def test_master_catalog_is_read_only(self):
        c=get_manager().catalog()["master_catalog"]
        self.assertEqual(c["canonical_entry_ids"],["S09_artificial_intelligence","S09_machine_learning"])
        self.assertEqual(c["catalogue_entries_added"],0)
    def test_layer_boundary(self):
        c=get_manager().catalog()
        self.assertFalse(c["live_connection_verified"])
        self.assertFalse(c["remote_operations_enabled"])
        self.assertEqual(c["api_calls_performed"],0)
        self.assertEqual(len(get_manager().dependency_map()["product_api_mappings"]),15)
    def test_policy_rejects_live_claims(self):
        policy=HuggingFaceCorePolicy()
        item=dict(list_products()[0],live_connection_verified=True)
        with self.assertRaises(ValueError): policy.validate_product(item)
    def test_unknown_product_rejected(self):
        with self.assertRaises(ValueError): get_manager().get_product_manager("unknown")
if __name__ == "__main__": unittest.main()
