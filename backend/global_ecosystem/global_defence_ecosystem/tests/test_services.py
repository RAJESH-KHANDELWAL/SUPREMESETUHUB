from global_ecosystem.global_defence_ecosystem.risk import evaluate_use_case
from global_ecosystem.global_defence_ecosystem.civil_protection import build_response_checklist
from global_ecosystem.global_defence_ecosystem.cyber_defence import assess_control_coverage
from global_ecosystem.global_defence_ecosystem.readiness import assess_readiness

def test_risk_requires_safeguards():
    result = evaluate_use_case("Emergency coordination", [])
    assert not result["allowed_for_catalogue"]

def test_emergency_checklist():
    result = build_response_checklist("flood")
    assert result["human_command_required"]

def test_control_coverage():
    assert assess_control_coverage(["asset_inventory"])["coverage_ratio"] > 0

def test_readiness_requires_all_dimensions():
    assert not assess_readiness({"people": 4})["complete"]
