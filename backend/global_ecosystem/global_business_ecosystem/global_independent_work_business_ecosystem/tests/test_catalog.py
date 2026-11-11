import unittest
from backend.global_ecosystem.global_business_ecosystem.global_independent_work_business_ecosystem.catalog import CATEGORIES,get_category,search_roles
class TestIndependentWorkCatalogue(unittest.TestCase):
    def test_category_ids_unique(self):
        self.assertEqual(len(CATEGORIES),len(set(CATEGORIES)))
    def test_roles_exist(self):
        self.assertTrue(all(v["role_names"] for v in CATEGORIES.values()))
    def test_search(self):
        self.assertTrue(search_roles("Freelancer"))
        self.assertEqual(get_category("freelancers")["name"],"Freelancers")
if __name__=="__main__": unittest.main()
