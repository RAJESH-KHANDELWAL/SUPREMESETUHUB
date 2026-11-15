import unittest

from .. import categories, services


class JobFamilyPackageTests(unittest.TestCase):
    """Validate either supported specialization adapter against its owning category."""

    def test_job_family_has_stable_identity_and_resolves_its_catalogue(self):
        self.assertTrue(categories.CATEGORY_ID)

        if hasattr(categories, "TRACK_ID"):
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
        else:
            self.assertTrue(categories.JOB_FAMILY_ID)
            self.assertTrue(categories.JOB_FAMILY_NAME)
            self.assertTrue(categories.ROLE_EXAMPLES)

            family = services.get_job_family()
            self.assertEqual(family["job_family_id"], categories.JOB_FAMILY_ID)
            self.assertEqual(family["category_id"], categories.CATEGORY_ID)
            self.assertEqual(family["name"], categories.JOB_FAMILY_NAME)
            self.assertTrue(family["role_examples"])


if __name__ == "__main__":
    unittest.main()
