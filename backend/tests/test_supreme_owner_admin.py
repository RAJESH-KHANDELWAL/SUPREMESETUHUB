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
    assert status["google_owner_account_tier"] == "ALL_PRIMARY"
    assert "WORDPRESS SITES" in status["controlled_domains"]
    assert "GOOGLE ACCOUNTS AND SERVICES" in status["controlled_domains"]


def test_global_business_coach_contact_covers_bharat_and_global_business_audience(monkeypatch):
    monkeypatch.delenv("GLOBAL_BUSINESS_COACH_EMAIL", raising=False)
    profile = SupremeOwnerAdminService().global_business_coach_profile()
    assert profile["contact_email"] == "drrajeshkhandelwalibc@gmail.com"
    assert profile["website"] == "https://drrajeshkhandelwalibc.com"
    assert profile["role"] == "GLOBAL BUSINESS COACH AND INDEPENDENT BUSINESS CONSULTANT"
    assert "BHARAT AND GLOBAL WORLD" in profile["audience"]
    assert "ENTREPRENEURS AND STARTUP FOUNDERS" in profile["audience"]
    assert "BUSINESS NETWORKING AND COLLABORATION" in profile["scope"]
    assert profile["automatic_forwarding_enabled"] is False
    assert profile["mailbox_connection_verified"] is False
    assert profile["social_identity"]["intended_username"] == "DRRAJESHKHANDELWALIBC"
    assert profile["social_identity"]["username_availability_verified"] is False
    assert profile["contact_channels"]["whatsapp"]["url"] == "https://wa.me/917611967229"
    assert profile["contact_channels"]["website_form"]["configured"] is False


def test_global_business_coach_contact_can_be_configured(monkeypatch):
    monkeypatch.setenv("GLOBAL_BUSINESS_COACH_EMAIL", "DRRAJESHKHANDELWALIBC@GMAIL.COM")
    profile = SupremeOwnerAdminService().global_business_coach_profile()
    assert profile["contact_email"] == "drrajeshkhandelwalibc@gmail.com"


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


def test_all_google_owner_emails_are_primary_and_can_scale_to_many_accounts(monkeypatch):
    monkeypatch.setenv(
        "GOOGLE_OWNER_ACCOUNT_EMAILS",
        "rajeshkhandelwal1996@gmail.com;rajeshkhandelwalofficial1996@gmail.com;third@example.test",
    )
    monkeypatch.setenv("SUPREME_OWNER_EMAILS", "fourth@example.test")
    monkeypatch.setenv("SUPREME_OWNER_PRIMARY_EMAIL", "owner@example.test")
    monkeypatch.setenv("SUPREME_OWNER_SECONDARY_EMAIL", "owner@example.test")
    monkeypatch.setenv("SUPREME_OWNER_RECOVERY_EMAIL", "recovery@example.test")
    accounts = SupremeOwnerAdminService().google_owner_accounts()
    by_email = {account["email"]: account for account in accounts}
    assert len(accounts) == 6
    assert by_email["rajeshkhandelwal1996@gmail.com"]["owner_account_tier"] == "PRIMARY"
    assert by_email["rajeshkhandelwalofficial1996@gmail.com"]["owner_account_tier"] == "PRIMARY"
    assert all(account["owner_account_tier"] == "PRIMARY" for account in accounts)
    assert all("BANKING_AND_FINANCIAL_NOTIFICATIONS" in account["purposes"] for account in accounts)
    assert all("SENSITIVE_DOCUMENTS_AND_RECORDS" in account["purposes"] for account in accounts)


def test_google_owner_accounts_deduplicate_and_never_expose_oauth_secrets(monkeypatch):
    monkeypatch.setenv("GOOGLE_OWNER_ACCOUNT_EMAILS", "OWNER@example.test;owner@example.test")
    monkeypatch.setenv("SUPREME_OWNER_PRIMARY_EMAIL", "owner@example.test")
    monkeypatch.setenv("GOOGLE_CLIENT_SECRET", "secret-do-not-return")
    payload = SupremeOwnerAdminService().governance()
    assert len(payload["google_owner_accounts"]) == 1
    assert payload["google_owner_accounts"][0]["owner_account_tier"] == "PRIMARY"
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
        "/api/v1/supreme-ecosystem/owner-admin/business-coach-profile",
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
