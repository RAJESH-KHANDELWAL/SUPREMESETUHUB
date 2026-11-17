import unittest

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


if __name__ == "__main__":
    unittest.main()
