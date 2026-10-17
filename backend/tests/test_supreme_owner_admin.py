from backend.api.supreme_ecosystem import require_supreme_ecosystem_owner, router as supreme_ecosystem_router
from backend.api.businesses import router as businesses_router
from backend.security.dependencies import get_current_user
from backend.api.global_business_coach import public_business_coach_profile, global_business_coach_keywords
from backend.supreme.social_media_control.registry import social_platform_status
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


def test_public_global_business_coach_profile_exposes_only_public_contact_data(monkeypatch):
    monkeypatch.setenv("GLOBAL_BUSINESS_COACH_EMAIL", "DRRAJESHKHANDELWALIBC@GMAIL.COM")
    monkeypatch.setenv("GLOBAL_BUSINESS_COACH_WEBSITE", "https://drrajeshkhandelwalibc.com")
    monkeypatch.setenv("GLOBAL_BUSINESS_COACH_SOCIAL_USERNAME", "DRRAJESHKHANDELWALIBC")
    monkeypatch.setenv("GLOBAL_BUSINESS_COACH_WHATSAPP_NUMBER", "917611967229")
    payload = public_business_coach_profile()
    assert payload["success"] is True
    assert payload["contact"]["email"] == "drrajeshkhandelwalibc@gmail.com"
    assert payload["contact"]["whatsapp_url"] == "https://wa.me/917611967229"
    assert payload["social"]["handle"] == "@DRRAJESHKHANDELWALIBC"
    assert payload["social"]["profile_urls_verified"] is False
    assert "oauth" not in repr(payload).casefold()
    assert "application_password" not in repr(payload).casefold()


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


def test_keyword_foundation_is_short_and_covers_bharat_and_global_intent():
    payload = global_business_coach_keywords()
    assert payload["success"] is True
    assert payload["audience"] == ["BHARAT", "GLOBAL WORLD"]
    assert payload["search_volume_verified"] is False
    assert "business coach" in payload["groups"]["CORE_BRAND"]
    assert "freelance work India" in payload["groups"]["BHARAT_INTENT"]
    assert "global consulting" in payload["groups"]["GLOBAL_INTENT"]
    assert all(len(keyword.split()) <= 4 for group in payload["groups"].values() for keyword in group)


def test_social_registry_lists_platforms_without_exposing_secret_values(monkeypatch):
    monkeypatch.setenv("META_ACCESS_TOKEN", "must-never-be-returned")
    payload = social_platform_status()
    ids = {item["platform_id"] for item in payload["platforms"]}
    assert {"FACEBOOK", "INSTAGRAM", "LINKEDIN", "X", "WHATSAPP", "YOUTUBE", "TELEGRAM"} <= ids
    assert all(item["connected"] is False for item in payload["platforms"])
    assert all(item["publishing_enabled"] is False for item in payload["platforms"])
    assert "must-never-be-returned" not in repr(payload)




def test_role_governance_catalog_covers_leadership_permissions_and_workflows():
    from backend.supreme.role_governance import role_governance_catalog

    payload = role_governance_catalog()
    roles = {role["role_id"]: role for role in payload["role_templates"]}
    assert {"PRIMARY_OWNER", "OWNER", "FOUNDER", "CO_FOUNDER", "CEO", "CMD", "MD", "CMA", "ADMIN", "MANAGER", "MEMBER", "CUSTOM"} <= set(roles)
    assert payload["roles_are_permissions"] is False
    assert "finance.approve_payments" in payload["permission_catalog"]
    assert "work.assign" in payload["permission_catalog"]
    assert "promotion.approve" in payload["permission_catalog"]
    assert {"WORK", "PROGRESS", "PROMOTION", "LEARNING", "EARNING", "VERIFICATION"} <= set(payload["workflow_sections"])
    assert roles["CMA"]["category"] == "PROFESSIONAL_DESIGNATION"
    assert roles["CMA"]["default_permissions"] == []
    assert roles["FOUNDER"]["can_transfer_ownership"] is False
    assert payload["persistence_status"] == "TEMPLATE_CATALOG_ONLY"
    assert payload["assignment_enforcement_status"] == "NOT_IMPLEMENTED_IN_THIS_CATALOG"


def test_role_governance_catalog_is_for_authenticated_business_platform_users():
    routes = {
        route.path: route
        for route in businesses_router.routes
        if getattr(route, "methods", None)
    }
    path = "/role-governance/catalog"
    assert path in routes
    assert any(
        dependency.call is get_current_user
        for dependency in routes[path].dependant.dependencies
    )
    owner_admin_routes = {
        route.path
        for route in supreme_ecosystem_router.routes
        if getattr(route, "methods", None)
    }
    assert "/api/v1/supreme-ecosystem/owner-admin/role-governance" not in owner_admin_routes
