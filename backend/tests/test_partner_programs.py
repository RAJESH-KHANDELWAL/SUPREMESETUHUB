from backend.core.global_ecosystem.global_core_ecosystem.partner_programs import get_partner_program_catalog


def test_hostinger_referral_program_uses_exact_owner_link():
    records = get_partner_program_catalog()
    assert len(records) == 1
    assert records[0]["provider_id"] == "HOSTINGER"
    assert records[0]["referral_url"] == "https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGLOBAL"
    assert records[0]["provider_dashboard_is_source_of_truth"] is True
    assert records[0]["purchases_visible_to_supreme_without_provider_api"] is False
    assert records[0]["capture_personal_data_without_consent"] is False


def test_partner_program_catalog_returns_independent_records():
    first = get_partner_program_catalog()
    first[0]["status"] = "ACTIVE_VERIFIED"
    assert get_partner_program_catalog()[0]["status"] == "CONFIGURED_NOT_VERIFIED_LIVE"
