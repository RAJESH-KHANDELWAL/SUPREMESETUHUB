import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_people_life_api_ecosystem.adult_media_pornography_18_plus.classification import (
    validate_adult_media_classification,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_security_core_ecosystem.content_safety_policy import (
    validate_content_safety_metadata,
)
from backend.engine.global_ecosystem.global_engine_ecosystem.global_people_life_engine_ecosystem.adult_media_pornography_18_plus.engine import (
    validate_classification_payload,
)
from backend.global_ecosystem.global_app_ecosystem.domain_runtime import (
    AppDomainService,
    DomainValidationError,
)

from backend.core.global_ecosystem.global_core_ecosystem.global_people_life_core_ecosystem.adult_media_pornography_18_plus.taxonomy import (
    AdultContentClassificationError,
    get_classification_catalog,
    validate_classification_metadata,
)


class AdultMediaTaxonomyTests(unittest.TestCase):
    def test_orientation_labels_are_present(self):
        catalog = get_classification_catalog()
        labels = {item["id"] for item in catalog["orientation_labels"]}
        self.assertTrue({"STRAIGHT", "GAY", "BISEXUAL", "OTHER", "UNSPECIFIED"} <= labels)
        self.assertFalse(catalog["orientation_inference_enabled"])

    def test_content_label_requires_declared_source_and_subject(self):
        record = validate_classification_metadata({
            "orientation_label": "BISEXUAL",
            "orientation_source": "SELF_DECLARED",
            "classification_subject_type": "PERFORMER",
            "participant_configuration": "MULTIPLE_GENDERS",
        })
        self.assertEqual(record["orientation_label"], "BISEXUAL")
        self.assertFalse(record["orientation_inferred"])

    def test_scene_configuration_is_separate_from_orientation(self):
        record = validate_classification_metadata({
            "orientation_label": "BISEXUAL",
            "orientation_source": "SELF_DECLARED",
            "classification_subject_type": "CREATOR",
            "participant_configuration": "SAME_GENDER",
        })
        self.assertEqual(record["participant_configuration"], "SAME_GENDER")

    def test_inference_is_rejected(self):
        with self.assertRaises(AdultContentClassificationError):
            validate_classification_metadata({
                "orientation_label": "GAY",
                "orientation_source": "SELF_DECLARED",
                "classification_subject_type": "PERFORMER",
                "orientation_inferred": True,
            })

    def test_viewer_profile_is_rejected(self):
        with self.assertRaises(AdultContentClassificationError):
            validate_classification_metadata({"viewer_profile": {"orientation": "GAY"}})

    def test_unknown_labels_are_rejected(self):
        with self.assertRaises(AdultContentClassificationError):
            validate_classification_metadata({"orientation_label": "UNKNOWN"})

    def test_api_adapter_uses_canonical_core_contract(self):
        record = validate_adult_media_classification({
            "orientation_label": "STRAIGHT",
            "orientation_source": "SELF_DECLARED",
            "classification_subject_type": "CREATOR",
        })
        self.assertEqual(record["orientation_label"], "STRAIGHT")

    def test_security_core_rejects_inferred_orientation(self):
        with self.assertRaises(ValueError):
            validate_content_safety_metadata({
                "content_class": "AGE_RESTRICTED_ADULT",
                "age_gate_configured": True,
                "age_assurance_policy_ref": "age-policy-v1",
                "orientation_label": "GAY",
                "orientation_source": "SELF_DECLARED",
                "classification_subject_type": "PERFORMER",
                "orientation_inferred": True,
            })

    def test_engine_boundary_validates_classification(self):
        record = validate_classification_payload({
            "orientation_label": "BISEXUAL",
            "orientation_source": "AUTHORIZED_RIGHTS_HOLDER",
            "classification_subject_type": "PERFORMER",
        })
        self.assertEqual(record["orientation_label"], "BISEXUAL")

    def test_app_runtime_rejects_inferred_orientation(self):
        service = AppDomainService("adult_entertainment_streaming_apps")
        payload = {
            "action": "validate",
            "age_verified": True,
            "participants_are_adults": True,
            "consent_confirmed": True,
            "rights_cleared": True,
            "content_classification": {
                "orientation_label": "GAY",
                "orientation_source": "SELF_DECLARED",
                "classification_subject_type": "PERFORMER",
                "orientation_inferred": True,
            },
        }
        with self.assertRaises(DomainValidationError):
            service.validate(payload)


if __name__ == "__main__":
    unittest.main()
