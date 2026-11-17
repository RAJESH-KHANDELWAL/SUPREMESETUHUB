import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_adult_content_core_ecosystem.catalog import (
    get_catalog,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_adult_content_core_ecosystem.taxonomy import (
    get_orientation,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_adult_content_core_ecosystem.contracts import (
    Orientation,
    PolicyEvidence,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_adult_content_core_ecosystem.policy import (
    evaluate_content_metadata,
)
from backend.core.global_ecosystem.global_core_ecosystem.catalog import get_catalog as get_global_catalog


class GlobalAdultContentCoreTests(unittest.TestCase):
    def test_parent_global_catalog_registers_core_as_direct_child(self):
        records = get_global_catalog()
        record = next(
            item for item in records
            if item["ecosystem_id"] == "GLOBAL-ADULT-CONTENT-CORE-ECOSYSTEM"
        )
        self.assertEqual(record["parent_id"], "GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(
            record["metadata"]["core_module"],
            "backend/core/global_ecosystem/global_core_ecosystem/global_adult_content_core_ecosystem",
        )

    def test_catalog_has_expected_orientation_labels(self):
        catalog = get_catalog()
        labels = {item["id"] for item in catalog["orientation_labels"]}
        self.assertTrue({"STRAIGHT", "GAY", "BISEXUAL", "OTHER", "UNSPECIFIED"} <= labels)
        self.assertFalse(catalog["orientation_inference_enabled"])

    def test_bisexual_is_not_scene_configuration(self):
        item = get_orientation("bisexual")
        self.assertIsNotNone(item)
        self.assertIn("more than one gender", item["definition"])
        self.assertNotEqual(Orientation.BISEXUAL.value, "MULTIPLE_GENDERS")

    def test_unknown_orientation_is_not_inferred(self):
        self.assertIsNone(get_orientation("unknown"))
        self.assertIsNone(get_orientation(""))

    def test_policy_fails_closed_when_evidence_missing(self):
        result = evaluate_content_metadata(PolicyEvidence())
        self.assertFalse(result["allowed"])
        self.assertIn("ALL_DEPICTED_PERSONS_VERIFIED_ADULTS", result["reasons"])

    def test_policy_allows_only_complete_attestation_set(self):
        evidence = PolicyEvidence(
            all_depicted_persons_verified_adults=True,
            informed_consent_documented=True,
            distribution_rights_documented=True,
            moderation_approved=True,
            jurisdiction_permitted=True,
        )
        self.assertTrue(evaluate_content_metadata(evidence)["allowed"])

    def test_prohibited_content_always_blocks(self):
        evidence = PolicyEvidence(
            all_depicted_persons_verified_adults=True,
            informed_consent_documented=True,
            distribution_rights_documented=True,
            moderation_approved=True,
            jurisdiction_permitted=True,
            prohibited_content_detected=True,
        )
        self.assertFalse(evaluate_content_metadata(evidence)["allowed"])


if __name__ == "__main__":
    unittest.main()
