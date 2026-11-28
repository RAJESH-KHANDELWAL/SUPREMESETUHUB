"""Reusable, folder-aware manager for relationship CORE sub-ecosystems."""
from __future__ import annotations
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
MODULE_KEY=Path(__file__).resolve().parent.name
_REQUIRED={"adult_affiliate_referral_relationships_core_ecosystem":["referral_program_id","commission_terms","referral_code"],"adult_complaints_takedown_dispute_relationships_core_ecosystem":["case_id","case_status","submitted_at"],"adult_content_distribution_licensing_relationships_core_ecosystem":["license_id","scope","territory","term"],"adult_content_hosting_cdn_relationships_core_ecosystem":["service_id","content_scope","region"],"adult_content_production_services_relationships_core_ecosystem":["service_agreement_id","service_scope"],"adult_creator_agency_management_relationships_core_ecosystem":["agency_id","management_scope","consent_status"],"adult_creator_business_relationships_core_ecosystem":["business_entity_id","creator_entity_id","agreement_id"],"adult_discovery_search_metadata_relationships_core_ecosystem":["platform_id","metadata_scope","visibility_status"],"adult_entertainment_studio_relationships_core_ecosystem":["studio_entity_id","production_scope","rights_status"],"adult_industry_payment_payout_relationships_core_ecosystem":["payment_provider_id","payout_account_ref","status"],"adult_industry_relationship_taxonomy":["relationship_category","definition","jurisdiction_scope"],"adult_legal_compliance_regional_relationships_core_ecosystem":["jurisdiction","compliance_scope","reviewed_at"],"adult_live_streaming_relationships_core_ecosystem":["platform_id","stream_scope","consent_status"],"adult_performer_rights_consent_relationships_core_ecosystem":["rights_holder_id","consent_record_id","rights_scope"],"adult_platform_operator_relationships_core_ecosystem":["operator_entity_id","platform_id","operator_scope"],"adult_privacy_security_identity_relationships_core_ecosystem":["identity_ref","privacy_basis","security_scope"],"adult_regional_market_access_relationships_core_ecosystem":["region","market_access_status","legal_review_ref"],"adult_subscription_membership_relationships_core_ecosystem":["subscription_id","member_ref","membership_status"],"age_verification_consent_relationships_core_ecosystem":["verification_method","verification_status","consent_timestamp"],"brand_trademark_relationships_core_ecosystem":["brand_id","trademark_ref","owner_entity_id"],"business_partner_supplier_relationships_core_ecosystem":["partner_entity_id","relationship_scope","agreement_ref"],"commerce_marketplace_relationships_core_ecosystem":["marketplace_id","seller_ref","commercial_scope"],"company_ownership_control_relationships_core_ecosystem":["owner_entity_id","owned_entity_id","ownership_percent"],"corporate_group_relationships_core_ecosystem":["parent_entity_id","member_entity_id","group_role"],"dating_relationships_platform_core_ecosystem":["platform_id","user_consent","relationship_scope"],"developer_api_provider_relationships_core_ecosystem":["provider_id","api_name","access_scope"],"digital_platform_social_media_relationships_core_ecosystem":["platform_id","account_ref","relationship_scope"],"founder_director_management_relationships_core_ecosystem":["person_entity_id","organization_entity_id","role","effective_date"],"global_entity_relationships_core_ecosystem":["source_entity_id","target_entity_id","relationship_type"],"india_entity_relationships_core_ecosystem":["entity_id","india_registration_ref","jurisdiction"],"normal_standard_advanced_enterprise_supreme_relationship_tiers":["tier_name","tier_scope","eligibility"],"payments_finance_relationships_core_ecosystem":["financial_entity_id","relationship_type","financial_scope"],"relationship_verification_provenance_core_ecosystem":["relationship_id","evidence_source","verification_status"],"sexual_health_relationships_resource_core_ecosystem":["resource_id","resource_type","source_organization","review_date"],"sexual_wellness_education_relationships_core_ecosystem":["resource_id","education_topic","source_organization","review_date"],"trust_safety_moderation_relationships_core_ecosystem":["case_ref","moderation_action","policy_basis"]}
REQUIRED_FIELDS=_REQUIRED.get(MODULE_KEY, [])
TITLE=MODULE_KEY.removesuffix("_core_ecosystem").replace("_"," ").upper()
ECOSYSTEM_NAME="GLOBAL "+TITLE+" CORE ECOSYSTEM"
ECOSYSTEM_ID="GLOBAL-"+MODULE_KEY.removesuffix("_core_ecosystem").replace("_","-").upper()+"-CORE-ECOSYSTEM"
class ValidationError(ValueError): pass
class RelationshipModuleManager:
 def status(self): return {"ecosystem_id":ECOSYSTEM_ID,"name":ECOSYSTEM_NAME,"module_key":MODULE_KEY,"required_fields":list(REQUIRED_FIELDS),"status":"METADATA_AND_VALIDATION_ONLY","live_connection_verified":False,"persistence_enabled":False}
 def contract(self): return {"required_fields":list(REQUIRED_FIELDS),"common_fields":["relationship_id","source_entity_id","target_entity_id","relationship_type","verification_status","source_urls","metadata"],"verification_states":["UNVERIFIED","PENDING_REVIEW","VERIFIED","REJECTED","EXPIRED"],"evidence_required_for_verified":True}
 def normalize(self,record):
  if not isinstance(record,dict): raise ValidationError("Expected a dict record")
  value=deepcopy(record)
  for key in ("relationship_id","source_entity_id","target_entity_id"):
   if isinstance(value.get(key),str): value[key]=value[key].strip()
  value.setdefault("verification_status","UNVERIFIED"); value.setdefault("source_urls",[]); value.setdefault("metadata",{})
  return value
 def validate(self,record):
  value=self.normalize(record); missing=[f for f in REQUIRED_FIELDS if value.get(f) in (None,"")]
  if missing: raise ValidationError("Missing category-specific fields: "+", ".join(missing))
  source=value.get("source_entity_id"); target=value.get("target_entity_id")
  if source and target and source==target: raise ValidationError("Self relationship is disallowed")
  state=value.get("verification_status")
  if state not in {"UNVERIFIED","PENDING_REVIEW","VERIFIED","REJECTED","EXPIRED"}: raise ValidationError("Invalid verification status")
  evidence=value.get("source_urls") or []
  if state=="VERIFIED" and (not evidence or any(not str(x).startswith(("http://","https://")) for x in evidence)): raise ValidationError("Verified relationships require evidence URLs")
  return {"valid":True,"ecosystem_id":ECOSYSTEM_ID,"record":value,"checked_at":datetime.now(timezone.utc).isoformat()}
 def get_required_fields(self): return list(REQUIRED_FIELDS)
def get_manager(): return RelationshipModuleManager()
