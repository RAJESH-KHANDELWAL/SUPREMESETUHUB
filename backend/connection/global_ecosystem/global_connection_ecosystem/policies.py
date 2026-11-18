"""Default-deny policies for global connection operations."""

SENSITIVE_OPERATIONS = ("authorize", "connect", "disconnect", "disable")


def validate_connection_request(request):
    required = ("connection_id", "provider_id", "server_id", "connection_type", "protocol")
    missing = [name for name in required if not getattr(request, name, None)]
    return tuple(f"Missing required field: {name}" for name in missing)
