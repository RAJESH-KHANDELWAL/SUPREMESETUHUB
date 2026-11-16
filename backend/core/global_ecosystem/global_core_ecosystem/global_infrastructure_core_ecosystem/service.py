"""CORE validation boundary for normalized infrastructure resource records."""
from __future__ import annotations
from collections.abc import Mapping
from typing import Any
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem.model.global_ecosystem.global_model_ecosystem import validate_resource_record
from .constants import ECOSYSTEM_ID,ECOSYSTEM_NAME,STATUS
from .policy import redact_sensitive_metadata

class GlobalInfrastructureCoreService:
    """Validate provider-neutral resource identity; never calls providers."""
    def describe(self)->dict[str,Any]:
        return {"layer":"CORE","ecosystem_id":ECOSYSTEM_ID,"ecosystem":ECOSYSTEM_NAME,
                "status":STATUS,"provider_operations_enabled":False}
    def validate_resource(self,payload:Mapping[str,Any])->dict[str,Any]:
        if not isinstance(payload,Mapping):
            return {"success":False,"error":"INFRASTRUCTURE_RESOURCE_VALIDATION_FAILED",
                    "validation_errors":["resource payload must be a mapping"]}
        errors=validate_resource_record(payload)
        if errors:
            return {"success":False,"error":"INFRASTRUCTURE_RESOURCE_VALIDATION_FAILED","validation_errors":errors}
        resource=dict(payload)
        resource["metadata"]=redact_sensitive_metadata(resource.get("metadata",{}))
        return {"success":True,"resource":resource,"validated_by":"GLOBAL_INFRASTRUCTURE_CORE"}
