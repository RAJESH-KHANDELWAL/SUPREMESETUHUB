from backend.core.global_ecosystem.global_core_ecosystem.partner_programs import get_partner_program_catalog
from backend.core.global_ecosystem.global_core_ecosystem.hostinger_referrals import get_hostinger_referral_accounts


def test_hostinger_referral_program_uses_current_primary_owner_link():
    records = get_partner_program_catalog()
    assert len(records) == 1
    assert records[0]["provider_id"] == "HOSTINGER"
    accounts = records[0]["referral_accounts"]
    official = next(account for account in accounts if account["identity_id"] == "DRRAJESHKHANDELWALIBCOFFICIAL")
    assert official["referral_code"] == "RAJESHIBCGROWTH"
    assert official["referral_url"] == "https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGROWTH"
    assert official["account_email"] == "drrajeshkhandelwalibcofficial@gmail.com"
    assert official["dashboard_label"] == "DR RAJESH KHANDELWAL IBC OFFICIAL"
    assert records[0]["referral_url"] == "https://www.hostinger.com/in?REFERRALCODE=RAJESHIBCGLOBAL"
    assert records[0]["provider_dashboard_is_source_of_truth"] is True
    assert records[0]["purchases_visible_to_supreme_without_provider_api"] is False
    assert records[0]["capture_personal_data_without_consent"] is False


def test_all_four_owner_referral_links_are_registered_and_within_hostinger_limit():
    accounts = get_hostinger_referral_accounts()
    assert len(accounts) == 4
    assert sum(1 for account in accounts if account["primary"]) == 1
    for account in accounts:
        code = account["referral_code"]
        assert 6 <= len(code) <= 15
        assert code.isalnum()
        assert account["referral_url"] == f"https://www.hostinger.com/in?REFERRALCODE={code}"


def test_partner_program_catalog_returns_independent_records():
    first = get_partner_program_catalog()
    first[0]["status"] = "ACTIVE_VERIFIED"
    first[0]["referral_accounts"][0]["referral_code"] = "CHANGED"
    fresh = get_partner_program_catalog()[0]
    assert fresh["status"] == "CONFIGURED_NOT_VERIFIED_LIVE"
    assert fresh["referral_accounts"][0]["referral_code"] == "RAJESHIBCGLOBAL"
