"""Canonical registry for Global Individual Core capability ecosystems."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
ECOSYSTEM={"ecosystem_id":"GLOBAL-INDIVIDUAL-CORE-ECOSYSTEM","name":"GLOBAL INDIVIDUAL CORE ECOSYSTEM","layer":"CORE","parent_id":"GLOBAL-CORE-ECOSYSTEM","status":"CORE_CATALOG_ONLY","enabled":True,"api_available":None,"live_connection_verified":False,"api_calls_performed":0}
_CHILDREN=(
{"id":"global-individual-services","name":"GLOBAL INDIVIDUAL SERVICES","folder":"global_individual_services_core_ecosystem","domain":"INDIVIDUAL_SERVICES","scope":"Individual service discovery and lifecycle metadata."},
{"id":"india-individual-services","name":"INDIA INDIVIDUAL SERVICES","folder":"india_individual_services_core_ecosystem","domain":"INDIA_SERVICES","scope":"India-specific service taxonomy, localization and regulatory boundaries."},
{"id":"individual-account-access","name":"INDIVIDUAL ACCOUNT ACCESS","folder":"individual_account_access_core_ecosystem","domain":"ACCOUNT_ACCESS","scope":"Account lifecycle, access metadata and session-policy boundaries."},
{"id":"individual-adult-age-verification","name":"INDIVIDUAL ADULT AGE VERIFICATION","folder":"individual_adult_age_verification_core_ecosystem","domain":"AGE_VERIFICATION","scope":"Age assurance policy and verification-provider boundaries."},
{"id":"individual-adult-content-creator","name":"INDIVIDUAL ADULT CONTENT CREATOR","folder":"individual_adult_content_creator_core_ecosystem","domain":"ADULT_CREATOR","scope":"Creator identity and onboarding metadata with consent and age safeguards."},
{"id":"individual-adult-content-distribution-licensing","name":"INDIVIDUAL ADULT CONTENT DISTRIBUTION & LICENSING","folder":"individual_adult_content_distribution_licensing_core_ecosystem","domain":"CONTENT_LICENSING","scope":"Content rights, licensing metadata and territory restrictions."},
{"id":"individual-adult-content-production-studio","name":"INDIVIDUAL ADULT CONTENT PRODUCTION STUDIO","folder":"individual_adult_content_production_studio_core_ecosystem","domain":"PRODUCTION_STUDIO","scope":"Production workflow metadata, participant rights and release boundaries."},
{"id":"individual-adult-entertainment-platforms","name":"INDIVIDUAL ADULT ENTERTAINMENT PLATFORMS","folder":"individual_adult_entertainment_platforms_core_ecosystem","domain":"ADULT_PLATFORMS","scope":"Age-restricted platform registry; no content hosting or delivery execution."},
{"id":"individual-adult-legal-regional-compliance","name":"INDIVIDUAL ADULT LEGAL & REGIONAL COMPLIANCE","folder":"individual_adult_legal_regional_compliance_core_ecosystem","domain":"LEGAL_COMPLIANCE","scope":"Jurisdiction and legal-review metadata; qualified review remains required."},
{"id":"individual-adult-live-streaming","name":"INDIVIDUAL ADULT LIVE STREAMING","folder":"individual_adult_live_streaming_core_ecosystem","domain":"LIVE_STREAMING","scope":"Live-streaming capability metadata with consent and moderation boundaries."},
{"id":"individual-adult-moderation-safety-takedown","name":"INDIVIDUAL ADULT MODERATION, SAFETY & TAKEDOWN","folder":"individual_adult_moderation_safety_takedown_core_ecosystem","domain":"MODERATION_SAFETY","scope":"Safety reporting, moderation policy and takedown workflow metadata."},
{"id":"individual-adult-payments-payouts","name":"INDIVIDUAL ADULT PAYMENTS & PAYOUTS","folder":"individual_adult_payments_payouts_core_ecosystem","domain":"ADULT_PAYMENTS","scope":"Payment and payout provider metadata; regulated operations remain delegated."},
{"id":"individual-adult-performer-rights-consent","name":"INDIVIDUAL ADULT PERFORMER RIGHTS & CONSENT","folder":"individual_adult_performer_rights_consent_core_ecosystem","domain":"PERFORMER_RIGHTS","scope":"Affirmative consent, rights, releases and withdrawal metadata."},
{"id":"individual-adult-privacy-security","name":"INDIVIDUAL ADULT PRIVACY & SECURITY","folder":"individual_adult_privacy_security_core_ecosystem","domain":"ADULT_PRIVACY","scope":"Sensitive-data privacy, access control and security policy metadata."},
{"id":"individual-adult-subscription-membership","name":"INDIVIDUAL ADULT SUBSCRIPTION & MEMBERSHIP","folder":"individual_adult_subscription_membership_core_ecosystem","domain":"ADULT_MEMBERSHIP","scope":"Subscription and membership metadata; billing execution is delegated."},
{"id":"individual-cloud-storage","name":"INDIVIDUAL CLOUD STORAGE","folder":"individual_cloud_storage_core_ecosystem","domain":"CLOUD_STORAGE","scope":"Cloud-storage provider inventory, capabilities and retention metadata."},
{"id":"individual-communication-social","name":"INDIVIDUAL COMMUNICATION & SOCIAL","folder":"individual_communication_social_core_ecosystem","domain":"COMMUNICATION_SOCIAL","scope":"Messaging, notification and social-network capability metadata."},
{"id":"individual-dating-relationships","name":"INDIVIDUAL DATING & RELATIONSHIPS","folder":"individual_dating_relationships_core_ecosystem","domain":"DATING_RELATIONSHIPS","scope":"Dating and relationship platform metadata with privacy and safety boundaries."},
{"id":"individual-documents-digital-locker","name":"INDIVIDUAL DOCUMENTS & DIGITAL LOCKER","folder":"individual_documents_digital_locker_core_ecosystem","domain":"DOCUMENTS_LOCKER","scope":"Personal document and digital-locker metadata, classification and retention."},
{"id":"individual-education-learning","name":"INDIVIDUAL EDUCATION & LEARNING","folder":"individual_education_learning_core_ecosystem","domain":"EDUCATION_LEARNING","scope":"Learning platforms, courses, credentials and learning-resource metadata."},
{"id":"individual-identity-profile","name":"INDIVIDUAL IDENTITY & PROFILE","folder":"individual_identity_profile_core_ecosystem","domain":"IDENTITY_PROFILE","scope":"Identity and profile metadata; proofing is delegated to verification services."},
{"id":"individual-intimacy-relationship-coaching","name":"INDIVIDUAL INTIMACY & RELATIONSHIP COACHING","folder":"individual_intimacy_relationship_coaching_core_ecosystem","domain":"INTIMACY_COACHING","scope":"Coaching-service discovery and education metadata; no clinical diagnosis claims."},
{"id":"individual-kyc-verification","name":"INDIVIDUAL KYC & VERIFICATION","folder":"individual_kyc_verification_core_ecosystem","domain":"KYC_VERIFICATION","scope":"KYC provider and verification workflow metadata; evidence remains in authorized systems."},
{"id":"individual-privacy-security","name":"INDIVIDUAL PRIVACY & SECURITY","folder":"individual_privacy_security_core_ecosystem","domain":"PRIVACY_SECURITY","scope":"Privacy controls, data rights and security capability metadata."},
{"id":"individual-professional-freelancer","name":"INDIVIDUAL PROFESSIONAL & FREELANCER","folder":"individual_professional_freelancer_core_ecosystem","domain":"PROFESSIONAL_FREELANCER","scope":"Freelancer profile, professional service and work-platform metadata."},
{"id":"individual-service-tiers-normal-to-supreme","name":"INDIVIDUAL SERVICE TIERS NORMAL TO SUPREME","folder":"individual_service_tiers_normal_to_supreme_core_ecosystem","domain":"SERVICE_TIERS","scope":"Service-tier definitions and entitlement metadata; billing is delegated."},
{"id":"individual-sexual-wellness-education","name":"INDIVIDUAL SEXUAL WELLNESS EDUCATION","folder":"individual_sexual_wellness_education_core_ecosystem","domain":"SEXUAL_WELLNESS_EDUCATION","scope":"Age-appropriate sexual-wellness education resource metadata and safeguards."},
{"id":"individual-wallet-finance","name":"INDIVIDUAL WALLET & FINANCE","folder":"individual_wallet_finance_core_ecosystem","domain":"WALLET_FINANCE","scope":"Wallet and finance provider metadata; money movement and advice are delegated."},
{"id":"individual-wellness-health-resources","name":"INDIVIDUAL WELLNESS & HEALTH RESOURCES","folder":"individual_wellness_health_resources_core_ecosystem","domain":"WELLNESS_HEALTH","scope":"Wellness and health-resource metadata; clinical decisions remain in authorized systems."},
)
def list_capabilities(enabled_only:bool=False)->list[dict[str,Any]]:
 items=[deepcopy(x) for x in _CHILDREN]
 return [x for x in items if x.get("enabled",True)] if enabled_only else items
def get_capability(capability_id:str)->dict[str,Any]|None:
 if not isinstance(capability_id,str) or not capability_id.strip():return None
 key=capability_id.strip().casefold()
 for item in _CHILDREN:
  if key in {item["id"].casefold(),item["folder"].casefold()}:return deepcopy(item)
 return None
def get_catalog()->dict[str,Any]:return {"ecosystem":deepcopy(ECOSYSTEM),"capabilities":list_capabilities()}
__all__=["ECOSYSTEM","list_capabilities","get_capability","get_catalog"]
