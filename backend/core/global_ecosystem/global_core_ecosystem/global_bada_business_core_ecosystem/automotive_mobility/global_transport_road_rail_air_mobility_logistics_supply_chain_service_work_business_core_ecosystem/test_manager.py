import unittest

from .catalog import get_business_domain, list_business_domains
from .manager import get_manager


class GlobalTransportMobilityBusinessCoreTests(unittest.TestCase):
    def test_business_domains_are_unique(self):
        domains = list_business_domains()
        self.assertEqual(len(domains), 10)
        self.assertEqual(len({item["id"] for item in domains}), 10)

    def test_business_domain_lookup(self):
        self.assertEqual(
            get_business_domain("freight_logistics_supply_chain")["category_id"],
            "freight_logistics_supply_chain",
        )
        self.assertIsNone(get_business_domain("not-a-domain"))

    def test_manager_does_not_execute_operations(self):
        status = get_manager().status()
        self.assertEqual(status["status"], "CORE_CATALOG_ONLY")
        self.assertEqual(status["operational_workflows_executed"], 0)
        self.assertEqual(get_manager().list_domains()["count"], 10)


if __name__ == "__main__":
    unittest.main()
