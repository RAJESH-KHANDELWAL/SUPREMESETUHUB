import unittest
from global_work_business_ecosystem.catalog import CATEGORIES,get_category,search_roles
class TestWorkCatalogue(unittest.TestCase):
    def test_categories_have_ids_and_aliases(self):
        self.assertTrue(CATEGORIES)
        self.assertTrue(all(v["role_names"] for v in CATEGORIES.values()))
    def test_lookup(self):
        self.assertEqual(get_category("employees")["name"],"Employees")
    def test_search(self):
        self.assertTrue(search_roles("Public Servant"))
    def test_empty_search(self):
        self.assertEqual(search_roles(""),[])
if __name__=="__main__": unittest.main()
