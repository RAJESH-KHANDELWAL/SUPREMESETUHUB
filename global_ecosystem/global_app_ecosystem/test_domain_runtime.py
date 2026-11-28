"""Tests for domain workflow services and mandatory safeguards."""
import unittest
from .domain_runtime import DomainValidationError, create_domain_service

class DomainRuntimeTests(unittest.TestCase):
    def test_all_domains_can_be_inspected(self):
        from .scope import list_domain_ids
        for domain_id in list_domain_ids():
            with self.subTest(domain_id=domain_id):
                self.assertEqual(create_domain_service(domain_id).inspect()["id"], domain_id)
    def test_normal_domain_validation(self):
        result = create_domain_service("mobile_android_ios_apps").validate({})
        self.assertTrue(result.accepted)
    def test_adult_domain_requires_age_and_consent(self):
        service = create_domain_service("adult_dating_relationship_apps")
        with self.assertRaises(DomainValidationError):
            service.validate({})
        result = service.validate({"age_verified": True, "participants_are_adults": True, "consent_confirmed": True})
        self.assertTrue(result.accepted)
    def test_adult_streaming_blocks_nonconsensual_content(self):
        service = create_domain_service("adult_entertainment_streaming_apps")
        payload = {"age_verified": True, "participants_are_adults": True, "consent_confirmed": True, "rights_cleared": True, "nonconsensual_intimate_content": True}
        with self.assertRaises(DomainValidationError):
            service.validate(payload)
    def test_unknown_action_rejected(self):
        with self.assertRaises(DomainValidationError):
            create_domain_service("mobile_android_ios_apps").validate({"action": "execute_payment"})

if __name__ == "__main__":
    unittest.main()
