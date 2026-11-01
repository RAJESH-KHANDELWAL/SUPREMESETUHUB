"""Structural tests for modular company/business/freelancer packages."""
import unittest
from ..classification_registry import list_record_classes, validate_record_class_registry
from ..company_legal_entities_api_ecosystem.catalog import CATEGORY as COMPANY
from ..business_enterprises_api_ecosystem.catalog import CATEGORY as BUSINESS
from ..freelancer_independent_professionals_api_ecosystem.catalog import CATEGORY as FREELANCER
from ..entity_registry import classify_entity_type
from ..global_company_world_map import list_world_domains

class ModularArchitectureTests(unittest.TestCase):
    def test_three_top_level_record_classes(self):
        self.assertEqual({x["record_type"] for x in list_record_classes()}, {"company","business","freelancer"})
        self.assertTrue(validate_record_class_registry()["structurally_valid"])
    def test_each_class_has_its_own_taxonomy(self):
        self.assertEqual((COMPANY["record_type"], BUSINESS["record_type"], FREELANCER["record_type"]), ("company","business","freelancer"))
        self.assertTrue(COMPANY["entity_types"] and BUSINESS["entity_types"] and FREELANCER["entity_types"])
    def test_entity_type_classification(self):
        self.assertEqual(classify_entity_type("registered_company"), "company")
        self.assertEqual(classify_entity_type("small_business"), "business")
        self.assertEqual(classify_entity_type("freelancer"), "freelancer")
        self.assertIsNone(classify_entity_type("unknown_type"))
    def test_world_map_covers_all_classes(self):
        domains = list_world_domains()
        self.assertEqual({x["record_type"] for x in domains}, {"company","business","freelancer"})
        self.assertEqual(len(domains), 3)
if __name__ == "__main__":
    unittest.main()
