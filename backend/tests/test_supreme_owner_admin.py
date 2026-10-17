from backend.supreme.supreme_owner_admin.service import (
    OWNER_CONTROLLED_DOMAINS,
    SupremeOwnerAdminService,
)


def test_owner_admin_is_single_owner_private_control_plane():
    status = SupremeOwnerAdminService().owner_status()
    assert status["control_plane"] == "SUPREME_OWNER_ADMIN"
    assert status["privacy"] == "OWNER_ONLY"
    assert status["single_owner_policy"] is True
    assert status["self_service_owner_signup"] is False
    assert "WORDPRESS SITES" in status["controlled_domains"]


def test_wordpress_sites_are_in_owner_platform_registry(monkeypatch):
    monkeypatch.setenv("WORDPRESS_SITE_URL", "https://example.test")
    monkeypatch.setenv("WORDPRESS_USERNAME", "owner")
    monkeypatch.setenv("WORDPRESS_APPLICATION_PASSWORD", "private-test-value")
    sites = SupremeOwnerAdminService().owned_platforms()
    by_id = {site["site_id"]: site for site in sites}
    assert {"rajeshkhandelwalofficial", "drrajeshkhandelwalibc"} <= set(by_id)
    assert by_id["rajeshkhandelwalofficial"]["credentials_configured"] is True
    assert by_id["rajeshkhandelwalofficial"]["live_connection_verified"] is False
    assert "application_password" not in by_id["rajeshkhandelwalofficial"]


def test_owner_status_never_returns_private_credentials(monkeypatch):
    monkeypatch.setenv("WORDPRESS_APPLICATION_PASSWORD", "do-not-return")
    payload = SupremeOwnerAdminService().governance()
    rendered = repr(payload)
    assert "do-not-return" not in rendered
    assert "WORDPRESS SITES" in OWNER_CONTROLLED_DOMAINS
