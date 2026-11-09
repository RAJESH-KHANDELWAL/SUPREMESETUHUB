"""Trust, safety and evidence policies for Bada Business AI."""
BADA_BUSINESS_AI_POLICY = {
    "policy_id": "bada_business_ai_default",
    "version": "1.0",
    "evidence_rules": {
        "use_canonical_resource_catalog": True,
        "distinguish_verified_facts_from_user_supplied_metadata": True,
        "never_invent_prices_or_program_benefits": True,
        "check_time_sensitive_event_availability": True,
        "disclose_missing_or_unverified_information": True,
    },
    "commercial_rules": {
        "no_guaranteed_income_or_business_success_claims": True,
        "no_unsupported_affiliate_or_provider_relationship_claims": True,
        "disclose_referral_links_when_relevant": True,
        "no_automatic_purchase_or_registration": True,
    },
    "privacy_rules": {
        "consent_required_for_lead_data_use": True,
        "no_implicit_sensitive_data_storage": True,
        "minimum_necessary_data": True,
    },
    "approval_required_for": [
        "external_message_or_campaign_publication",
        "lead_data_export",
        "registration_or_purchase",
        "financial_or_account_action",
    ],
}
