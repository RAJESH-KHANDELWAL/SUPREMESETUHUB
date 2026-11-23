from ..contracts import CommandRequest, validate_request
class CapabilityCoreService:
    capability = "command"
    def validate(self, request: CommandRequest) -> bool:
        return validate_request(request)
