"""Tests for the accessibility ecosystem starter modules."""

import unittest

from global_accessibility_ecosystem.audit import (
    audit_form_labels,
    audit_image_alternatives,
)
from global_accessibility_ecosystem.catalog import list_features


class AccessibilityTests(unittest.TestCase):
    def test_catalog_contains_screen_reader_support(self):
        self.assertTrue(
            any(item.feature_id == "screen_reader_support" for item in list_features())
        )

    def test_category_filter(self):
        self.assertTrue(
            all(item.category == "captions" for item in list_features("captions"))
        )

    def test_missing_image_alt_is_reported(self):
        findings = audit_image_alternatives([{"id": "hero", "alt": ""}])
        self.assertEqual(findings[0]["severity"], "error")

    def test_missing_form_name_is_reported(self):
        findings = audit_form_labels([{"id": "email"}])
        self.assertEqual(findings[0]["severity"], "error")


if __name__ == "__main__":
    unittest.main()
