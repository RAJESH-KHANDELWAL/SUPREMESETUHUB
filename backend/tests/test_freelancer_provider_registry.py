from backend.engines.freelancer_ecosystem.providers import get_freelancer_provider_status


def test_provider_catalog_contains_google_microsoft_aws_and_apple(monkeypatch):
    for key in (
        "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET",
        "GOOGLE_CLOUD_PROJECT", "GOOGLE_CLOUD_STORAGE_BUCKET",
        "MICROSOFT_CLIENT_ID", "MICROSOFT_TENANT_ID", "AWS_S3_BUCKET",
        "APPLE_CLIENT_ID", "APPLE_TEAM_ID", "APPLE_KEY_ID", "APPLE_PRIVATE_KEY",
    ):
        monkeypatch.delenv(key, raising=False)

    result = get_freelancer_provider_status()
    providers = {item["provider_id"]: item for item in result["providers"]}

    assert {
        "google_drive",
        "google_cloud_storage",
        "microsoft_onedrive",
        "aws_s3",
        "apple_sign_in",
    }.issubset(providers)
    assert result["connected_provider_count"] == 0
    assert all(item["connected"] is False for item in providers.values())


def test_apple_sign_in_is_not_misrepresented_as_icloud_storage():
    result = get_freelancer_provider_status()
    apple = next(item for item in result["providers"] if item["provider_id"] == "apple_sign_in")

    assert apple["category"] == "IDENTITY"
    assert "not an iCloud Drive file-storage adapter" in apple["limitation"]


def test_provider_status_never_returns_secret_values(monkeypatch):
    monkeypatch.setenv("GOOGLE_CLIENT_ID", "example-client-id")
    monkeypatch.setenv("GOOGLE_CLIENT_SECRET", "do-not-return-this-secret")

    result = get_freelancer_provider_status()
    rendered = repr(result)

    assert "do-not-return-this-secret" not in rendered
    assert "example-client-id" not in rendered
