import unittest
from ..catalog import get_catalog
from ..manager import get_manager
from ..domain_catalog import list_business_domains
class AgricultureBusinessTests(unittest.TestCase):
    def test_identity_and_parent(self):
        catalog=get_catalog()
        self.assertEqual(catalog["ecosystem_id"], get_manager().ECOSYSTEM_ID)
        self.assertEqual(catalog["parent_id"], "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM")
    def test_domain_ids_unique(self):
        ids=[x["domain_id"] for x in list_business_domains()]
        self.assertEqual(len(ids), len(set(ids)))
    def test_service_work_business(self):
        for item in list_business_domains():
            self.assertEqual(item["capabilities"], ["SERVICE", "WORK", "BUSINESS"])
    def test_global_core_dependency(self):
        self.assertEqual(get_catalog()["global_core_id"], "GLOBAL-AGRICULTURE-FOOD-NATURAL-RESOURCES-HUMAN-ANIMAL-CORE-ECOSYSTEM")
    def test_no_live_provider_claim(self):
        self.assertFalse(get_manager().health()["live_providers_verified"])
if __name__ == "__main__": unittest.main()
