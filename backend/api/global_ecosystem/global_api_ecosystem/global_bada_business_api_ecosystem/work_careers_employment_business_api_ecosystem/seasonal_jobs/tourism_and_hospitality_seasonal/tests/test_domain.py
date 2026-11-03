import unittest

from .. import categories, services

class JobFamilyPackageTests(unittest.TestCase):
    def test_job_family_has_its_own_identity_and_catalogue(self):
        self.assertTrue(categories.CATEGORY_ID)
        self.assertEqual(categories.JOB_FAMILY_ID, "tourism_and_hospitality_seasonal")
        self.assertTrue(categories.JOB_FAMILY_NAME)
        self.assertTrue(categories.ROLE_EXAMPLES)
        family = services.get_job_family()
        self.assertEqual(family["job_family_id"], categories.JOB_FAMILY_ID)
        self.assertEqual(family["category_id"], categories.CATEGORY_ID)
        self.assertTrue(family["role_examples"])

if __name__ == "__main__":
    unittest.main()
