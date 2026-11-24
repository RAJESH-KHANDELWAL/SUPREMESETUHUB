import unittest
from ..catalog import list_work_types, get_work_type, search_work_types
from ..validators import validate_work_types

class SpecializationTests(unittest.TestCase):
    def test_work_types_are_present_and_unique(self):
        items = list_work_types()
        self.assertTrue(items)
        self.assertEqual(len(items), len({item.id for item in items}))
        self.assertTrue(all(item.name and item.description for item in items))

    def test_detail_and_search(self):
        first = list_work_types()[0]
        self.assertEqual(get_work_type(first.id), first)
        self.assertTrue(search_work_types(first.name.split()[0]))

    def test_integrity(self):
        self.assertTrue(validate_work_types()["structurally_valid"])

if __name__ == "__main__":
    unittest.main()
