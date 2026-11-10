import unittest

from .policy import evaluate_use_context


class GovernancePolicyTests(unittest.TestCase):
    def test_adult_context_fails_closed_without_safeguards(self):
        result = evaluate_use_context(domain="adult_content", purpose="lawful_adult_platform_safety")
        self.assertFalse(result["allowed_by_precheck"])
        self.assertIn("age_verified", result["missing_safeguards"])
        self.assertIn("consent_confirmed", result["missing_safeguards"])
        self.assertIn("rights_confirmed", result["missing_safeguards"])

    def test_adult_context_requires_permitted_purpose(self):
        result = evaluate_use_context(
            domain="adult", age_verified=True, consent_confirmed=True, rights_confirmed=True,
        )
        self.assertFalse(result["allowed_by_precheck"])
        self.assertIn("permitted_purpose", result["missing_safeguards"])

    def test_health_context_requires_human_review(self):
        result = evaluate_use_context(domain="healthcare")
        self.assertFalse(result["allowed_by_precheck"])
        self.assertIn("human_review_available", result["missing_safeguards"])


if __name__ == "__main__":
    unittest.main()
