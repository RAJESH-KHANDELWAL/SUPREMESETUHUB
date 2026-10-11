from __future__ import annotations

import unittest

from backend.database.service import DatabaseService
from backend.supreme.core.referral_service import SupremeReferralService
from backend.supreme.database.referral_repository import ReferralRepository
from backend.supreme.engines.referral_engine import ReferralEngine
from backend.supreme.storage.referral_store import ReferralStore


class SupremeReferralStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.database = DatabaseService(":memory:")
        self.repository = ReferralRepository(self.database)
        self.service = SupremeReferralService(
            store=ReferralStore(self.repository),
            engine=ReferralEngine(),
        )

    def tearDown(self) -> None:
        self.database.close()

    def test_person_and_do_not_contact_are_persisted(self) -> None:
        person = self.service.create_person({
            "display_name": "Test Person",
            "source_platform": "BADA BUSINESS",
            "need_category": "BUSINESS",
            "contact_consent": True,
            "whatsapp_contact": "+910000000000",
        })
        self.assertEqual(person["response_stage"], "NEW")
        self.assertEqual(person["contact_consent"], 1)

        suppressed = self.service.set_person_stage(person["person_id"], "DO_NOT_CONTACT")
        self.assertEqual(suppressed["response_stage"], "DO_NOT_CONTACT")
        self.assertEqual(suppressed["contact_consent"], 0)

    def test_referral_link_requires_https_and_keeps_platform_identity(self) -> None:
        with self.assertRaises(ValueError):
            self.service.create_referral_link({
                "platform": "YOUTAG WELLNESS",
                "program_name": "Team Referral",
                "referral_url": "http://example.com/ref",
                "ownership_type": "TEAM",
            })

        link = self.service.create_referral_link({
            "platform": "YOUTAG WELLNESS",
            "program_name": "Team Referral",
            "referral_url": "https://example.com/ref",
            "whatsapp_contact": "+910000000000",
            "ownership_type": "TEAM",
        })
        self.assertEqual(link["platform"], "YOUTAG WELLNESS")
        self.assertEqual(link["ownership_type"], "TEAM")

    def test_commission_requires_valid_state_transitions(self) -> None:
        person = self.service.create_person({
            "display_name": "Commission Test",
            "source_platform": "I DIGITAL PRENEUR",
            "need_category": "LEARNING",
        })
        link = self.service.create_referral_link({
            "platform": "I DIGITAL PRENEUR",
            "program_name": "Team Link",
            "referral_url": "https://example.com/idp",
        })
        commission = self.service.create_commission({
            "person_id": person["person_id"],
            "referral_id": link["referral_id"],
            "partner_name": "Test Partner",
            "order_reference": "ORDER-TEST-001",
            "amount_paise": 100,
        })
        self.assertEqual(commission["status"], "PENDING")
        self.assertEqual(commission["amount_paise"], 100)

        approved = self.service.update_commission_status(commission["commission_id"], "APPROVED")
        self.assertEqual(approved["status"], "APPROVED")
        paid = self.service.update_commission_status(commission["commission_id"], "PAID")
        self.assertEqual(paid["status"], "PAID")

        with self.assertRaises(ValueError):
            self.service.update_commission_status(commission["commission_id"], "PENDING")


if __name__ == "__main__":
    unittest.main()
