from backend.api.global_ecosystem.global_api_ecosystem.oracle_api_ecosystem.config import OCIConfig


def test_config_reports_missing_required_values():
    config = OCIConfig("", "", "", "")
    missing = config.validate()
    assert "OCI_TENANCY_OCID" in missing
    assert "OCI_USER_OCID" in missing
    assert "OCI_FINGERPRINT" in missing
    assert "OCI_REGION" in missing
    assert "OCI_PRIVATE_KEY_FILE or OCI_PRIVATE_KEY_PEM" in missing


def test_config_builds_key_id_and_accepts_pem():
    config = OCIConfig(
        tenancy_ocid="tenancy",
        user_ocid="user",
        fingerprint="fingerprint",
        region="ap-mumbai-1",
        private_key_pem="test-key",
    )
    assert config.key_id == "tenancy/user/fingerprint"
    assert config.validate() == []
