from ..contracts import TokenizeRequest, validate_request
class CapabilityCoreService:
    capability = "tokenize"
    def validate(self, request: TokenizeRequest) -> bool:
        return validate_request(request)
