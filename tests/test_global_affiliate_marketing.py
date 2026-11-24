"""Tests for the Bada Business affiliate CORE + DATABASE vertical slice."""
import unittest

from backend.database.service import DatabaseService
from backend.database.global_ecosystem.global_database_ecosystem.global_bada_business_database_ecosystem.global_affiliate_marketing_business_database_ecosystem import (
    AffiliateMarketingRepository,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_affiliate_marketing_business_core_ecosystem import (
    AffiliateMarketingCoreService,
)


class AffiliateMarketingWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseService(db_path=":memory:")
        self.repository = AffiliateMarketingRepository(self.database)
        self.service = AffiliateMarketingCoreService(self.repository)
        self.service.register_program(
            program_id="test-program",
            platform_id="I-DIGITALPRENEUR",
            program_name="Test affiliate program",
            commission_type="PERCENTAGE",
            commission_rate=10,
            currency="INR",
            terms_url="https://example.com/terms",
            verification_status="VERIFIED",
            program_status="ACTIVE",
        )

    def tearDown(self):
        self.database.close()

    def test_referral_requires_compensation_disclosure(self):
        with self.assertRaisesRegex(ValueError, "AFFILIATE_DISCLOSURE_REQUIRED"):
            self.service.create_referral(
                owner_user_id="owner-1",
                program_id="test-program",
                referral_code="RAJESH01",
                destination_url="https://example.com/product",
                disclosure_text="",
            )

    def test_referral_and_conversion_event_are_persisted(self):
        referral = self.service.create_referral(
            owner_user_id="owner-1",
            program_id="test-program",
            referral_code="RAJESH01",
            destination_url="https://example.com/product",
            disclosure_text="This is an affiliate link; I may earn a commission.",
        )
        event = self.service.record_event(
            referral_id=referral["referral_id"],
            source_event_id="provider-event-100",
            event_type="CONVERSION",
            amount_minor=250000,
            commission_minor=25000,
            currency="INR",
        )
        self.assertEqual(event["event_type"], "CONVERSION")
        self.assertEqual(event["amount_minor"], 250000)
        self.assertEqual(len(self.repository.list_events(referral["referral_id"])), 1)

    def test_event_ingestion_is_idempotent(self):
        referral = self.service.create_referral(
            owner_user_id="owner-1",
            program_id="test-program",
            referral_code="RAJESH02",
            destination_url="https://example.com/product",
            disclosure_text="I may earn a commission from this affiliate link.",
        )
        payload = {
            "referral_id": referral["referral_id"],
            "source_event_id": "provider-event-duplicate",
            "event_type": "CLICK",
            "currency": "INR",
        }
        first = self.service.record_event(**payload)
        second = self.service.record_event(**payload)
        self.assertEqual(first["event_id"], second["event_id"])
        self.assertEqual(len(self.repository.list_events(referral["referral_id"])), 1)

    def test_unverified_program_cannot_be_activated(self):
        with self.assertRaisesRegex(ValueError, "MUST_BE_VERIFIED"):
            self.service.register_program(
                program_id="unverified-program",
                platform_id="LEADSGURU",
                program_name="Unverified program",
                program_status="ACTIVE",
                verification_status="UNVERIFIED",
                terms_url="https://example.com/terms",
            )

    def test_unknown_platform_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "PLATFORM_NOT_SUPPORTED"):
            self.service.register_program(
                program_id="unknown-program",
                platform_id="UNKNOWN",
                program_name="Unknown program",
            )

    def test_currency_mismatch_is_rejected(self):
        referral = self.service.create_referral(
            owner_user_id="owner-1",
            program_id="test-program",
            referral_code="RAJESH03",
            destination_url="https://example.com/product",
            disclosure_text="This affiliate link may earn me a commission.",
        )
        with self.assertRaisesRegex(ValueError, "CURRENCY_MISMATCH"):
            self.service.record_event(
                referral_id=referral["referral_id"],
                source_event_id="provider-event-101",
                event_type="CONVERSION",
                amount_minor=1000,
                commission_minor=100,
                currency="USD",
            )


if __name__ == "__main__":
    unittest.main()
