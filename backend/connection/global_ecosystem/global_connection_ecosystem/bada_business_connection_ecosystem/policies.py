"""Bada Business connection safety policies."""

DEFAULT_REQUIRE_APPROVAL = True
DEFAULT_ENABLED = False
ALLOWED_CONNECTION_TYPES = ("api", "webhook", "service", "server")


def validate_bada_business_connection(request):
    errors = []
    required = ("connection_id", "provider_id", "server_id", "connection_type", "protocol")
    for field in required:
        if not getattr(request, field, None):
            errors.append(f"Missing required field: {field}")
    if request.connection_type not in ALLOWED_CONNECTION_TYPES:
        errors.append("Unsupported Bada Business connection_type")
    return tuple(errors)
