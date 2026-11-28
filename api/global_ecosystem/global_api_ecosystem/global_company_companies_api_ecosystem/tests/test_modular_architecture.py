"""Structural tests for Company, Enterprise and Corporate Group packages."""
import unittest
from ..classification_registry import list_record_classes, validate_record_class_registry
from ..company_legal_entities_api_ecosystem.catalog import CATEGORY as COMPANY
from ..business_enterprises_api_ecosystem.catalog import CATEGORY as ENTERPRISE
from ..corporate_groups_api_ecosystem import SUBCATEGORY_IDS as GROUP_SUBCATEGORIES
from ..entity_registry import classify_entity_type
from ..global_company_world_map import list_world_domains

class ModularArchitectureTests(unittest.TestCase):
    def test_three_top_level_record_classes(self):
        self.assertEqual({x["record_type"] for x in list_record_classes()}, {"company","enterprise","corporate_group"})
        self.assertTrue(validate_record_class_registry()["structurally_valid"])
        self.assertFalse(validate_record_class_registry()["freelancer_is_company_record_class"])
    def test_each_class_has_its_own_taxonomy(self):
        self.assertTrue(COMPANY["entity_types"] and ENTERPRISE["entity_types"] and GROUP_SUBCATEGORIES)
    def test_entity_type_classification(self):
        self.assertEqual(classify_entity_type("registered_company"), "company")
        self.assertEqual(classify_entity_type("small_business"), "enterprise")
        self.assertEqual(classify_entity_type("corporate_group"), "corporate_group")
        self.assertIsNone(classify_entity_type("freelancer"))
        self.assertIsNone(classify_entity_type("unknown_type"))
    def test_world_map_covers_all_classes(self):
        domains=list_world_domains()
        self.assertEqual({x["record_type"] for x in domains},{"company","enterprise","corporate_group"})
        self.assertEqual(len(domains),3)
if __name__=="__main__": unittest.main()
