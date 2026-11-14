from backend.infrastructure.ftp.profiles import FTP_PROFILES, get_ftp_profile


def test_five_ftp_profiles_are_named_for_the_main_system_and_four_identities():
    assert [profile.profile_id for profile in FTP_PROFILES] == [
        "supremesetuhub",
        "rajeshkhandelwalofficial",
        "rajeshkhandelwal",
        "drrajeshkhandelwalibcofficial",
        "drrajeshkhandelwalibc",
    ]


def test_profile_environment_names_follow_requested_host_name_user_password_port_pattern():
    profile = get_ftp_profile("drrajeshkhandelwalibc")
    assert profile.server_env == "DRRAJESHKANDELWALIBC_FTP_HOST"
    assert profile.name_env == "DRRAJESHKANDELWALIBC_FTP_NAME"
    assert profile.username_env == "DRRAJESHKANDELWALIBC_FTP_USER"
    assert profile.password_env == "DRRAJESHKANDELWALIBC_FTP_PASSWORD"
    assert profile.port_env == "DRRAJESHKANDELWALIBC_FTP_PORT"


def test_missing_ftp_credentials_are_reported_without_fallback():
    profile = get_ftp_profile("rajeshkhandelwal")
    result = profile.resolve({})
    assert result["configured"] is False
    assert result["server_configured"] is False
    assert result["name_configured"] is False
    assert result["username_configured"] is False
    assert result["password_configured"] is False


def test_profile_resolves_all_five_requested_fields():
    profile = get_ftp_profile("rajeshkhandelwalofficial")
    values = profile.resolve({
        profile.server_env: "ftp.example.invalid",
        profile.name_env: "RAJESHKHANDELWALOFFICIAL",
        profile.username_env: "actual-ftp-account",
        profile.password_env: "ftp-secret",
        profile.port_env: "21",
    })
    assert values["configured"] is True
    assert values["host"] == "ftp.example.invalid"
    assert values["name"] == "RAJESHKHANDELWALOFFICIAL"
    assert values["username"] == "actual-ftp-account"
    assert values["password"] == "ftp-secret"
    assert values["port"] == 21


def test_invalid_or_blank_port_does_not_mark_profile_configured():
    profile = get_ftp_profile("supremesetuhub")
    values = profile.resolve({
        profile.server_env: "ftp.example.invalid",
        profile.name_env: "SUPREMESETUHUB",
        profile.username_env: "actual-ftp-account",
        profile.password_env: "ftp-secret",
        profile.port_env: "",
    })
    assert values["configured"] is False
