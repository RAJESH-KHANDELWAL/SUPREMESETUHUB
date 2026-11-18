import unittest

from ..business_domain import BusinessOffering, ProviderProfile
from ..governance import assess_listing
from ..marketplace import published_offerings

class BusinessDomainTests(unittest.TestCase):
    def make_offering(self, **changes):
        provider = ProviderProfile(
            provider_id="provider-001", display_name="Verified artisan collective",
            provider_type="community_group", region="Bharat", verification_status="verified",
        )
        values = dict(
            offering_id="offering-001", title="Handcrafted textile",
            domain="arts_crafts_handloom", offering_type="product", provider=provider,
            description="An artisan-led textile offering.", cultural_origin="Bharat",
            provenance_reference="evidence:origin-001", rights_status="licensed",
            consent_status="granted", fair_compensation_defined=True,
            safety_reviewed=True, legal_reviewed=True, status="approved",
        )
        values.update(changes)
        return BusinessOffering(**values)

    def test_fully_reviewed_offering_passes(self):
        self.assertTrue(assess_listing(self.make_offering()).eligible_for_publication)

    def test_unverified_provider_is_blocked(self):
        provider = ProviderProfile(
            provider_id="provider-002", display_name="New provider",
            provider_type="individual", verification_status="pending",
        )
        offering = self.make_offering(provider=provider)
        self.assertIn("provider_not_verified", assess_listing(offering).reasons)

    def test_marketplace_excludes_unapproved_offerings(self):
        approved = self.make_offering()
        pending = self.make_offering(offering_id="offering-002", consent_status="pending")
        self.assertEqual(published_offerings([approved, pending]), (approved,))

if __name__ == "__main__":
    unittest.main()
