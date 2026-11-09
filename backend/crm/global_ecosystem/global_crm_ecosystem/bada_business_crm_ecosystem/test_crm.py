"""Tests for Bada Business CRM adapter using injected fake CRM service."""

import unittest

from .service import BadaBusinessCRMService


class FakeCRMService:
    def __init__(self):
        self.created = None

    def create_contact(self, owner, actor, data):
        self.created = (owner, actor, data)
        return data

    def list_contacts(self, owner, **filters):
        return [{"contact_id": "c1", "category": "LEAD"}] if filters.get("category") == "LEAD" else []

    @staticmethod
    def suggest_category(record):
        return {"contact_id": record["contact_id"], "suggested_category": "LEAD"}

    @staticmethod
    def get_contact(owner, contact_id):
        return {"contact_id": contact_id, "full_name": "Sample", "consent_to_contact": False, "contact_status": "ACTIVE"}

    @staticmethod
    def suggest_follow_up(record):
        return {"suggested_action": "CHECK_CONSENT_BEFORE_OUTREACH"}

    @staticmethod
    def draft_message(*args):
        raise PermissionError("EXPLICIT_CONTACT_CONSENT_REQUIRED")


class BadaBusinessCRMTests(unittest.TestCase):
    def setUp(self):
        self.fake = FakeCRMService()
        self.service = BadaBusinessCRMService(self.fake)

    def test_create_lead_sets_domain_defaults(self):
        result = self.service.create_business_lead("owner-1", "actor-1", {"full_name": "Lead"})
        self.assertEqual(result["category"], "LEAD")
        self.assertEqual(result["source"], "BADA_BUSINESS")
        self.assertFalse(result["consent_to_contact"])

    def test_list_leads_is_owner_scoped_and_category_filtered(self):
        result = self.service.list_business_leads("owner-1")
        self.assertEqual(result["count"], 1)

    def test_category_suggestion_is_not_applied(self):
        result = self.service.suggest_lead_category({"contact_id": "c1"})
        self.assertTrue(result["requires_human_approval"])
        self.assertFalse(result["applied"])

    def test_follow_up_never_sends_message(self):
        result = self.service.prepare_follow_up("owner-1", "c1")
        self.assertFalse(result["message_sent"])

    def test_outreach_uses_consent_enforcing_core_service(self):
        with self.assertRaises(PermissionError):
            self.service.draft_outreach("owner-1", "c1", "business opportunity")


if __name__ == "__main__":
    unittest.main()
