from backend.api.supreme_ecosystem import require_supreme_ecosystem_owner, router as supreme_ecosystem_router
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
    assert "GOOGLE ACCOUNTS AND SERVICES" in status["controlled_domains"]


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


def test_google_owner_accounts_read_from_private_environment(monkeypatch):
    monkeypatch.setenv("SUPREME_OWNER_PRIMARY_EMAIL", "owner-one@example.test")
    monkeypatch.setenv("SUPREME_OWNER_SECONDARY_EMAIL", "owner-two@example.test")
    monkeypatch.delenv("GOOGLE_CLIENT_ID", raising=False)
    monkeypatch.delenv("GOOGLE_CLIENT_SECRET", raising=False)
    monkeypatch.delenv("GOOGLE_REDIRECT_URI", raising=False)
    accounts = SupremeOwnerAdminService().google_owner_accounts()
    assert [account["email"] for account in accounts] == [
        "owner-one@example.test",
        "owner-two@example.test",
    ]
    assert all("GMAIL" in account["approved_services"] for account in accounts)
    assert all("GOOGLE_DRIVE" in account["approved_services"] for account in accounts)
    assert all(account["connected"] is False for account in accounts)
    assert all(account["token_storage_status"] == "NOT_IMPLEMENTED" for account in accounts)


def test_google_owner_accounts_deduplicate_and_never_expose_oauth_secrets(monkeypatch):
    monkeypatch.setenv("GOOGLE_OWNER_ACCOUNT_EMAILS", "OWNER@example.test;owner@example.test")
    monkeypatch.setenv("SUPREME_OWNER_PRIMARY_EMAIL", "owner@example.test")
    monkeypatch.setenv("GOOGLE_CLIENT_SECRET", "secret-do-not-return")
    payload = SupremeOwnerAdminService().governance()
    assert len(payload["google_owner_accounts"]) == 1
    assert "secret-do-not-return" not in repr(payload)


def test_owner_status_never_returns_private_credentials(monkeypatch):
    monkeypatch.setenv("WORDPRESS_APPLICATION_PASSWORD", "do-not-return")
    payload = SupremeOwnerAdminService().governance()
    rendered = repr(payload)
    assert "do-not-return" not in rendered
    assert "WORDPRESS SITES" in OWNER_CONTROLLED_DOMAINS


def test_supreme_ecosystem_router_guards_owner_admin_endpoints():
    assert any(
        dependency.dependency is require_supreme_ecosystem_owner
        for dependency in supreme_ecosystem_router.dependencies
    )
    protected_paths = {
        "/api/v1/supreme-ecosystem/owner-admin/status",
        "/api/v1/supreme-ecosystem/owner-admin/owned-platforms",
        "/api/v1/supreme-ecosystem/owner-admin/google-accounts",
        "/api/v1/supreme-ecosystem/owner-admin/governance",
    }
    routes = {
        route.path: route
        for route in supreme_ecosystem_router.routes
        if getattr(route, "methods", None)
    }
    assert protected_paths <= set(routes)
    for path in protected_paths:
        assert any(
            dependency.call is require_supreme_ecosystem_owner
            for dependency in routes[path].dependant.dependencies
        )
