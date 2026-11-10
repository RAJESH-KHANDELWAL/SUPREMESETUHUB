from global_ecosystem.global_defence_ecosystem.regional import resolve_region
from global_ecosystem.global_defence_ecosystem.incident_management import create_incident_record, transition_incident
from global_ecosystem.global_defence_ecosystem.training import build_exercise_plan
from global_ecosystem.global_defence_ecosystem.logistics import build_supply_request

def test_india_region_has_local_review():
    assert resolve_region("India")["requires_local_legal_review"]

def test_incident_transition_requires_approval():
    item = create_incident_record("INC-1", "power_outage", "operator")
    updated = transition_incident(item, "triaged", "duty_manager")
    assert updated["state"] == "triaged"

def test_exercise_plan_requires_objectives():
    plan = build_exercise_plan("Continuity drill", "tabletop", ["test call tree"])
    assert plan["requires_after_action_review"]

def test_relief_supply_is_draft_only():
    item = build_supply_request("REQ-1", "safe_water", 100, "litres")
    assert item["status"] == "DRAFT_REQUIRES_AUTHORIZATION"
