from backend.core.global_ecosystem.global_core_ecosystem.global_language_core_ecosystem import (
    GlobalLanguageCoreOrchestrator, GlobalLanguageCoreService,
    get_catalog, get_domain, get_domains, get_service_tiers,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_language_core_ecosystem.policy import adult_content_policy,redact_sensitive_metadata

def test_two_separate_language_divisions_exist():
    c=get_catalog()
    assert [x["division_id"] for x in c["divisions"]]==["HUMAN-LANGUAGES","PROGRAMMING-LANGUAGES"]
    assert len(get_domains("HUMAN"))>0
    assert len(get_domains("PROGRAMMING"))>0

def test_programming_language_group_is_separate():
    assert get_domain("GLOBAL_PROGRAMMING_LANGUAGES") is not None
    assert get_domain("PYTHON") is None  # individual language records are a later catalog population task

def test_bharat_and_global_human_language_domains_exist():
    assert get_domain("BHARAT_INDIC_LANGUAGES") is not None
    assert get_domain("GLOBAL_NATURAL_HUMAN_LANGUAGES") is not None
    assert get_domain("SIGNED_LANGUAGES") is not None

def test_adult_language_scope_requires_age_and_consent():
    adult=get_domain("ADULT_LANGUAGE")
    assert adult["age_restricted"] is True and adult["consent_required"] is True
    policy=adult_content_policy()
    assert policy["verified_adults_only"] is True
    assert "sexual content involving minors" in policy["prohibited"]

def test_service_tiers_cover_normal_to_supreme():
    tiers=get_service_tiers()
    assert tiers[0]["tier_id"]=="NORMAL"
    assert tiers[-1]["tier_id"]=="SUPREME"
    assert [x["rank"] for x in tiers]==list(range(1,8))

def test_catalog_is_read_only_and_redacts_secrets():
    service=GlobalLanguageCoreService()
    assert service.health()["success"] is True
    data={"provider":"google","api_key":"hidden","region":"global"}
    clean=redact_sensitive_metadata(data)
    assert "api_key" not in clean and clean["region"]=="global"
    assert GlobalLanguageCoreOrchestrator().health()["execution_enabled"] is False
