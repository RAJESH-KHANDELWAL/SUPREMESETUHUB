from ..adult_content_technology import AdultPlatformControls, assess_platform_controls
from ..governance import validate_release_gate
def test_adult_controls_report_missing_items():
    result = assess_platform_controls(AdultPlatformControls(False,False,False,False,False,False,False,False))
    assert result["status"] == "CONTROLS_INCOMPLETE"
    assert len(result["missing_controls"]) == 8
def test_release_gate_requires_all_controls():
    result = validate_release_gate(tests_passed=True,security_reviewed=True,privacy_reviewed=True,rollback_ready=True,owner_approved=False)
    assert result["release_gate_passed"] is False
