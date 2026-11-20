"""Canonical individual module inventory."""
from copy import deepcopy
MODULES=[
  {
    "module_id": "GLOBAL-INDIVIDUAL-SERVICES-CORE-ECOSYSTEM",
    "directory": "global_individual_services_core_ecosystem",
    "name": "Global Individual Services",
    "master_entry_ids": [
      "S02_individual",
      "S02_human_identity",
      "S02_community"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIA-INDIVIDUAL-SERVICES-CORE-ECOSYSTEM",
    "directory": "india_individual_services_core_ecosystem",
    "name": "India Individual Services",
    "master_entry_ids": [
      "S02_individual",
      "S02_human_identity"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ACCOUNT-ACCESS-CORE-ECOSYSTEM",
    "directory": "individual_account_access_core_ecosystem",
    "name": "Individual Account Access",
    "master_entry_ids": [
      "S02_human_identity",
      "S02_individual"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-AGE-VERIFICATION-CORE-ECOSYSTEM",
    "directory": "individual_adult_age_verification_core_ecosystem",
    "name": "Individual Adult Age Verification",
    "master_entry_ids": [
      "S02_adults",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-CONTENT-CREATOR-CORE-ECOSYSTEM",
    "directory": "individual_adult_content_creator_core_ecosystem",
    "name": "Individual Adult Content Creator",
    "master_entry_ids": [
      "S02_adults",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-CONTENT-DISTRIBUTION-LICENSING-CORE-ECOSYSTEM",
    "directory": "individual_adult_content_distribution_licensing_core_ecosystem",
    "name": "Individual Adult Content Distribution Licensing",
    "master_entry_ids": [
      "S02_adults",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-CONTENT-PRODUCTION-STUDIO-CORE-ECOSYSTEM",
    "directory": "individual_adult_content_production_studio_core_ecosystem",
    "name": "Individual Adult Content Production Studio",
    "master_entry_ids": [
      "S02_adults",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-ENTERTAINMENT-PLATFORMS-CORE-ECOSYSTEM",
    "directory": "individual_adult_entertainment_platforms_core_ecosystem",
    "name": "Individual Adult Entertainment Platforms",
    "master_entry_ids": [
      "S02_adults",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-LEGAL-REGIONAL-COMPLIANCE-CORE-ECOSYSTEM",
    "directory": "individual_adult_legal_regional_compliance_core_ecosystem",
    "name": "Individual Adult Legal Regional Compliance",
    "master_entry_ids": [
      "S02_human_rights",
      "S02_adults"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-LIVE-STREAMING-CORE-ECOSYSTEM",
    "directory": "individual_adult_live_streaming_core_ecosystem",
    "name": "Individual Adult Live Streaming",
    "master_entry_ids": [
      "S02_adults",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-MODERATION-SAFETY-TAKEDOWN-CORE-ECOSYSTEM",
    "directory": "individual_adult_moderation_safety_takedown_core_ecosystem",
    "name": "Individual Adult Moderation Safety Takedown",
    "master_entry_ids": [
      "S02_human_rights",
      "S02_adults"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-PAYMENTS-PAYOUTS-CORE-ECOSYSTEM",
    "directory": "individual_adult_payments_payouts_core_ecosystem",
    "name": "Individual Adult Payments Payouts",
    "master_entry_ids": [
      "S02_adults",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-PERFORMER-RIGHTS-CONSENT-CORE-ECOSYSTEM",
    "directory": "individual_adult_performer_rights_consent_core_ecosystem",
    "name": "Individual Adult Performer Rights Consent",
    "master_entry_ids": [
      "S02_human_rights",
      "S02_adults"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-PRIVACY-SECURITY-CORE-ECOSYSTEM",
    "directory": "individual_adult_privacy_security_core_ecosystem",
    "name": "Individual Adult Privacy Security",
    "master_entry_ids": [
      "S02_human_rights",
      "S02_adults"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-ADULT-SUBSCRIPTION-MEMBERSHIP-CORE-ECOSYSTEM",
    "directory": "individual_adult_subscription_membership_core_ecosystem",
    "name": "Individual Adult Subscription Membership",
    "master_entry_ids": [
      "S02_adults",
      "S02_individual"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-CLOUD-STORAGE-CORE-ECOSYSTEM",
    "directory": "individual_cloud_storage_core_ecosystem",
    "name": "Individual Cloud Storage",
    "master_entry_ids": [
      "S02_individual",
      "S02_human_identity"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-COMMUNICATION-SOCIAL-CORE-ECOSYSTEM",
    "directory": "individual_communication_social_core_ecosystem",
    "name": "Individual Communication Social",
    "master_entry_ids": [
      "S02_individual",
      "S02_community",
      "S02_society"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-DATING-RELATIONSHIPS-CORE-ECOSYSTEM",
    "directory": "individual_dating_relationships_core_ecosystem",
    "name": "Individual Dating Relationships",
    "master_entry_ids": [
      "S02_individual",
      "S02_adults",
      "S02_human_behaviour"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-DOCUMENTS-DIGITAL-LOCKER-CORE-ECOSYSTEM",
    "directory": "individual_documents_digital_locker_core_ecosystem",
    "name": "Individual Documents Digital Locker",
    "master_entry_ids": [
      "S02_human_identity",
      "S02_individual"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-EDUCATION-LEARNING-CORE-ECOSYSTEM",
    "directory": "individual_education_learning_core_ecosystem",
    "name": "Individual Education Learning",
    "master_entry_ids": [
      "S02_education",
      "S02_knowledge",
      "S02_skills_and_talents"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-IDENTITY-PROFILE-CORE-ECOSYSTEM",
    "directory": "individual_identity_profile_core_ecosystem",
    "name": "Individual Identity Profile",
    "master_entry_ids": [
      "S02_human_identity",
      "S02_individual"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-INTIMACY-RELATIONSHIP-COACHING-CORE-ECOSYSTEM",
    "directory": "individual_intimacy_relationship_coaching_core_ecosystem",
    "name": "Individual Intimacy Relationship Coaching",
    "master_entry_ids": [
      "S02_individual",
      "S02_human_behaviour",
      "S02_adults"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-KYC-VERIFICATION-CORE-ECOSYSTEM",
    "directory": "individual_kyc_verification_core_ecosystem",
    "name": "Individual KYC Verification",
    "master_entry_ids": [
      "S02_human_identity",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-PRIVACY-SECURITY-CORE-ECOSYSTEM",
    "directory": "individual_privacy_security_core_ecosystem",
    "name": "Individual Privacy Security",
    "master_entry_ids": [
      "S02_human_rights",
      "S02_human_identity"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-PROFESSIONAL-FREELANCER-CORE-ECOSYSTEM",
    "directory": "individual_professional_freelancer_core_ecosystem",
    "name": "Individual Professional Freelancer",
    "master_entry_ids": [
      "S02_individual",
      "S02_skills_and_talents"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-SERVICE-TIERS-NORMAL-TO-SUPREME-CORE-ECOSYSTEM",
    "directory": "individual_service_tiers_normal_to_supreme_core_ecosystem",
    "name": "Individual Service Tiers Normal to Supreme",
    "master_entry_ids": [
      "S02_individual"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-SEXUAL-WELLNESS-EDUCATION-CORE-ECOSYSTEM",
    "directory": "individual_sexual_wellness_education_core_ecosystem",
    "name": "Individual Sexual Wellness Education",
    "master_entry_ids": [
      "S02_adults",
      "S02_human_rights"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-WALLET-FINANCE-CORE-ECOSYSTEM",
    "directory": "individual_wallet_finance_core_ecosystem",
    "name": "Individual Wallet Finance",
    "master_entry_ids": [
      "S02_individual",
      "S02_human_identity"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  },
  {
    "module_id": "INDIVIDUAL-WELLNESS-HEALTH-RESOURCES-CORE-ECOSYSTEM",
    "directory": "individual_wellness_health_resources_core_ecosystem",
    "name": "Individual Wellness Health Resources",
    "master_entry_ids": [
      "S02_individual",
      "S02_human_development"
    ],
    "status": "CORE_CATALOG_ONLY",
    "connected": false
  }
]
INDIVIDUAL_CORE_ECOSYSTEM={"ecosystem_id":"GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM","name":"GLOBAL INDIVIDUAL CORE ECOSYSTEM","parent_id":"GLOBAL-CORE-ECOSYSTEM","modules":MODULES,"module_count":len(MODULES)}
def get_catalog(): return deepcopy(INDIVIDUAL_CORE_ECOSYSTEM)
def get_modules(): return deepcopy(MODULES)
def get_module(module_id):
    key=module_id.strip().upper()
    return next((deepcopy(x) for x in MODULES if key in (x["module_id"],x["directory"].upper())),None)
