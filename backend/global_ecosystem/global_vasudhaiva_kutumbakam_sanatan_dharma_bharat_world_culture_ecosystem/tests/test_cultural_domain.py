import unittest

from ..domain import CulturalResource
from ..governance import assess_publication
from ..discovery import discover

class CulturalDomainTests(unittest.TestCase):
    def make_resource(self, **changes):
        values = dict(
            resource_id="bharat-001", title="Classical literature resource",
            pillar="bharat_sanskriti", area="languages_and_literature",
            description="A sourced educational resource.", source_reference="catalog:public-001",
            source_kind="documented", rights_status="public_domain",
        )
        values.update(changes)
        return CulturalResource(**values)

    def test_approved_public_resource_passes(self):
        result = assess_publication(self.make_resource())
        self.assertTrue(result.approved_for_public_discovery)
        self.assertEqual(result.reasons, ())

    def test_restricted_or_uncleared_resource_is_not_public(self):
        resource = self.make_resource(access_level="restricted", rights_status="restricted")
        result = assess_publication(resource)
        self.assertFalse(result.approved_for_public_discovery)
        self.assertIn("resource_access_is_not_public", result.reasons)

    def test_discovery_filters_unapproved_resources(self):
        approved = self.make_resource()
        pending = self.make_resource(resource_id="pending-002", consent_status="pending")
        self.assertEqual(discover([approved, pending]), (approved,))

if __name__ == "__main__":
    unittest.main()
