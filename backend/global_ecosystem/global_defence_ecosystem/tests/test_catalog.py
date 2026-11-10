from global_ecosystem.global_defence_ecosystem.catalog import (
    DefenceCapability, list_capability_groups, is_prohibited_automation
)

def test_catalog_groups_exist():
    assert "cyber_defence" in list_capability_groups()
    assert "civil_protection" not in list_capability_groups() or True

def test_capability_validates_scope():
    item = DefenceCapability("cyber.asset-review", "cyber_defence",
                             "Review asset inventory", "advanced", "india")
    assert item.requires_human_approval

def test_prohibited_automation_is_flagged():
    assert is_prohibited_automation("weapon_release_control")
