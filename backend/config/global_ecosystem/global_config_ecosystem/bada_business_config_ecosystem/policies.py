"""Safe defaults and validation rules for Bada Business configuration."""

ALLOWED_ENVIRONMENTS = ("development", "testing", "staging", "production")
DEFAULT_REQUIRE_APPROVAL = True
DEFAULT_ENABLED = False
MIN_REQUEST_TIMEOUT_SECONDS = 1
MAX_REQUEST_TIMEOUT_SECONDS = 120


def validate_bada_business_values(values):
    errors = []
    environment = values.get("environment", "development")
    if environment not in ALLOWED_ENVIRONMENTS:
        errors.append("environment must be one of: " + ", ".join(ALLOWED_ENVIRONMENTS))
    timeout = values.get("request_timeout_seconds", 15)
    if not isinstance(timeout, int) or isinstance(timeout, bool) or not MIN_REQUEST_TIMEOUT_SECONDS <= timeout <= MAX_REQUEST_TIMEOUT_SECONDS:
        errors.append(f"request_timeout_seconds must be an integer from {MIN_REQUEST_TIMEOUT_SECONDS} to {MAX_REQUEST_TIMEOUT_SECONDS}")
    if not isinstance(values.get("enabled", False), bool):
        errors.append("enabled must be a boolean")
    if not isinstance(values.get("require_approval", True), bool):
        errors.append("require_approval must be a boolean")
    return tuple(errors)
