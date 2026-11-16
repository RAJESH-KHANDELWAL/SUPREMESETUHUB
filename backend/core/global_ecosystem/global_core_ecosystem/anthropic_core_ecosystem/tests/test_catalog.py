"""Offline root catalog consistency tests."""
import unittest
from . import __doc__
from ..catalog import get_anthropic_core_catalog,list_anthropic_core_modules
from ..product_catalog import list_anthropic_offerings, anthropic_offerings_summary
from ..domain_catalog import list_anthropic_domain_inventory, anthropic_domain_summary

class AnthropicCoreCatalogTests(unittest.TestCase):
    def test_nine_modules_have_unique_ids_and_api_refs(self):
        items=list_anthropic_core_modules()
        self.assertEqual(len(items),9)
        self.assertEqual(len({x["ecosystem_id"] for x in items}),9)
        self.assertTrue(all(x["api_catalog_ref"].startswith("backend/api/") for x in items))
        self.assertTrue(all(x["live_connection_verified"] is False for x in items))
    def test_product_catalog_and_domain_coverage(self):
        offerings = list_anthropic_offerings()
        summary = anthropic_offerings_summary()
        domains = list_anthropic_domain_inventory()
        domain_summary = anthropic_domain_summary()
        self.assertEqual(len(offerings), 9)
        self.assertEqual(summary["mapped_count"], 9)
        self.assertEqual(len(domains), 9)
        self.assertEqual(domain_summary["assigned_offering_count"], 9)
        self.assertEqual(domain_summary["domain_count"], 9)
        self.assertEqual(summary["live_connections_verified"], 0)
        self.assertTrue(all(item["api_available"] is None for item in offerings))

    def test_catalog_is_defensive_copy(self):
        first=get_anthropic_core_catalog()
        first["children"].clear()
        self.assertEqual(len(get_anthropic_core_catalog()["children"]),9)

if __name__=="__main__":
    unittest.main()
