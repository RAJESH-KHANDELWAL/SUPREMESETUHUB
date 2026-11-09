"""Canonical GLOBAL CORE ECOSYSTEM catalog within CORE → GLOBAL ECOSYSTEM."""

from __future__ import annotations

from copy import deepcopy
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
        "ecosystem_id": "GLOBAL-SECURITY-CORE-ECOSYSTEM",
        "name": "GLOBAL SECURITY CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["SECURITY_SERVICE", "POLICY_ENFORCEMENT", "AUDIT"],
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
        "ecosystem_id": "GLOBAL-SERVER-CORE-ECOSYSTEM",
        "name": "GLOBAL SERVER CORE ECOSYSTEM",
        "ecosystem_type": "CORE_SERVICE",
        "capabilities": ["SERVER_LIFECYCLE", "HEALTH_CHECKS", "DEPLOYMENT_COORDINATION"],
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
    records = [
        ROOT,
        *CATEGORIES,
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
