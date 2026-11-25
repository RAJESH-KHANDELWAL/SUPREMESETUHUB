from ..contracts import RerankRequest, validate_request
class CapabilityCoreService:
    capability = "rerank"
    def validate(self, request: RerankRequest) -> bool:
        return validate_request(request)
