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
    assert profile.server_env == "DRRAJESHKHANDELWALIBC_FTP_HOST"
    assert profile.name_env == "DRRAJESHKHANDELWALIBC_FTP_NAME"
    assert profile.username_env == "DRRAJESHKHANDELWALIBC_FTP_USER"
    assert profile.password_env == "DRRAJESHKHANDELWALIBC_FTP_PASSWORD"
    assert profile.port_env == "DRRAJESHKHANDELWALIBC_FTP_PORT"


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


def test_one_shared_ftp_account_resolves_for_all_five_logical_profiles():
    shared = {
        "FTP_SERVER": "ftps.example.invalid",
        "FTP_USERNAME": "shared-ftp-user",
        "FTP_PASSWORD": "shared-ftp-secret",
        "FTP_PORT": "21",
        "FTP_TIMEOUT": "23",
    }
    resolved = [profile.resolve(shared) for profile in FTP_PROFILES]
    assert len(resolved) == 5
    assert all(item["configured"] is True for item in resolved)
    assert {item["host"] for item in resolved} == {"ftps.example.invalid"}
    assert {item["username"] for item in resolved} == {"shared-ftp-user"}
    assert {item["password"] for item in resolved} == {"shared-ftp-secret"}
    assert {item["port"] for item in resolved} == {21}
    assert {item["timeout"] for item in resolved} == {23}
    assert len({item["identity_code"] for item in resolved}) == 5


def test_identity_specific_ftp_settings_override_shared_account():
    profile = get_ftp_profile("drrajeshkhandelwalibc")
    values = profile.resolve({
        "FTP_SERVER": "shared.example.invalid",
        "FTP_USERNAME": "shared-user",
        "FTP_PASSWORD": "shared-secret",
        "DRRAJESHKHANDELWALIBC_FTP_HOST": "brand.example.invalid",
        "DRRAJESHKHANDELWALIBC_FTP_NAME": "IBC isolated profile",
        "DRRAJESHKHANDELWALIBC_FTP_USER": "brand-user",
        "DRRAJESHKHANDELWALIBC_FTP_PASSWORD": "brand-secret",
        "DRRAJESHKHANDELWALIBC_FTP_PORT": "2121",
    })
    assert values["host"] == "brand.example.invalid"
    assert values["username"] == "brand-user"
    assert values["password"] == "brand-secret"
    assert values["port"] == 2121


def test_invalid_shared_ftp_timeout_does_not_mark_profile_configured():
    profile = get_ftp_profile("supremesetuhub")
    values = profile.resolve({
        "FTP_SERVER": "ftp.example.invalid",
        "FTP_USERNAME": "user",
        "FTP_PASSWORD": "secret",
        "FTP_TIMEOUT": "999",
    })
    assert values["configured"] is False
