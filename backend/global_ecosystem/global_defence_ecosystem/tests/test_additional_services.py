from global_ecosystem.global_defence_ecosystem.disaster_response import build_resource_plan
from global_ecosystem.global_defence_ecosystem.emergency_communications import build_message_record
from global_ecosystem.global_defence_ecosystem.infrastructure_resilience import assess_dependencies
from global_ecosystem.global_defence_ecosystem.governance import check_governance

def test_resource_plan_requires_population():
    assert build_resource_plan("flood", 100)["population_estimate"] == 100

def test_message_requires_authority():
    try:
        build_message_record("Alert", "Hindi", "")
    except ValueError:
        pass
    else:
        raise AssertionError("issuing authority should be required")

def test_dependency_map_flags_unmapped_sectors():
    result = assess_dependencies({"energy": ["telecommunications"]})
    assert "water" in result["sectors_without_mapping"]

def test_governance_requires_all_controls():
    assert not check_governance([])["complete"]
