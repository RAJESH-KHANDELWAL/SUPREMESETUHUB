from ..contracts import EmbedRequest, validate_request
class CapabilityCoreService:
    capability = "embed"
    def validate(self, request: EmbedRequest) -> bool:
        return validate_request(request)
