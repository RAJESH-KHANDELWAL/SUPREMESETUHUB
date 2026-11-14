from backend.infrastructure.ftp.profiles import FTP_PROFILES, get_ftp_profile


def test_five_ftp_profiles_are_named_for_the_main_system_and_four_identities():
    assert [profile.profile_id for profile in FTP_PROFILES] == [
        "supremesetuhub",
        "rajeshkhandelwalofficial",
        "rajeshkhandelwal",
        "drrajeshkhandelwalibcofficial",
        "drrajeshkhandelwalibc",
    ]


def test_profile_environment_names_follow_brand_identity():
    profile = get_ftp_profile("drrajeshkhandelwalibc")
    assert profile.server_env == "HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_SERVER"
    assert profile.username_env == "HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_USERNAME"
    assert profile.password_env == "HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_PASSWORD"


def test_missing_ftp_credentials_are_reported_without_fallback():
    profile = get_ftp_profile("rajeshkhandelwal")
    result = profile.resolve({})
    assert result["configured"] is False
    assert result["server_configured"] is False
    assert result["username_configured"] is False
    assert result["password_configured"] is False


def test_ftp_password_is_never_required_to_be_a_database_password():
    profile = get_ftp_profile("rajeshkhandelwalofficial")
    values = profile.resolve({
        profile.server_env: "ftp.example.invalid",
        profile.username_env: "actual-ftp-account",
        profile.password_env: "ftp-secret",
    })
    assert values["configured"] is True
    assert values["password"] == "ftp-secret"
