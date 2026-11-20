"""GLOBAL CORE ECOSYSTEM catalog data and hierarchy manager in one module."""

from __future__ import annotations

from copy import deepcopy
from .global_communication_core_ecosystem.product_catalog import PROVIDER_DIRECTORY
from typing import Any


ROOT_ID = "GLOBAL-ECOSYSTEM"

ROOT: dict[str, Any] = {
    "ecosystem_id": ROOT_ID,
    "name": "GLOBAL ECOSYSTEM",
    "ecosystem_type": "MASTER",
    "repository_ref": None,
    "status": "REGISTERED",
    "enabled": True,
    "capabilities": [
        "CENTRAL_REGISTRY",
        "HIERARCHY",
        "DISCOVERY",
    ],
    "parent_id": None,
    "metadata": {},
}


# Canonical ecosystem categories, including API, CORE, Language, and Video hierarchies.
CATEGORIES: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "GLOBAL-SUPREME-ECOSYSTEM",
        "name": "GLOBAL SUPREME ECOSYSTEM",
        "ecosystem_type": "CORE",
        "capabilities": ["ADMINISTRATION", "PLATFORM_CONTROL", "INTEGRATION"],
    },
    {
        "ecosystem_id": "GLOBAL-PEOPLE-ECOSYSTEM",
        "name": "GLOBAL PEOPLE ECOSYSTEM",
        "ecosystem_type": "AUDIENCE",
        "capabilities": ["IDENTITY", "PROFILE", "COMMUNITY"],
    },
    {
        "ecosystem_id": "GLOBAL-BUSINESS-ECOSYSTEM",
        "name": "GLOBAL BUSINESS ECOSYSTEM",
        "ecosystem_type": "AUDIENCE",
        "capabilities": ["ORGANIZATION", "BUSINESS", "TEAM", "PROJECTS"],
    },
    {
        "ecosystem_id": "GLOBAL-ENTREPRENEUR-ECOSYSTEM",
        "name": "GLOBAL ENTREPRENEUR ECOSYSTEM",
        "ecosystem_type": "AUDIENCE",
        "capabilities": ["STARTUPS", "VENTURES", "BUSINESS_DEVELOPMENT"],
    },
    {
        "ecosystem_id": "GLOBAL-CLOUD-ECOSYSTEM",
        "name": "GLOBAL CLOUD ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["COMPUTE", "INFRASTRUCTURE", "NETWORKING"],
    },
    {
        "ecosystem_id": "GLOBAL-CLOUD-STORAGE-ECOSYSTEM",
        "name": "GLOBAL CLOUD STORAGE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["OBJECT_STORAGE", "FILE_STORAGE", "DATA_STORAGE"],
    },
    {
        "ecosystem_id": "GLOBAL-STORAGE-ECOSYSTEM",
        "name": "GLOBAL STORAGE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["STORAGE_CATALOG", "ADAPTERS", "ASSET_METADATA"],
    },
    {
        "ecosystem_id": "GLOBAL-SERVER-ECOSYSTEM",
        "name": "GLOBAL SERVER ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SERVER_MANAGEMENT", "DEPLOYMENT", "MONITORING"],
    },
    {
        "ecosystem_id": "GLOBAL-WEB-HOSTING-ECOSYSTEM",
        "name": "GLOBAL WEB & HOSTING ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["WEBSITES", "DOMAINS", "HOSTING", "CMS"],
    },
    {
        "ecosystem_id": "GLOBAL-SOCIAL-MEDIA-ECOSYSTEM",
        "name": "GLOBAL SOCIAL MEDIA ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SOCIAL_NETWORKS", "PUBLISHING", "COMMUNITIES"],
    },
    {
        "ecosystem_id": "GLOBAL-CREATOR-MEDIA-ECOSYSTEM",
        "name": "GLOBAL CREATOR & MEDIA ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "CREATOR_TOOLS",
            "MEDIA",
            "PUBLISHING",
            "MONETIZATION",
        ],
    },
    {
        "ecosystem_id": "GLOBAL-ADULT-ENTERTAINMENT-ECOSYSTEM",
        "name": "GLOBAL ADULT ENTERTAINMENT ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "AGE_RESTRICTED_SERVICES",
            "CREATOR_SERVICES",
            "PLATFORM_DISCOVERY",
        ],
        "metadata": {
            "age_restricted": True,
            "age_verification_required": True,
            "consent_and_rights_required": True,
            "legal_compliance_required": True,
        },
    },
    {
        "ecosystem_id": "GLOBAL-AI-AUTOMATION-ECOSYSTEM",
        "name": "GLOBAL AI & AUTOMATION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["AI_MODELS", "AI_APIS", "AUTOMATION"],
    },
    {
        "ecosystem_id": "GLOBAL-PAYMENT-COMMERCE-ECOSYSTEM",
        "name": "GLOBAL PAYMENT & COMMERCE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["PAYMENTS", "BILLING", "SUBSCRIPTIONS", "COMMERCE"],
    },
    {
        "ecosystem_id": "GLOBAL-IDENTITY-SECURITY-ECOSYSTEM",
        "name": "GLOBAL IDENTITY & SECURITY ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["AUTHENTICATION", "AUTHORIZATION", "PRIVACY"],
    },
    {
        "ecosystem_id": "GLOBAL-COMMUNICATION-ECOSYSTEM",
        "name": "GLOBAL COMMUNICATION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["EMAIL", "MESSAGING", "NOTIFICATIONS"],
    },
    {
        "ecosystem_id": "GLOBAL-DATA-DATABASE-ECOSYSTEM",
        "name": "GLOBAL DATA & DATABASE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["DATABASES", "DATA_EXCHANGE", "ANALYTICS"],
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-ECOSYSTEM",
        "name": "GLOBAL DEVELOPER ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["APIS", "SDKS", "REPOSITORIES", "CI_CD"],
    },

    # CORE hierarchy — mirrors the GLOBAL API ECOSYSTEM hierarchy.
    {
        "ecosystem_id": "GLOBAL-CORE-ECOSYSTEM",
        "name": "GLOBAL CORE ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": ["CORE_REGISTRY", "FOUNDATION_SERVICES", "LIFECYCLE"],
    },
    {
        "ecosystem_id": "GLOBAL-DATABASE-CORE-ECOSYSTEM",
        "name": "GLOBAL DATABASE CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["DATABASE_SERVICE", "MIGRATIONS", "TRANSACTIONS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-STORAGE-CORE-ECOSYSTEM",
        "name": "GLOBAL STORAGE CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["STORAGE_SERVICE", "ASSET_METADATA", "ADAPTERS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-API-CORE-ECOSYSTEM",
        "name": "GLOBAL API CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["API_SERVICE", "ROUTING", "CONTRACTS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-AI-CORE-ECOSYSTEM",
        "name": "GLOBAL AI CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["AI_ORCHESTRATION", "MODEL_ADAPTERS", "POLICY_GATES"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SEARCH-CORE-ECOSYSTEM",
        "name": "GLOBAL SEARCH CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["SEARCH_INDEXING", "DISCOVERY", "QUERY_ROUTING"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-BACKUP-CORE-ECOSYSTEM",
        "name": "GLOBAL BACKUP CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["BACKUP_POLICIES", "RESTORE_WORKFLOWS", "INTEGRITY_CHECKS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-LOGGING-CORE-ECOSYSTEM",
        "name": "GLOBAL LOGGING CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["STRUCTURED_LOGGING", "CORRELATION_IDS", "AUDIT_EVENTS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-NOTIFICATIONS-CORE-ECOSYSTEM",
        "name": "GLOBAL NOTIFICATIONS CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["NOTIFICATION_ROUTING", "TEMPLATES", "DELIVERY_STATUS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SETTINGS-CORE-ECOSYSTEM",
        "name": "GLOBAL SETTINGS CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["CONFIGURATION", "FEATURE_FLAGS", "ENVIRONMENT_SETTINGS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-BUSINESS-CORE-ECOSYSTEM",
        "name": "GLOBAL BUSINESS CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["BUSINESS_RULES", "DOMAIN_SERVICES", "WORKFLOWS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },

    {
        "ecosystem_id": "STRIPE-CORE-ECOSYSTEM",
        "name": "STRIPE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE",
        "capabilities": [
            "STRIPE_PROVIDER_REGISTRY",
            "PAYMENT_LIFECYCLE_ORCHESTRATION",
            "BILLING_AND_SUBSCRIPTION_ORCHESTRATION",
            "WEBHOOK_EVENT_ROUTING",
            "IDEMPOTENCY_POLICY",
            "TENANT_SCOPED_CONFIGURATION",
            "SECRET_REFERENCE_BOUNDARY",
            "AUDIT_AND_HEALTH_METADATA",
        ],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {
            "core_catalog": "backend/core/global_ecosystem/global_core_ecosystem/stripe_core_ecosystem",
            "api_catalog": "backend/api/global_ecosystem/global_api_ecosystem/stripe_api_ecosystem",
            "status": "CORE_CATALOG_ONLY",
            "live_connection_verified": False,
        },
    },
    {
        "ecosystem_id": "STRIPE-ACCOUNTS-CORE-ECOSYSTEM",
        "name": "STRIPE ACCOUNTS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CONNECT_ACCOUNT_METADATA", "ONBOARDING_STATUS"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_accounts_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-BILLING-CORE-ECOSYSTEM",
        "name": "STRIPE BILLING CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["INVOICE_LIFECYCLE", "BILLING_CONFIGURATION"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_billing_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-CHECKOUT-CORE-ECOSYSTEM",
        "name": "STRIPE CHECKOUT CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CHECKOUT_SESSION_ORCHESTRATION", "RETURN_URL_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_checkout_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-CUSTOMERS-CORE-ECOSYSTEM",
        "name": "STRIPE CUSTOMERS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CUSTOMER_REFERENCE", "CUSTOMER_LIFECYCLE"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_customers_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-DISPUTES-CORE-ECOSYSTEM",
        "name": "STRIPE DISPUTES CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["DISPUTE_STATUS", "EVIDENCE_WORKFLOW_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_disputes_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-EVENTS-CORE-ECOSYSTEM",
        "name": "STRIPE EVENTS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["EVENT_DISCOVERY", "EVENT_DEDUPLICATION"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_events_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-FRAUD-CORE-ECOSYSTEM",
        "name": "STRIPE FRAUD CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["RISK_METADATA", "REVIEW_WORKFLOW_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_fraud_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-ISSUING-CORE-ECOSYSTEM",
        "name": "STRIPE ISSUING CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["ISSUING_ELIGIBILITY_METADATA", "CARDHOLDER_LIFECYCLE_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_issuing_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-PAYMENT-INTENTS-CORE-ECOSYSTEM",
        "name": "STRIPE PAYMENT INTENTS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PAYMENT_INTENT_STATE", "PAYMENT_CONFIRMATION_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_payment_intents_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-PAYMENT-LINKS-CORE-ECOSYSTEM",
        "name": "STRIPE PAYMENT LINKS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PAYMENT_LINK_METADATA", "LINK_STATUS"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_payment_links_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-PAYMENT-METHODS-CORE-ECOSYSTEM",
        "name": "STRIPE PAYMENT METHODS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PAYMENT_METHOD_REFERENCE", "SETUP_INTENT_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_payment_methods_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-PAYOUTS-CORE-ECOSYSTEM",
        "name": "STRIPE PAYOUTS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PAYOUT_STATUS", "BALANCE_RECONCILIATION_REFERENCE"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_payouts_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-PRODUCTS-PRICES-CORE-ECOSYSTEM",
        "name": "STRIPE PRODUCTS AND PRICES CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PRODUCT_CATALOG_METADATA", "PRICE_REFERENCE"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_products_prices_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-REFUNDS-CORE-ECOSYSTEM",
        "name": "STRIPE REFUNDS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["REFUND_ELIGIBILITY_METADATA", "REFUND_LIFECYCLE"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_refunds_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-REPORTING-CORE-ECOSYSTEM",
        "name": "STRIPE REPORTING CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["REPORTING_CONFIGURATION", "RECONCILIATION_METADATA"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_reporting_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-SUBSCRIPTIONS-CORE-ECOSYSTEM",
        "name": "STRIPE SUBSCRIPTIONS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["SUBSCRIPTION_LIFECYCLE", "RENEWAL_STATUS"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_subscriptions_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-TAX-CORE-ECOSYSTEM",
        "name": "STRIPE TAX CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["TAX_CALCULATION_BOUNDARY", "TAX_CONFIGURATION_METADATA"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_tax_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-TERMINAL-CORE-ECOSYSTEM",
        "name": "STRIPE TERMINAL CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["READER_LOCATION_METADATA", "IN_PERSON_PAYMENT_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_terminal_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-TREASURY-CORE-ECOSYSTEM",
        "name": "STRIPE TREASURY CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["FINANCIAL_ACCOUNT_METADATA", "TREASURY_ELIGIBILITY_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_treasury_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-WEBHOOKS-CORE-ECOSYSTEM",
        "name": "STRIPE WEBHOOKS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["WEBHOOK_EVENT_ROUTING", "SIGNATURE_STATUS_METADATA"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_webhooks_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-CLIMATE-CORE-ECOSYSTEM",
        "name": "STRIPE CLIMATE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CLIMATE_ORDER_METADATA"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_climate_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },
    {
        "ecosystem_id": "STRIPE-CRYPTO-ONRAMP-CORE-ECOSYSTEM",
        "name": "STRIPE CRYPTO ONRAMP CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["ONRAMP_ELIGIBILITY_METADATA", "TRANSACTION_STATUS_BOUNDARY"],
        "parent_id": "STRIPE-CORE-ECOSYSTEM",
        "metadata": {"core_module": "stripe_crypto_onramp_core_ecosystem", "status": "CORE_CATALOG_ONLY"},
    },

    {
        "ecosystem_id": "GOOGLE-CORE-ECOSYSTEM",
        "name": "GOOGLE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE",
        "capabilities": ["GOOGLE_PROVIDER_REGISTRY", "GOOGLE_WORKSPACE_CORE", "GOOGLE_CLOUD_CORE", "GOOGLE_IDENTITY_OAUTH_CORE"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {
            "core_catalog": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem",
            "google_api_catalog": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem",
            "existing_google_core": "backend/global_ecosystem/google_ecosystem/runtime/core",
        },
    },
    {
        "ecosystem_id": "GOOGLE-GMAIL-CORE-ECOSYSTEM",
        "name": "GOOGLE GMAIL CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["MAILBOX_OAUTH", "MAILBOX_STATUS", "MAIL_SEND", "TOKEN_REFRESH_BOUNDARY"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/gmail_core.py",
            "api_service": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_gmail_api_ecosystem/service.py",
            "default_scope": "https://www.googleapis.com/auth/gmail.send",
            "status": "ADAPTER_SCAFFOLD_NOT_LIVE_VERIFIED",
        },
    },
    {
        "ecosystem_id": "GOOGLE-IDENTITY-OAUTH-CORE-ECOSYSTEM",
        "name": "GOOGLE IDENTITY AND OAUTH CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["OAUTH_CLIENT_METADATA", "CONSENT_AND_SCOPE_POLICY", "TOKEN_LIFECYCLE_BOUNDARY"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_identity_oauth_core_ecosystem",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-DRIVE-CORE-ECOSYSTEM",
        "name": "GOOGLE DRIVE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["FILE_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_drive",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-CALENDAR-CORE-ECOSYSTEM",
        "name": "GOOGLE CALENDAR CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CALENDAR_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_calendar",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-PEOPLE-CORE-ECOSYSTEM",
        "name": "GOOGLE PEOPLE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PEOPLE_PROFILE_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_people",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-GEMINI-CORE-ECOSYSTEM",
        "name": "GOOGLE GEMINI CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["GENERATIVE_AI_REQUEST_BOUNDARY"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_gemini",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-VERTEX-AI-CORE-ECOSYSTEM",
        "name": "GOOGLE VERTEX AI CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CLOUD_AI_MODEL_DISCOVERY"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_vertex_ai",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-ADMIN-SDK-CORE-ECOSYSTEM",
        "name": "GOOGLE ADMIN SDK CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["WORKSPACE_DIRECTORY_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_admin_sdk",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-ADS-CORE-ECOSYSTEM",
        "name": "GOOGLE ADS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CAMPAIGN_MANAGEMENT_BOUNDARY"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_ads",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-ANALYTICS-CORE-ECOSYSTEM",
        "name": "GOOGLE ANALYTICS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PROPERTY_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_analytics",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-BUSINESS-PROFILE-CORE-ECOSYSTEM",
        "name": "GOOGLE BUSINESS PROFILE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["BUSINESS_LOCATION_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_business_profile",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-CHAT-CORE-ECOSYSTEM",
        "name": "GOOGLE CHAT CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CHAT_SPACE_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_chat",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-CLOUD-CORE-ECOSYSTEM",
        "name": "GOOGLE CLOUD CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CLOUD_PROJECT_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_cloud",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-CONTACTS-CORE-ECOSYSTEM",
        "name": "GOOGLE CONTACTS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CONTACTS_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_contacts",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-DOCS-CORE-ECOSYSTEM",
        "name": "GOOGLE DOCS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["DOCUMENT_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_docs",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-FIREBASE-CORE-ECOSYSTEM",
        "name": "GOOGLE FIREBASE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["FIREBASE_PROJECT_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_firebase",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-FORMS-CORE-ECOSYSTEM",
        "name": "GOOGLE FORMS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["FORM_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_forms",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-MAPS-CORE-ECOSYSTEM",
        "name": "GOOGLE MAPS PLATFORM CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["MAPS_PLATFORM_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_maps",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-MEET-CORE-ECOSYSTEM",
        "name": "GOOGLE MEET CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["MEETING_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_meet",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-SEARCH-CONSOLE-CORE-ECOSYSTEM",
        "name": "GOOGLE SEARCH CONSOLE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["SEARCH_PERFORMANCE_BOUNDARY"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_search_console",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-SHEETS-CORE-ECOSYSTEM",
        "name": "GOOGLE SHEETS CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["SPREADSHEET_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_sheets",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-SLIDES-CORE-ECOSYSTEM",
        "name": "GOOGLE SLIDES CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PRESENTATION_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_slides",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GOOGLE-YOUTUBE-CORE-ECOSYSTEM",
        "name": "GOOGLE YOUTUBE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CHANNEL_METADATA"],
        "parent_id": "GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/google_core_ecosystem/google_youtube",
            "status": "CORE_CATALOG_ONLY",
        },
    },

    # API hierarchy
    {
        "ecosystem_id": "GLOBAL-API-ECOSYSTEM",
        "name": "GLOBAL API ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": ["API_CATALOG", "API_ROUTING", "INTEGRATION"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
        "name": "GLOBAL BUSINESS API ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": ["BUSINESS_APIS", "BUSINESS_INTEGRATIONS"],
        "parent_id": "GLOBAL-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-NETWORK-MARKETING-API-ECOSYSTEM",
        "name": "GLOBAL NETWORK MARKETING API ECOSYSTEM",
        "ecosystem_type": "BUSINESS_API",
        "capabilities": [
            "DIRECT_SELLING",
            "NETWORK_MARKETING",
            "PARTNER_NETWORKS",
        ],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-AFFILIATE-MARKETING-API-ECOSYSTEM",
        "name": "GLOBAL AFFILIATE MARKETING API ECOSYSTEM",
        "ecosystem_type": "BUSINESS_API",
        "capabilities": ["AFFILIATE_TRACKING", "REFERRALS", "COMMISSIONS"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
        "metadata": {"partner_program_registry": "backend/core/global_ecosystem/global_core_ecosystem/partner_programs.py"},
    },
    {
        "ecosystem_id": "GLOBAL-ECOMMERCE-API-ECOSYSTEM",
        "name": "GLOBAL E-COMMERCE API ECOSYSTEM",
        "ecosystem_type": "BUSINESS_API",
        "capabilities": ["PRODUCT_CATALOG", "ORDERS", "INVENTORY"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-CRM-LEAD-GENERATION-API-ECOSYSTEM",
        "name": "GLOBAL CRM & LEAD GENERATION API ECOSYSTEM",
        "ecosystem_type": "BUSINESS_API",
        "capabilities": ["CRM", "LEAD_CAPTURE", "LEAD_MANAGEMENT"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },

    # Language hierarchy
    {
        "ecosystem_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
        "name": "GLOBAL LANGUAGE ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": [
            "LANGUAGE_PREFERENCES",
            "LOCALIZATION",
            "MULTILINGUAL_SUPPORT",
        ],
    },
    {
        "ecosystem_id": "GLOBAL-LANGUAGE-TRANSLATION-ECOSYSTEM",
        "name": "GLOBAL LANGUAGE TRANSLATION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "TEXT_TRANSLATION",
            "MESSAGE_TRANSLATION",
            "CONTENT_TRANSLATION",
        ],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SPEECH-ECOSYSTEM",
        "name": "GLOBAL SPEECH ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SPEECH_PROCESSING", "AUDIO_LANGUAGE_SUPPORT"],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SPEECH-TO-TEXT-ECOSYSTEM",
        "name": "GLOBAL SPEECH TO TEXT ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["TRANSCRIPTION", "SPEECH_RECOGNITION"],
        "parent_id": "GLOBAL-SPEECH-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-TEXT-TO-SPEECH-ECOSYSTEM",
        "name": "GLOBAL TEXT TO SPEECH ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SPEECH_SYNTHESIS", "VOICE_OUTPUT"],
        "parent_id": "GLOBAL-SPEECH-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SUBTITLE-ECOSYSTEM",
        "name": "GLOBAL SUBTITLE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["CAPTIONS", "SUBTITLE_TRANSLATION", "TIMED_TEXT"],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },

    # Video hierarchy
    {
        "ecosystem_id": "GLOBAL-VIDEO-ECOSYSTEM",
        "name": "GLOBAL VIDEO ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": [
            "VIDEO_CATALOG",
            "VIDEO_PROCESSING",
            "VIDEO_PUBLISHING",
        ],
    },
    {
        "ecosystem_id": "GLOBAL-VIDEO-LANGUAGE-ECOSYSTEM",
        "name": "GLOBAL VIDEO LANGUAGE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "VIDEO_TRANSCRIPTION",
            "DUBBING",
            "MULTILINGUAL_AUDIO",
        ],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-MEDIA-INGESTION-ECOSYSTEM",
        "name": "GLOBAL MEDIA INGESTION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "AUTHORIZED_UPLOADS",
            "MEDIA_IMPORT",
            "FORMAT_VALIDATION",
        ],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-VIDEO-ACCESSIBILITY-ECOSYSTEM",
        "name": "GLOBAL VIDEO ACCESSIBILITY ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "CAPTIONS",
            "AUDIO_DESCRIPTION",
            "ACCESSIBILITY_PREFERENCES",
        ],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },

    {
        "ecosystem_id": "GLOBAL-FREELANCER-ECOSYSTEM",
        "name": "GLOBAL FREELANCER ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": [
            "FREELANCER_PROFILES",
            "SERVICE_OFFERS",
            "PORTFOLIO_METADATA",
            "PROJECT_BRIEFS",
            "APPLICATION_TRACKING",
            "CENTRAL_DATABASE_METADATA",
            "CENTRAL_STORAGE_ASSET_REFERENCES",
        ],
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
        "metadata": {
            "api_module": "backend/api/global_freelancer_ecosystem.py",
            "engine_module": "backend/engine/freelancer_ecosystem/manager.py",
            "database_module": "backend/database/freelancer_ecosystem.py",
            "storage_boundary": "MAIN BASE FOUNDATION StorageEngine",
        },
    },
    {
        "ecosystem_id": "GLOBAL-VASUDHAIVA-KUTUMBAKAM-CULTURE-CORE-ECOSYSTEM",
        "name": "GLOBAL VASUDHAIVA KUTUMBAKAM SANATAN DHARMA BHARAT WORLD CULTURE CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["CULTURAL_DOMAIN_RULES", "KNOWLEDGE_GOVERNANCE", "EVIDENCE_REVIEW", "CULTURAL_TAXONOMY"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"module_path": "global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem", "implementation_state": "FOUNDATION_READY"},
    },
    {
        "ecosystem_id": "GLOBAL-VASUDHAIVA-CULTURE-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM",
        "name": "GLOBAL VASUDHAIVA KUTUMBAKAM CULTURE SERVICE WORK BUSINESS CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["CULTURAL_SERVICE_TAXONOMY", "CULTURAL_WORK_CLASSIFICATION", "BUSINESS_CAPABILITY_GOVERNANCE", "RECORD_VALIDATION"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"module_path": "global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem", "implementation_state": "IMPLEMENTED_FOUNDATION"},
    }
)


# Google CORE ecosystem registry (metadata only; no credentials are stored).
GOOGLE_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "GLOBAL-GOOGLE-CORE-ECOSYSTEM",
        "name": "GLOBAL GOOGLE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE",
        "capabilities": [
            "GOOGLE_PROVIDER_REGISTRY",
            "GOOGLE_PRODUCT_DISCOVERY",
            "GOOGLE_API_ECOSYSTEM_MAPPING",
            "OAUTH_CONFIGURATION_READINESS",
            "GOOGLE_CLOUD_IDENTITY_READINESS",
            "GEMINI_API_ADAPTER_BOUNDARY",
        ],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {
            "provider_id": "google",
            "api_catalog_module": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_api_ecosystem.py",
            "product_catalog_module": "backend/global_ecosystem/google_ecosystem/runtime/service.py",
            "provider_adapter_module": "backend/integrations/providers/google.py",
            "gemini_adapter_module": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_gemini_api_ecosystem/google_gemini_api_ecosystem.py",
            "cloud_readiness_module": "backend/global_ecosystem/google_ecosystem/runtime/cloud/connection.py",
            "live_connection_verified": False,
            "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
            "catalog_source_of_truth": "backend/global_ecosystem/google_ecosystem/runtime/service.py",
        },
    },
    {
        "ecosystem_id": "GLOBAL-GOOGLE-API-CORE-ECOSYSTEM",
        "name": "GLOBAL GOOGLE API CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["API_CATALOG_REFERENCE", "API_FAMILY_DISCOVERY", "PROVIDER_STATUS_METADATA"],
        "parent_id": "GLOBAL-GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "source_module": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_api_ecosystem.py",
            "api_family_count": 23,
            "api_family_ids": ["gmail","drive","calendar","contacts","sheets","docs","slides","forms","chat","meet","admin_sdk","people","youtube","maps","business_profile","ads","analytics","search_console","cloud","firebase","identity_oauth","vertex_ai","gemini"],
            "live_connection_verified": False,
        },
    },
    {
        "ecosystem_id": "GLOBAL-GOOGLE-PRODUCT-CORE-ECOSYSTEM",
        "name": "GLOBAL GOOGLE PRODUCT CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["PRODUCT_CATALOG", "PRODUCT_CAPABILITY_METADATA", "AVAILABILITY_METADATA"],
        "parent_id": "GLOBAL-GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "source_module": "backend/global_ecosystem/google_ecosystem/runtime/service.py",
            "product_count": 129,
            "product_ids": ["gmail","google_chat","meet","calendar","contacts","google_voice","google_groups","drive","docs","sheets","google_slides","google_forms","google_sites","google_keep","tasks","google_jamboard","google_workspace_admin","google_one","cloud","firebase","maps","google_places","google_routes","google_geocoding","google_earth","google_search","google_search_console","analytics","google_tag_manager","google_ads","google_ad_manager","google_play_console","google_play_services","google_gemini","vertex_ai","google_ai_studio","google_colab","bigquery","look_studio","looker","google_cloud_storage","google_cloud_dns","google_compute_engine","google_kubernetes_engine","cloud_run","cloud_functions","cloud_sql","pub_sub","google_workspace_marketplace","youtube","youtube_analytics","photos","google_play_books","google_news","google_shopping","google_business_profile","google_translate","google_speech","google_text_to_speech","google_vision","google_document_ai","google_recaptcha","google_safe_browsing","google_identity","google_authenticator","google_wallet","google_pay","google_flights","google_travel","google_classroom","google_assignments","google_appsheet","google_apps_script","google_blogger","google_books","google_fonts","google_developers","google_play_console_reporting","google_android_management","google_play_integrity","google_cloud_identity","google_vault","google_endpoint_management","google_workspace_migrate","firebase_authentication","cloud_firestore","firebase_realtime_database","firebase_hosting","firebase_app_distribution","firebase_crashlytics","firebase_remote_config","firebase_performance","firebase_cloud_messaging","firebase_app_check","google_cloud_iam","google_secret_manager","google_cloud_kms","google_cloud_logging","google_cloud_monitoring","google_cloud_build","google_artifact_registry","google_cloud_armor","google_cloud_cdn","google_cloud_load_balancing","google_cloud_vpc","google_dataflow","google_dataproc","google_cloud_composer","google_app_engine","google_vertex_ai_search","google_dialogflow","google_natural_language","google_video_intelligence","google_recommendations_ai","google_adsense","google_admob","google_merchant_center","google_street_view","google_maps_elevation","google_maps_time_zone","google_maps_directions_legacy","google_art_and_culture","google_podcasts","google_duo","google_play_games","google_family_link","google_store","google_pixel","google_nest"],
            "live_connection_verified": False,
        },
    },
    {
        "ecosystem_id": "GLOBAL-GOOGLE-GEMINI-CORE-ECOSYSTEM",
        "name": "GLOBAL GOOGLE GEMINI CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["GEMINI_MODEL_DISCOVERY", "CONTENT_GENERATION_ADAPTER", "USER_SUPPLIED_API_KEY_SUPPORT"],
        "parent_id": "GLOBAL-GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "source_module": "backend/api/global_ecosystem/global_api_ecosystem/google_api_ecosystem/google_gemini_api_ecosystem/google_gemini_api_ecosystem.py",
            "api_key_env": "GOOGLE_GEMINI_API_KEY",
            "model_env": "GOOGLE_GEMINI_MODEL",
            "credential_persisted": False,
            "status": "ADAPTER_SCAFFOLD",
        },
    },
    {
        "ecosystem_id": "GLOBAL-GOOGLE-CLOUD-CORE-ECOSYSTEM",
        "name": "GLOBAL GOOGLE CLOUD CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["CLOUD_PROJECT_DISCOVERY", "READ_ONLY_CLOUD_PROJECT_HEALTH"],
        "parent_id": "GLOBAL-GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "source_module": "backend/global_ecosystem/google_ecosystem/runtime/cloud/connection.py",
            "project_env": "GOOGLE_CLOUD_PROJECT",
            "authentication": "APPLICATION_DEFAULT_CREDENTIALS",
            "read_only": True,
            "live_connection_verified": False,
        },
    },
    {
        "ecosystem_id": "GLOBAL-GOOGLE-OAUTH-CORE-ECOSYSTEM",
        "name": "GLOBAL GOOGLE OAUTH CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": ["OAUTH_APP_CONFIGURATION_READINESS", "REDIRECT_URI_CONFIGURATION_READINESS"],
        "parent_id": "GLOBAL-GOOGLE-CORE-ECOSYSTEM",
        "metadata": {
            "required_env": ["GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REDIRECT_URI"],
            "token_storage_status": "NOT_IMPLEMENTED",
            "oauth_flow_status": "PENDING_IMPLEMENTATION",
        },
    },
)


# Anthropic CORE ecosystem registry (metadata only; no credentials are stored).
ANTHROPIC_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {"ecosystem_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE", "capabilities": ["ANTHROPIC_PROVIDER_REGISTRY", "ANTHROPIC_PRODUCT_DISCOVERY", "ANTHROPIC_API_ECOSYSTEM_MAPPING", "TENANT_CONTEXT_POLICY", "CAPABILITY_LIFECYCLE"], "parent_id": "GLOBAL-CORE-ECOSYSTEM", "metadata": {"provider_id": "anthropic", "core_catalog": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem", "api_catalog": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem", "provider_adapter_module": "backend/integrations/providers/anthropic.py", "live_connection_verified": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY", "status": "CORE_CATALOG_ONLY"}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-API-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC API CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["API_CATALOG_REFERENCE", "API_FAMILY_DISCOVERY", "PROVIDER_STATUS_METADATA"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"source_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_api_ecosystem.py", "api_family_count": 9, "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-PRODUCT-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC PRODUCT CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["PRODUCT_CATALOG", "PRODUCT_CAPABILITY_METADATA", "AVAILABILITY_METADATA"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"source_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/catalog.py", "product_count": 9, "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-MESSAGES-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC MESSAGES CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_MESSAGES_CREATE", "ANTHROPIC_MESSAGES_STREAM", "ANTHROPIC_MESSAGES_TOOL_USE"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_messages_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_messages_api_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-BATCHES-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC MESSAGE BATCHES CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_BATCH_CREATE", "ANTHROPIC_BATCH_STATUS", "ANTHROPIC_BATCH_RESULTS"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_batches_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_batches_api_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-MODELS-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC MODELS CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_MODELS_LIST", "ANTHROPIC_MODEL_METADATA"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_models_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_models_api_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-TOKEN-COUNTING-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC TOKEN COUNTING CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_TOKEN_COUNT_ESTIMATE"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_token_counting_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_token_counting_api_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-FILES-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC FILES CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_FILES_LIST", "ANTHROPIC_FILES_UPLOAD", "ANTHROPIC_FILES_RETRIEVE", "ANTHROPIC_FILES_DELETE"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_files_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_files_api_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-ADMIN-WORKSPACES-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC ADMIN WORKSPACES CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_WORKSPACE_LIST", "ANTHROPIC_WORKSPACE_ADMIN"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_admin_workspaces_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_admin_workspaces_api_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-MANAGED-AGENTS-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC MANAGED AGENTS CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_MANAGED_AGENT_SESSIONS", "ANTHROPIC_MANAGED_AGENT_ENVIRONMENTS"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_managed_agents_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_managed_agents_api_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-TOOL-USE-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC TOOL USE CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_TOOL_DEFINITION", "ANTHROPIC_TOOL_CHOICE", "ANTHROPIC_TOOL_HANDOFF"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_tool_use_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_tool_use_api_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}},
    {"ecosystem_id": "GLOBAL-ANTHROPIC-AUTH-IDENTITY-CORE-ECOSYSTEM", "name": "GLOBAL ANTHROPIC AUTHENTICATION AND IDENTITY CORE ECOSYSTEM", "ecosystem_type": "PROVIDER_CORE_SERVICE", "capabilities": ["ANTHROPIC_CREDENTIAL_READINESS", "ANTHROPIC_WORKLOAD_IDENTITY_BOUNDARY", "ANTHROPIC_CREDENTIAL_ROTATION_BOUNDARY"], "parent_id": "GLOBAL-ANTHROPIC-CORE-ECOSYSTEM", "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/anthropic_core_ecosystem/anthropic_auth_identity_core_ecosystem", "api_module": "backend/api/global_ecosystem/global_api_ecosystem/anthropic_api_ecosystem/anthropic_auth_identity_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False}}
)




# Apple CORE ecosystem registry (catalog metadata only; no credentials are stored).
APPLE_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
 {"ecosystem_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","name":"GLOBAL APPLE CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE","capabilities":["APPLE_PROVIDER_REGISTRY","APPLE_PRODUCT_DISCOVERY","APPLE_API_ECOSYSTEM_MAPPING","APPLE_CAPABILITY_LIFECYCLE"],"parent_id":"GLOBAL-CORE-ECOSYSTEM","metadata":{"provider_id":"apple","core_catalog":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem","api_catalog":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem","live_connection_verified":False,"credential_storage":"EXTERNAL_SECRET_STORE_ONLY","status":"CORE_CATALOG_ONLY"}},
 {"ecosystem_id":"GLOBAL-APPLE-API-CORE-ECOSYSTEM","name":"GLOBAL APPLE API CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["API_CATALOG_REFERENCE","API_FAMILY_DISCOVERY","PROVIDER_STATUS_METADATA"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"source_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_api_ecosystem.py","api_family_count":8,"live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-PRODUCT-CORE-ECOSYSTEM","name":"GLOBAL APPLE PRODUCT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["PRODUCT_CATALOG","PRODUCT_CAPABILITY_METADATA","AVAILABILITY_METADATA"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"source_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/catalog.py","product_count":8,"live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-APP-STORE-CONNECT-CORE-ECOSYSTEM","name":"GLOBAL APPLE APP STORE CONNECT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["APP_METADATA","APP_VERSION_LIFECYCLE","APP_REVIEW_BOUNDARY"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/apple_app_store_connect_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_app_store_connect_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-APP-STORE-SERVER-CORE-ECOSYSTEM","name":"GLOBAL APPLE APP STORE SERVER CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["TRANSACTION_LOOKUP_BOUNDARY","SERVER_NOTIFICATION_METADATA","SUBSCRIPTION_STATUS"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/apple_app_store_server_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_app_store_server_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-DEVICE-MANAGEMENT-CORE-ECOSYSTEM","name":"GLOBAL APPLE DEVICE MANAGEMENT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["DEVICE_ENROLLMENT_METADATA","DEVICE_CONFIGURATION_POLICY","DEVICE_COMMAND_LIFECYCLE"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/apple_device_management_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_device_management_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-ICLOUD-CLOUDKIT-CORE-ECOSYSTEM","name":"GLOBAL APPLE ICLOUD CLOUDKIT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["CLOUDKIT_CONTAINER_METADATA","RECORD_SCHEMA_METADATA","CLOUDKIT_SUBSCRIPTION_BOUNDARY"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/apple_icloud_cloudkit_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_icloud_cloudkit_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-APPLE-PAY-CORE-ECOSYSTEM","name":"GLOBAL APPLE PAY CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["MERCHANT_CONFIGURATION_METADATA","PAYMENT_TOKEN_HANDOFF","PAYMENT_AUTHORIZATION_POLICY"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/apple_pay_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_pay_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-PUSH-NOTIFICATION-CORE-ECOSYSTEM","name":"GLOBAL APPLE PUSH NOTIFICATION SERVICE CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["APNS_PROVIDER_CONFIGURATION","DEVICE_TOKEN_REFERENCE","PUSH_DELIVERY_BOUNDARY"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/apple_push_notification_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_push_notification_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-SIGN-IN-WITH-APPLE-CORE-ECOSYSTEM","name":"GLOBAL APPLE SIGN IN WITH APPLE CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["APPLE_IDENTITY_CLIENT_METADATA","AUTHORIZATION_POLICY","IDENTITY_TOKEN_VALIDATION_BOUNDARY"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/apple_sign_in_with_apple_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_sign_in_with_apple_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
 {"ecosystem_id":"GLOBAL-APPLE-STOREKIT-CORE-ECOSYSTEM","name":"GLOBAL APPLE STOREKIT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["IN_APP_PRODUCT_METADATA","PURCHASE_LIFECYCLE_BOUNDARY","SUBSCRIPTION_ENTITLEMENT_METADATA"],"parent_id":"GLOBAL-APPLE-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/apple_core_ecosystem/apple_storekit_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/apple_api_ecosystem/apple_storekit_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
)


# Atlassian CORE ecosystem registry (catalog metadata only; no credentials are stored).
ATLASSIAN_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {"ecosystem_id":"GLOBAL-ATLASSIAN-CORE-ECOSYSTEM","name":"GLOBAL ATLASSIAN CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE","capabilities":["ATLASSIAN_PROVIDER_REGISTRY","ATLASSIAN_PRODUCT_DISCOVERY","ATLASSIAN_API_ECOSYSTEM_MAPPING","ATLASSIAN_CAPABILITY_LIFECYCLE"],"parent_id":"GLOBAL-CORE-ECOSYSTEM","metadata":{"provider_id":"atlassian","core_catalog":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem","api_catalog":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem","live_connection_verified":False,"credential_storage":"EXTERNAL_SECRET_STORE_ONLY","status":"CORE_CATALOG_ONLY"}},
    {"ecosystem_id":"GLOBAL-ATLASSIAN-API-CORE-ECOSYSTEM","name":"GLOBAL ATLASSIAN API CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["API_CATALOG_REFERENCE","API_FAMILY_DISCOVERY","PROVIDER_STATUS_METADATA"],"parent_id":"GLOBAL-ATLASSIAN-CORE-ECOSYSTEM","metadata":{"source_module":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_api_ecosystem.py","api_family_count":5,"live_connection_verified":False}},
    {"ecosystem_id":"GLOBAL-ATLASSIAN-PRODUCT-CORE-ECOSYSTEM","name":"GLOBAL ATLASSIAN PRODUCT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["PRODUCT_CATALOG","PRODUCT_CAPABILITY_METADATA","AVAILABILITY_METADATA"],"parent_id":"GLOBAL-ATLASSIAN-CORE-ECOSYSTEM","metadata":{"source_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/catalog.py","product_count":5,"live_connection_verified":False}},
    {"ecosystem_id":"GLOBAL-ATLASSIAN-ADMIN-IDENTITY-CORE-ECOSYSTEM","name":"GLOBAL ATLASSIAN ATLASSIAN ADMINISTRATION AND IDENTITY CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["ORGANIZATION_DIRECTORY_METADATA","USER_AND_GROUP_ADMINISTRATION_BOUNDARY","SCIM_PROVISIONING_METADATA","ACCESS_POLICY_METADATA"],"parent_id":"GLOBAL-ATLASSIAN-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_admin_identity_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_admin_identity_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
    {"ecosystem_id":"GLOBAL-ATLASSIAN-BITBUCKET-CORE-ECOSYSTEM","name":"GLOBAL ATLASSIAN BITBUCKET CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["REPOSITORY_METADATA","PULL_REQUEST_LIFECYCLE_BOUNDARY","PIPELINE_CONFIGURATION_METADATA","WORKSPACE_ACCESS_POLICY"],"parent_id":"GLOBAL-ATLASSIAN-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_bitbucket_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_bitbucket_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
    {"ecosystem_id":"GLOBAL-ATLASSIAN-CONFLUENCE-CORE-ECOSYSTEM","name":"GLOBAL ATLASSIAN CONFLUENCE CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["SPACE_METADATA","PAGE_LIFECYCLE_BOUNDARY","CONTENT_PERMISSION_METADATA","CONTENT_DISCOVERY_METADATA"],"parent_id":"GLOBAL-ATLASSIAN-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_confluence_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_confluence_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
    {"ecosystem_id":"GLOBAL-ATLASSIAN-JIRA-CORE-ECOSYSTEM","name":"GLOBAL ATLASSIAN JIRA CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["PROJECT_METADATA","ISSUE_LIFECYCLE_BOUNDARY","WORKFLOW_CONFIGURATION_METADATA","BOARD_AND_SPRINT_METADATA"],"parent_id":"GLOBAL-ATLASSIAN-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_jira_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_jira_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
    {"ecosystem_id":"GLOBAL-ATLASSIAN-JIRA-SERVICE-MANAGEMENT-CORE-ECOSYSTEM","name":"GLOBAL ATLASSIAN JIRA SERVICE MANAGEMENT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["SERVICE_PROJECT_METADATA","REQUEST_AND_INCIDENT_LIFECYCLE_BOUNDARY","SERVICE_LEVEL_METADATA","ASSET_AND_CHANGE_GOVERNANCE_BOUNDARY"],"parent_id":"GLOBAL-ATLASSIAN-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/atlassian_core_ecosystem/atlassian_jira_service_management_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/atlassian_api_ecosystem/atlassian_jira_service_management_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False}},
)


# AWS CORE ecosystem registry (catalog-only metadata; no credentials or live access are asserted).
AWS_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {"ecosystem_id":"GLOBAL-AWS-CORE-ECOSYSTEM","name":"GLOBAL AWS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE","capabilities":["AWS_PROVIDER_REGISTRY","AWS_SERVICE_FAMILY_DISCOVERY","AWS_ACCOUNT_REGION_CONTEXT","AWS_CAPABILITY_POLICY_METADATA"],"parent_id":"GLOBAL-CORE-ECOSYSTEM","metadata":{"provider_id":"aws","core_catalog":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem","api_catalog":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem","service_family_count":16,"live_connection_verified":False,"credential_storage":"IAM_ROLE_WEB_IDENTITY_OR_EXTERNAL_SECRET_REFERENCE_ONLY","status":"CORE_CATALOG_ONLY"}},
    {"ecosystem_id":"GLOBAL-AWS-API-CORE-ECOSYSTEM","name":"GLOBAL AWS API CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["AWS_API_CATALOG_REFERENCE","AWS_API_FAMILY_DISCOVERY","AWS_PROVIDER_ADAPTER_REFERENCE"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"source_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_api_ecosystem.py","api_family_count":16,"live_connection_verified":False}},
    {"ecosystem_id":"GLOBAL-AWS-PRODUCT-CORE-ECOSYSTEM","name":"GLOBAL AWS PRODUCT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["AWS_SERVICE_FAMILY_CATALOG","AWS_CAPABILITY_METADATA","AWS_DOMAIN_TAXONOMY"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"source_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/product_catalog.py","product_count":16,"live_connection_verified":False}},
    {"ecosystem_id":"GLOBAL-AWS-API-GATEWAY-CORE-ECOSYSTEM","name":"GLOBAL AWS API GATEWAY CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["REST_API_METADATA","HTTP_API_METADATA","WEBSOCKET_API_METADATA","STAGE_AND_DEPLOYMENT_METADATA","AUTHORIZER_CONFIGURATION_BOUNDARY"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_api_gateway_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_api_gateway_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-BEDROCK-SAGEMAKER-CORE-ECOSYSTEM","name":"GLOBAL AWS BEDROCK AND SAGEMAKER AI CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["FOUNDATION_MODEL_CATALOG_METADATA","MODEL_INVOCATION_POLICY_BOUNDARY","SAGEMAKER_RESOURCE_METADATA","MODEL_DEPLOYMENT_LIFECYCLE","AI_GOVERNANCE_METADATA"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_bedrock_sagemaker_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_bedrock_sagemaker_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-BILLING-COST-CORE-ECOSYSTEM","name":"GLOBAL AWS BILLING AND COST MANAGEMENT CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["BILLING_ACCOUNT_METADATA","COST_EXPLORER_QUERY_METADATA","BUDGET_POLICY_METADATA","COST_ALLOCATION_TAG_METADATA","USAGE_REPORTING_BOUNDARY"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_billing_cost_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_billing_cost_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-CLOUDFORMATION-CORE-ECOSYSTEM","name":"GLOBAL AWS CLOUDFORMATION CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["STACK_METADATA","TEMPLATE_METADATA","CHANGE_SET_REVIEW_BOUNDARY","PROVISIONING_LIFECYCLE","DRIFT_DETECTION_METADATA"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_cloudformation_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_cloudformation_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-CLOUDTRAIL-CORE-ECOSYSTEM","name":"GLOBAL AWS CLOUDTRAIL CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["AUDIT_TRAIL_METADATA","EVENT_HISTORY_QUERY_BOUNDARY","EVENT_SELECTOR_METADATA","GOVERNANCE_EVIDENCE_METADATA"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_cloudtrail_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_cloudtrail_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-CLOUDWATCH-CORE-ECOSYSTEM","name":"GLOBAL AWS CLOUDWATCH CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["METRIC_METADATA","ALARM_POLICY_METADATA","DASHBOARD_METADATA","LOG_GROUP_AND_STREAM_METADATA","OBSERVABILITY_QUERY_BOUNDARY"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_cloudwatch_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_cloudwatch_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-CONTAINERS-CORE-ECOSYSTEM","name":"GLOBAL AWS CONTAINERS (ECS, EKS AND ECR) CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["ECS_CLUSTER_AND_SERVICE_METADATA","EKS_CLUSTER_METADATA","ECR_REPOSITORY_METADATA","CONTAINER_DEPLOYMENT_LIFECYCLE","ORCHESTRATION_POLICY_METADATA"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_containers_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_containers_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-DATABASE-CORE-ECOSYSTEM","name":"GLOBAL AWS DATABASE (RDS, AURORA AND DYNAMODB) CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["RDS_INSTANCE_METADATA","AURORA_CLUSTER_METADATA","DYNAMODB_TABLE_METADATA","BACKUP_AND_RESTORE_POLICY_METADATA","DATABASE_LIFECYCLE_BOUNDARY"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_database_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_database_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-EC2-COMPUTE-CORE-ECOSYSTEM","name":"GLOBAL AWS EC2 COMPUTE CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["EC2_INSTANCE_METADATA","AMI_CATALOG_METADATA","EBS_VOLUME_AND_SNAPSHOT_METADATA","COMPUTE_LIFECYCLE_BOUNDARY","INSTANCE_ACCESS_POLICY_METADATA"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_ec2_compute_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_ec2_compute_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-IAM-STS-CORE-ECOSYSTEM","name":"GLOBAL AWS IAM AND STS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["IAM_IDENTITY_METADATA","ROLE_AND_POLICY_METADATA","TRUST_RELATIONSHIP_METADATA","TEMPORARY_CREDENTIALS_BOUNDARY","IDENTITY_GOVERNANCE_METADATA"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_iam_sts_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_iam_sts_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-KMS-SECRETS-CORE-ECOSYSTEM","name":"GLOBAL AWS KMS AND SECRETS MANAGER CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["KMS_KEY_METADATA","CRYPTOGRAPHIC_OPERATION_POLICY_BOUNDARY","SECRETS_METADATA","SECRET_ROTATION_POLICY_METADATA","SECURE_PARAMETER_REFERENCE"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_kms_secrets_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_kms_secrets_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-LAMBDA-CORE-ECOSYSTEM","name":"GLOBAL AWS LAMBDA CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["FUNCTION_METADATA","VERSION_AND_ALIAS_METADATA","INVOCATION_POLICY_BOUNDARY","EVENT_SOURCE_MAPPING_METADATA","FUNCTION_LIFECYCLE_BOUNDARY"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_lambda_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_lambda_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-LIGHTSAIL-CORE-ECOSYSTEM","name":"GLOBAL AWS LIGHTSAIL CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["INSTANCE_METADATA","CONTAINER_SERVICE_METADATA","MANAGED_DATABASE_METADATA","LIGHTSAIL_NETWORKING_METADATA","SNAPSHOT_LIFECYCLE_BOUNDARY"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_lightsail_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_lightsail_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-ROUTE53-DNS-CORE-ECOSYSTEM","name":"GLOBAL AWS ROUTE 53 DNS CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["HOSTED_ZONE_METADATA","DNS_RECORD_METADATA","HEALTH_CHECK_METADATA","DNS_ROUTING_POLICY_METADATA","DOMAIN_REGISTRATION_BOUNDARY"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_route53_dns_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_route53_dns_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-S3-STORAGE-CORE-ECOSYSTEM","name":"GLOBAL AWS S3 STORAGE CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["BUCKET_METADATA","OBJECT_METADATA","LIFECYCLE_CONFIGURATION_METADATA","ENCRYPTION_POLICY_METADATA","BUCKET_ACCESS_POLICY_METADATA"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_s3_storage_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_s3_storage_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
    {"ecosystem_id":"GLOBAL-AWS-VPC-NETWORKING-CORE-ECOSYSTEM","name":"GLOBAL AWS VPC NETWORKING CORE ECOSYSTEM","ecosystem_type":"PROVIDER_CORE_SERVICE","capabilities":["VPC_METADATA","SUBNET_AND_ROUTE_TABLE_METADATA","GATEWAY_METADATA","SECURITY_GROUP_POLICY_METADATA","NETWORK_INTERFACE_METADATA"],"parent_id":"GLOBAL-AWS-CORE-ECOSYSTEM","metadata":{"core_module":"backend/core/global_ecosystem/global_core_ecosystem/aws_core_ecosystem/aws_vpc_networking_core_ecosystem","api_module":"backend/api/global_ecosystem/global_api_ecosystem/aws_api_ecosystem/aws_vpc_networking_api_ecosystem","status":"CORE_CATALOG_ONLY","live_connection_verified":False,"api_available":None}},
)


# Existing personal registrations
PERSONAL_REGISTRATIONS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "PERSONAL-RAJESHKHANDELWAL",
        "name": "RAJESHKHANDELWAL",
        "ecosystem_type": "PERSONAL",
        "repository_ref": "RAJESHKHANDELWALOFFICIAL/RAJESHKHANDELWAL",
        "capabilities": [
            "IDENTITY",
            "PROFILE",
            "WEBSITE",
            "DOMAIN",
            "PROJECTS",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-RAJESHKHANDELWALOFFICIAL",
        "name": "RAJESHKHANDELWALOFFICIAL",
        "ecosystem_type": "PERSONAL",
        "repository_ref": "RAJESHKHANDELWALOFFICIAL/MAIN-BASE-FOUNDATION",
        "capabilities": [
            "IDENTITY",
            "PROFILE",
            "BUSINESS",
            "WEBSITE",
            "DOMAIN",
            "PROJECTS",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-DRRAJESHKANDELWALIBC",
        "name": "DRRAJESHKANDELWALIBC",
        "ecosystem_type": "PERSONAL_BRAND",
        "capabilities": [
            "IDENTITY",
            "BRAND",
            "BUSINESS",
            "WEBSITE",
            "DOMAIN",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-DRRAJESHKANDELWALIBCOFFICIAL",
        "name": "DRRAJESHKANDELWALIBCOFFICIAL",
        "ecosystem_type": "PERSONAL_BRAND",
        "capabilities": [
            "IDENTITY",
            "BRAND",
            "BUSINESS",
            "WEBSITE",
            "DOMAIN",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
)


# Existing company and company-group registrations
_COMPANY_CAPABILITIES = [
    "ORGANIZATION",
    "BUSINESS",
    "TEAM",
    "PROJECTS",
    "WEBSITE",
    "DOMAIN",
]

COMPANY_REGISTRATIONS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "COMPANY-KHANDELWALGROUPANDCOMPANY",
        "name": "KHANDELWALGROUPANDCOMPANY",
        "ecosystem_type": "COMPANY",
        "capabilities": _COMPANY_CAPABILITIES,
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
    },
    {
        "ecosystem_id": "COMPANY-KHANDELWALGROUPANDCOMPANYOFFICIAL",
        "name": "KHANDELWALGROUPANDCOMPANYOFFICIAL",
        "ecosystem_type": "COMPANY",
        "capabilities": _COMPANY_CAPABILITIES,
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
    },
    {
        "ecosystem_id": "COMPANY-KHANDELWALGROUPANDCOMPANIES",
        "name": "KHANDELWALGROUPANDCOMPANIES",
        "ecosystem_type": "COMPANY_GROUP",
        "capabilities": _COMPANY_CAPABILITIES,
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
    },
    {
        "ecosystem_id": "COMPANY-KHANDELWALGROUPANDCOMPANIESOFFICIAL",
        "name": "KHANDELWALGROUPANDCOMPANIESOFFICIAL",
        "ecosystem_type": "COMPANY_GROUP",
        "capabilities": _COMPANY_CAPABILITIES,
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
    },
)



# Cloudflare Core registry (metadata only; no credentials or live access asserted).
CLOUDFLARE_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM",
        "name": "GLOBAL CLOUDFLARE CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE",
        "capabilities": [
            "CLOUDFLARE_PRODUCT_DISCOVERY",
            "CLOUDFLARE_DOMAIN_TAXONOMY",
            "CLOUDFLARE_ACCOUNT_GOVERNANCE_METADATA",
            "CLOUDFLARE_SECURITY_POLICY_METADATA",
            "CLOUDFLARE_EDGE_AND_DEVELOPER_PLATFORM_METADATA",
        ],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {
            "provider_id": "cloudflare",
            "core_catalog": "backend/core/global_ecosystem/global_core_ecosystem/global_cloudflare_core_ecosystem",
            "product_catalog_module": "backend/core/global_ecosystem/global_core_ecosystem/global_cloudflare_core_ecosystem/product_catalog.py",
            "product_count": 67,
            "existing_directory_count": 89,
            "live_connection_verified": False,
            "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
            "status": "CORE_CATALOG_ONLY",
        },
    },
    {
        "ecosystem_id": "GLOBAL-CLOUDFLARE-PRODUCT-CORE-ECOSYSTEM",
        "name": "GLOBAL CLOUDFLARE PRODUCT CORE ECOSYSTEM",
        "ecosystem_type": "PROVIDER_CORE_SERVICE",
        "capabilities": [
            "CLOUDFLARE_PRODUCT_CATALOG",
            "PRODUCT_TO_DOMAIN_ROUTING",
            "DIRECTORY_CLASSIFICATION_AUDIT",
        ],
        "parent_id": "GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM",
        "metadata": {
            "source_module": "backend/core/global_ecosystem/global_core_ecosystem/global_cloudflare_core_ecosystem/product_catalog.py",
            "product_count": 67,
            "directory_count": 89,
            "live_connection_verified": False,
            "status": "CORE_CATALOG_ONLY",
        },
    },
)


# Developer Core registry (catalog-only metadata; no provider APIs or credentials asserted).
DEVELOPER_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-CORE-ECOSYSTEM",
        "name": "GLOBAL DEVELOPER CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": [
            "DEVELOPER_PLATFORM_REGISTRY",
            "DEVELOPER_PRODUCT_SERVICE_DISCOVERY",
            "SDK_AND_API_CAPABILITY_METADATA",
            "DEVELOPER_TOOLCHAIN_CLASSIFICATION",
            "SECURITY_AND_COMPLIANCE_POLICY_METADATA",
            "TENANT_SCOPED_CONNECTION_METADATA",
            "CREDENTIAL_BOUNDARY_AND_SECRET_REFERENCE",
            "DEPENDENCY_AND_LIFECYCLE_METADATA",
        ],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_developer_core_ecosystem",
            "status": "CORE_CATALOG_ONLY",
            "module_reference_count": 29,
            "domain_count": 19,
            "live_connection_verified": False,
            "api_transport_in_core": False,
            "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
        },
    },
)


# Domain Core registry (provider inventory only; no API transport or live DNS operations asserted).
DOMAIN_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "GLOBAL-DOMAIN-CORE-ECOSYSTEM",
        "name": "GLOBAL DOMAIN CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["DOMAIN_REGISTRY", "DNS_AND_REGISTRAR_CLASSIFICATION", "DOMAIN_LIFECYCLE_METADATA", "DNSSEC_AND_TLS_METADATA", "PROVIDER_DISCOVERY", "TENANT_SCOPED_DOMAIN_METADATA", "POLICY_AND_READINESS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_domain_core_ecosystem", "status": "CORE_CATALOG_ONLY", "provider_directory_count": 78, "domain_count": 18, "live_connection_verified": False, "api_transport_in_core": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"},
    },
)

# Communication Core registry (catalog-only metadata; no credentials or live access asserted).
COMMUNICATION_CORE_ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM",
        "name": "GLOBAL COMMUNICATION CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["COMMUNICATION_PROVIDER_DISCOVERY", "EMAIL_AND_MESSAGING_TAXONOMY", "VOICE_AND_VIDEO_METADATA", "NOTIFICATION_ROUTING_METADATA", "PRIVACY_AND_TRUST_SAFETY_POLICY"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_communication_core_ecosystem", "status": "CORE_CATALOG_ONLY", "provider_platform_reference_count": 95, "service_family_count": 40, "directory_entry_count": 19, "domain_count": 28, "live_connection_verified": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"},
    },
    {
        "ecosystem_id": "GLOBAL-COMMUNICATION-PROVIDERS-CORE-ECOSYSTEM",
        "name": "GLOBAL COMMUNICATION PROVIDERS CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["PROVIDER_DIRECTORY", "PROVIDER_CLASSIFICATION", "PROVIDER_LIFECYCLE_METADATA"],
        "parent_id": "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM",
        "metadata": {"source_module": "backend/core/global_ecosystem/global_core_ecosystem/global_communication_core_ecosystem/product_catalog.py", "provider_platform_reference_count": 95, "service_family_count": 40, "domain_count": 28, "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    },
    *[
        {
            "ecosystem_id": f"GLOBAL-{provider['id'].upper()}-COMMUNICATION-CORE-ECOSYSTEM",
            "name": f"GLOBAL {provider['name'].upper()} COMMUNICATION CORE ECOSYSTEM",
            "ecosystem_type": "PROVIDER_PLATFORM_REFERENCE",
            "capabilities": ["PROVIDER_IDENTITY_METADATA", "COMMUNICATION_PRODUCT_DISCOVERY", "CAPABILITY_CLASSIFICATION"],
            "parent_id": "GLOBAL-COMMUNICATION-PROVIDERS-CORE-ECOSYSTEM",
            "metadata": {
                "reference_id": provider["id"],
                "service_family": provider["family"],
                "geographic_scope": provider["region"],
                "products_reference": provider["products"],
                "status": "REFERENCE_ONLY",
                "live_connection_verified": False,
                "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
            },
        }
        for provider in PROVIDER_DIRECTORY
    ],
    {
        "ecosystem_id": "GLOBAL-COMMUNICATION-PRIVACY-CORE-ECOSYSTEM",
        "name": "GLOBAL COMMUNICATION PRIVACY CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["DATA_MINIMIZATION_POLICY", "RETENTION_POLICY_METADATA", "ACCESS_AND_AUDIT_BOUNDARIES"],
        "parent_id": "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM",
        "metadata": {"status": "CORE_CATALOG_ONLY", "live_enforcement_verified": False},
    },
    {
        "ecosystem_id": "GLOBAL-COMMUNICATION-TRUST-SAFETY-CORE-ECOSYSTEM",
        "name": "GLOBAL COMMUNICATION TRUST AND SAFETY CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["ABUSE_REPORTING_METADATA", "MODERATION_POLICY", "AGE_AND_CONSENT_BOUNDARIES"],
        "parent_id": "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM",
        "metadata": {"status": "CORE_CATALOG_ONLY", "live_enforcement_verified": False},
    },
)

def _normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    """Return a complete, independent record with safe defaults."""
    normalized = deepcopy(record)
    normalized.setdefault("repository_ref", None)
    normalized.setdefault("status", "REGISTERED")
    normalized.setdefault("enabled", True)
    normalized.setdefault("capabilities", [])
    normalized.setdefault("parent_id", ROOT_ID)
    normalized.setdefault("metadata", {})
    return normalized


def get_catalog() -> list[dict[str, Any]]:
    """Return the root, all categories, and all registrations."""
    infrastructure_core = {
        "ecosystem_id": "GLOBAL-INFRASTRUCTURE-CORE-ECOSYSTEM",
        "name": "GLOBAL INFRASTRUCTURE CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["RESOURCE_IDENTITY", "RESOURCE_CONTRACT_VALIDATION", "INFRASTRUCTURE_DOMAIN_DISCOVERY", "PROVIDER_NEUTRAL_METADATA", "LIFECYCLE_POLICY_METADATA", "SECURITY_AND_COMPLIANCE_BOUNDARIES", "HEALTH_AND_STATUS_METADATA"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_infrastructure_core_ecosystem", "status": "CORE_CATALOG_ONLY", "api_available": None, "live_connection_verified": False},
    }
    integrations_core = {
        "ecosystem_id": "GLOBAL-INTEGRATIONS-CORE-ECOSYSTEM",
        "name": "GLOBAL INTEGRATIONS CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["PROVIDER_REGISTRY", "INTEGRATION_DOMAIN_DISCOVERY", "CAPABILITY_CONTRACTS", "PROVIDER_POLICY_METADATA", "TENANT_AND_SCOPE_BOUNDARIES", "SECRET_REFERENCE_BOUNDARY", "INTEGRATION_LIFECYCLE_METADATA", "AUDIT_AND_COMPLIANCE_METADATA"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_integrations_core_ecosystem", "status": "CORE_CATALOG_ONLY", "integration_domain_count": 31, "api_available": None, "live_connection_verified": False, "credential_storage": "EXTERNAL_SECRET_STORE_ONLY"},
    }
    human_language_core = {
        "ecosystem_id": "GLOBAL-HUMAN-LANGUAGE-CORE-ECOSYSTEM",
        "name": "GLOBAL HUMAN LANGUAGE CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["HUMAN_LANGUAGE_TAXONOMY", "BHARAT_AND_GLOBAL_LANGUAGE_DISCOVERY", "LANGUAGE_STANDARDS_METADATA", "TRANSLATION_AND_LOCALIZATION_METADATA", "TRANSLITERATION_METADATA", "SPEECH_OCR_AND_DETECTION_METADATA", "LANGUAGE_LEARNING_METADATA", "ADULT_CONTENT_AGE_CONSENT_POLICY", "NORMAL_TO_SUPREME_SERVICE_TIERS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_human_language_core_ecosystem", "division_layout": "INDEPENDENT_SIBLING_ECOSYSTEM", "status": "CORE_CATALOG_ONLY", "division": "HUMAN-LANGUAGES", "human_language_coverage_exhaustive": False, "live_provider_connections_verified": False},
    }
    programming_language_core = {
        "ecosystem_id": "GLOBAL-PROGRAMMING-LANGUAGE-CORE-ECOSYSTEM",
        "name": "GLOBAL PROGRAMMING LANGUAGE CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["PROGRAMMING_LANGUAGE_TAXONOMY", "LANGUAGE_STANDARDS_METADATA", "COMPILER_AND_RUNTIME_METADATA", "DEVELOPER_TOOLING_METADATA", "PROGRAMMING_EDUCATION_METADATA", "PROGRAMMING_LANGUAGE_SECURITY_AND_QUALITY_METADATA", "NORMAL_TO_SUPREME_SERVICE_TIERS"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_programming_language_core_ecosystem", "division_layout": "INDEPENDENT_SIBLING_ECOSYSTEM", "status": "CORE_CATALOG_ONLY", "division": "PROGRAMMING-LANGUAGES", "programming_language_coverage_exhaustive": False, "live_provider_connections_verified": False},
    }
    server_core = {
        "ecosystem_id": "GLOBAL-SERVER-CORE-ECOSYSTEM",
        "name": "GLOBAL SERVER CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["SERVER_RESOURCE_IDENTITY", "SERVER_LIFECYCLE_CONTRACTS", "PROVIDER_NEUTRAL_CONFIGURATION", "DEPLOYMENT_POLICY_METADATA", "HEALTH_STATE_CONTRACTS", "REGION_AND_ENVIRONMENT_TAXONOMY", "ACCESS_POLICY_METADATA", "INVENTORY_VALIDATION_RULES", "SERVER_PROVIDER_DISCOVERY"],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {"core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_server_core_ecosystem", "division_layout": "INDEPENDENT_SIBLING_ECOSYSTEM", "status": "CORE_CATALOG_ONLY", "division": "SERVER", "server_provider_count": 7, "provider_coverage_exhaustive": False, "live_provider_connections_verified": False, "remote_operations_enabled": False, "registry_persistence": "PROCESS_LOCAL_ONLY"},
    }
    security_core = {
        "ecosystem_id": "GLOBAL-SECURITY-CORE-ECOSYSTEM",
        "name": "GLOBAL SECURITY CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": [
            "SECURITY_DOMAIN_REGISTRY",
            "PROVIDER_SECURITY_METADATA",
            "IDENTITY_AND_ACCESS_POLICY_METADATA",
            "THREAT_AND_VULNERABILITY_METADATA",
            "GOVERNANCE_AND_AUDIT_METADATA",
            "NORMAL_TO_SUPREME_SERVICE_TIERS",
        ],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_security_core_ecosystem",
            "division_layout": "INDEPENDENT_SIBLING_ECOSYSTEM",
            "status": "CORE_CATALOG_ONLY",
            "division": "SECURITY",
            "security_domain_count": 33,
            "security_provider_count": 6,
            "domain_coverage_exhaustive": False,
            "provider_coverage_exhaustive": False,
            "live_provider_connections_verified": False,
            "security_enforcement_verified": False,
            "credential_storage": "EXTERNAL_SECRET_STORE_ONLY",
        },
    }
    people_life_core = {
        "ecosystem_id": "GLOBAL-PEOPLE-LIFE-CORE-ECOSYSTEM",
        "name": "GLOBAL PEOPLE LIFE CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": [
            "PEOPLE_LIFE_DOMAIN_REGISTRY",
            "LIFE_STAGE_AND_SERVICE_DISCOVERY",
            "PRIVACY_AND_SAFETY_POLICY_METADATA",
            "AGE_AND_CONSENT_POLICY_BOUNDARY",
            "WORK_FAMILY_AND_WELLBEING_TAXONOMY",
            "NORMAL_TO_SUPREME_SERVICE_TIERS",
        ],
        "parent_id": "GLOBAL-CORE-ECOSYSTEM",
        "metadata": {
            "core_module": "backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem",
            "division_layout": "INDEPENDENT_SIBLING_ECOSYSTEM",
            "status": "CORE_CATALOG_ONLY",
            "division": "PEOPLE-LIFE",
            "people_life_domain_count": 28,
            "age_restricted_domain_count": 11,
            "domain_coverage_exhaustive": False,
            "live_service_connections_verified": False,
            "adult_content_age_verification_required": True,
            "adult_content_consent_and_rights_required": True,
        },
    }
    records = [
        ROOT,
        *CATEGORIES,
        infrastructure_core,
        integrations_core,
        human_language_core,
        programming_language_core,
        server_core,
        security_core,
        people_life_core,
        *CLOUDFLARE_CORE_ECOSYSTEMS,
        *COMMUNICATION_CORE_ECOSYSTEMS,
        *DEVELOPER_CORE_ECOSYSTEMS,
        *DOMAIN_CORE_ECOSYSTEMS,
        *PERSONAL_REGISTRATIONS,
        *COMPANY_REGISTRATIONS,
    ]
    return [_normalize_record(record) for record in records]


def get_category_catalog() -> list[dict[str, Any]]:
    """Return independent copies of all ecosystem categories."""
    return [_normalize_record(record) for record in CATEGORIES]


def get_registration_catalog() -> list[dict[str, Any]]:
    """Return independent copies of the 8 existing registrations."""
    records = [
        *PERSONAL_REGISTRATIONS,
        *COMPANY_REGISTRATIONS,
    ]
    return [_normalize_record(record) for record in records]


from .models import GlobalEcosystemIdentity
from .registry import GlobalEcosystemRegistry


class GlobalEcosystemManager:
    """Manage the canonical GLOBAL ECOSYSTEM hierarchy."""

    ROOT_ID = ROOT_ID
    ROOT_NAME = "GLOBAL ECOSYSTEM"
    VERSION = "1.0.0"
    CORE_ID = "GLOBAL-CORE-ECOSYSTEM"

    def __init__(self) -> None:
        self.registry = GlobalEcosystemRegistry()
        self._initialize()

    @staticmethod
    def _to_identity(record: dict[str, Any]) -> GlobalEcosystemIdentity:
        return GlobalEcosystemIdentity(
            ecosystem_id=record["ecosystem_id"],
            name=record["name"],
            ecosystem_type=record["ecosystem_type"],
            repository_ref=record.get("repository_ref"),
            status=record.get("status", "REGISTERED"),
            enabled=record.get("enabled", True),
            capabilities=list(record.get("capabilities", [])),
            metadata=dict(record.get("metadata", {})),
            message=record.get("message"),
            parent_id=record.get("parent_id"),
        )

    def _initialize(self) -> None:
        """Register catalog entries in parent-first order."""
        # get_catalog() is the single canonical source; provider entries are already included there.
        records = get_catalog()

        if not records:
            raise RuntimeError("GLOBAL ECOSYSTEM catalog is empty")

        # The canonical Core catalog already contains provider roots and
        # provider child records (Google and Stripe). Register that catalog once.
        registered_ids: set[str] = set()
        for record in records:
            identity = self._to_identity(record)
            ecosystem_id = identity.ecosystem_id

            if ecosystem_id in registered_ids:
                raise RuntimeError(f"Duplicate ecosystem ID in catalog: {ecosystem_id}")

            parent_id = identity.parent_id
            if parent_id and parent_id not in registered_ids:
                raise RuntimeError(
                    f"Parent must appear before child: {ecosystem_id} -> {parent_id}"
                )

            try:
                self.registry.register(identity)
            except (ValueError, KeyError) as exc:
                raise RuntimeError(
                    f"Initialization failed for {ecosystem_id}: {exc}"
                ) from exc

            registered_ids.add(ecosystem_id)

        if self.ROOT_ID not in registered_ids:
            raise RuntimeError("GLOBAL ECOSYSTEM root is missing")

    def status(self) -> dict[str, Any]:
        root = self.registry.get(self.ROOT_ID)

        return {
            "success": root is not None,
            "ecosystem_id": self.ROOT_ID,
            "name": self.ROOT_NAME,
            "version": self.VERSION,
            "status": "FOUNDATION" if root else "NOT_INITIALIZED",
            "count": self.registry.count(),
        }

    def health(self) -> dict[str, Any]:
        root_exists = self.registry.exists(self.ROOT_ID)
        core_exists = self.registry.exists(self.CORE_ID)
        healthy = root_exists and core_exists

        return {
            "success": healthy,
            "root_exists": root_exists,
            "core_exists": core_exists,
            "registry_count": self.registry.count(),
            "status": (
                "FOUNDATION_READY"
                if healthy
                else "FOUNDATION_INCOMPLETE"
            ),
        }

    def list(self) -> dict[str, Any]:
        ecosystems = self.registry.list()

        return {
            "success": True,
            "count": len(ecosystems),
            "ecosystems": ecosystems,
        }

    def names(self) -> dict[str, Any]:
        names = self.registry.names()

        return {
            "success": True,
            "count": len(names),
            "names": names,
        }

    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        return self.registry.get(ecosystem_id)

    def exists(self, ecosystem_id: str) -> bool:
        return self.registry.exists(ecosystem_id)

    def register(
        self,
        identity: GlobalEcosystemIdentity,
    ) -> dict[str, Any]:
        ecosystem_id = identity.ecosystem_id.strip()

        if not ecosystem_id:
            return {
                "success": False,
                "error": "ECOSYSTEM_ID_REQUIRED",
            }

        if ecosystem_id == self.ROOT_ID:
            return {
                "success": False,
                "error": "ROOT_ALREADY_INITIALIZED",
            }

        if self.registry.exists(ecosystem_id):
            return {
                "success": False,
                "error": "ECOSYSTEM_ALREADY_EXISTS",
                "ecosystem_id": ecosystem_id,
            }

        if not identity.parent_id:
            identity.parent_id = self.ROOT_ID

        if not self.registry.exists(identity.parent_id):
            return {
                "success": False,
                "error": "PARENT_NOT_FOUND",
                "parent_id": identity.parent_id,
            }

        try:
            registered = self.registry.register(identity)
        except (ValueError, KeyError) as exc:
            return {
                "success": False,
                "error": "REGISTRATION_FAILED",
                "message": str(exc),
                "ecosystem_id": ecosystem_id,
            }

        return {
            "success": True,
            "ecosystem": registered,
        }

    def google_catalog_status(self) -> dict[str, Any]:
        """Report CORE-owned Google catalog readiness without consulting API modules."""
        from backend.core.global_ecosystem.global_core_ecosystem.google_core_ecosystem.catalog import (
            get_google_core_catalog,
        )
        from backend.global_ecosystem.google_ecosystem.runtime.service import GoogleEcosystemService

        google_catalog = get_google_core_catalog()
        root = self.registry.get("GOOGLE-CORE-ECOSYSTEM")
        return {
            "success": root is not None,
            "ecosystem_id": "GLOBAL-GOOGLE-CORE-ECOSYSTEM",
            "status": "CORE_REGISTERED" if root else "NOT_REGISTERED",
            "api_family_count": len(google_catalog["children"]),
            "product_count": len(GoogleEcosystemService().catalog()),
            "core_module_count": len(google_catalog["children"]),
            "live_connection_verified": False,
            "oauth_flow_status": "PENDING_IMPLEMENTATION",
            "token_storage_status": "NOT_IMPLEMENTED",
            "security_note": "CORE-owned catalog metadata only; no API service is imported or invoked.",
        }

    def test_google_gemini_connection(self, api_key: str | None = None) -> dict[str, Any]:
        """CORE does not invoke API-layer clients; report the boundary explicitly."""
        return {
            "success": False,
            "ecosystem_id": "GLOBAL-GOOGLE-GEMINI-CORE-ECOSYSTEM",
            "status": "NOT_IMPLEMENTED_IN_CORE",
            "connection_tested": False,
            "credential_persisted": False,
            "error": "CORE_API_LAYER_ISOLATION",
            "message": "Gemini API connectivity checks belong to the independent API layer.",
        }

    def tree(self) -> dict[str, Any]:
        records = self.registry.list()

        by_id = {
            record["ecosystem_id"]: {
                **record,
                "children": [],
            }
            for record in records
        }

        for record in records:
            parent_id = record.get("parent_id")
            ecosystem_id = record["ecosystem_id"]

            if parent_id in by_id:
                by_id[parent_id]["children"].append(
                    by_id[ecosystem_id]
                )

        root = by_id.get(self.ROOT_ID)

        return {
            "success": root is not None,
            "tree": root,
        }

    def connection_map(self) -> dict[str, Any]:
        records = self.registry.list()

        edges = [
            {
                "source": record["parent_id"],
                "target": record["ecosystem_id"],
                "relationship": "CONTAINS",
            }
            for record in records
            if record.get("parent_id")
        ]

        return {
            "success": True,
            "node_count": len(records),
            "edge_count": len(edges),
            "edges": edges,
        }


EcosystemManager = GlobalEcosystemManager


_manager_instance: GlobalEcosystemManager | None = None


def get_manager() -> GlobalEcosystemManager:
    """Return the shared GLOBAL ECOSYSTEM manager instance."""
    global _manager_instance
    if _manager_instance is None:
        _manager_instance = GlobalEcosystemManager()
    return _manager_instance
