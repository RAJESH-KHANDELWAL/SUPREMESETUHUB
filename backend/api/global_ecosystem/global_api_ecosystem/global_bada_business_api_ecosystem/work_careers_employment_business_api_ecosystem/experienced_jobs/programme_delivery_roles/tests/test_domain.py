import unittest

from .. import categories, services


class JobFamilyPackageTests(unittest.TestCase):
    """Validate the specialization adapter against its canonical category record."""

    def test_job_family_resolves_its_canonical_definition(self):
        self.assertTrue(categories.CATEGORY_ID)
        self.assertTrue(categories.TRACK_ID)

        definition = categories.get_track_definition()
        self.assertEqual(definition["id"], categories.TRACK_ID)
        self.assertTrue(definition["name"])
        self.assertTrue(definition["description"])

        resource = services.get_track_api_resource()
        self.assertEqual(resource["id"], categories.TRACK_ID)
        self.assertEqual(resource["category_id"], categories.CATEGORY_ID)
        self.assertEqual(resource["name"], definition["name"])
        self.assertEqual(resource["description"], definition["description"])
        self.assertEqual(resource["taxonomy_status"], "taxonomy_only")
        self.assertIsInstance(resource["role_families"], list)


if __name__ == "__main__":
    unittest.main()
