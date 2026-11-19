"""Safety and lifecycle policy metadata for infrastructure CORE."""
from collections.abc import Mapping
SENSITIVE_METADATA_KEYS=frozenset({"password","secret","client_secret","api_key","access_token","refresh_token","authorization","private_key","credential","credential_value","connection_string"})
def validate_metadata(metadata):
 if metadata is None:return []
 if not isinstance(metadata,Mapping):return ["metadata must be a mapping"]
 return []
def redact_sensitive_metadata(value):
 if isinstance(value,Mapping):return {str(k):redact_sensitive_metadata(v) for k,v in value.items() if str(k).lower() not in SENSITIVE_METADATA_KEYS}
 if isinstance(value,list):return [redact_sensitive_metadata(v) for v in value]
 if isinstance(value,tuple):return tuple(redact_sensitive_metadata(v) for v in value)
 return value
