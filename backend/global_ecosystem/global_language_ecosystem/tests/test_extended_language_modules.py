"""Tests for extended language metadata modules."""
import pytest
from global_language_ecosystem.writing_systems import get_writing_system_catalog
from global_language_ecosystem.dialects import build_dialect_profile
from global_language_ecosystem.language_detection import validate_detection_result
from global_language_ecosystem.language_detection.service import DetectionResult
from global_language_ecosystem.interpretation import build_interpretation_request
from global_language_ecosystem.moderation import review_content_policy_flags

def test_writing_system_catalog_includes_indic_scripts():
 assert "Devanagari" in get_writing_system_catalog()["indic"]

def test_dialect_profile_requires_region():
 with pytest.raises(ValueError): build_dialect_profile("hi", "Braj", "")

def test_detection_confidence_range():
 with pytest.raises(ValueError): validate_detection_result(DetectionResult("en", 1.2))

def test_interpretation_mode():
 assert build_interpretation_request("hi", "en", mode="simultaneous").mode == "simultaneous"

def test_moderation_flags_are_allowlisted():
 assert review_content_policy_flags(("sexual_content_involving_minors", "random")) == ("sexual_content_involving_minors",)
