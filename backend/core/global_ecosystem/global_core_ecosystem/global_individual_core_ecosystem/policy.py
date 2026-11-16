"""Metadata-only privacy and capability policy guardrails."""
from collections.abc import Mapping
SENSITIVE_MARKERS=("IDENTITY","KYC","AGE","HEALTH","FINANCE","WALLET","ADULT","INTIMACY","CONSENT","PAYMENT","PRIVATE")
_SECRET_KEYS={"token","access_token","refresh_token","client_secret","api_key","secret","authorization","password","credential_value","private_key","ssn","government_id","id_number","medical_record","email","phone","mobile","date_of_birth","birth_date","dob","address","aadhaar","aadhaar_number","pan_number","passport_number","bank_account","card_number"}
class GlobalIndividualCorePolicyError(PermissionError):pass
class GlobalIndividualCorePolicy:
 @staticmethod
 def require_tenant_context(context):
  if context is None or not callable(getattr(context,"validate",None)):raise GlobalIndividualCorePolicyError("AUTHENTICATED_TENANT_CONTEXT_REQUIRED")
  context.validate()
 @staticmethod
 def classify_capability(capability:str)->str:
  value=str(capability).upper()
  return "SENSITIVE_REQUIRES_EXPLICIT_AUTHORIZATION_CONSENT_AND_AUDIT" if any(x in value for x in SENSITIVE_MARKERS) else "STANDARD_REQUIRES_TENANT_AND_APPLICATION_AUTHORIZATION"
 @staticmethod
 def safe_metadata(value):
  if isinstance(value,Mapping):return {k:GlobalIndividualCorePolicy.safe_metadata(v) for k,v in value.items() if str(k).casefold().replace("-","_") not in _SECRET_KEYS}
  if isinstance(value,(tuple,list)):return [GlobalIndividualCorePolicy.safe_metadata(v) for v in value]
  return value
__all__=["GlobalIndividualCorePolicy","GlobalIndividualCorePolicyError"]
