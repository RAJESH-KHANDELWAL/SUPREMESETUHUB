SECRET_FIELDS = frozenset({"api_key", "token", "secret", "password", "authorization"})
def assert_no_secret_fields(payload):
    found = SECRET_FIELDS.intersection(str(key).lower() for key in payload)
    if found:
        raise ValueError("Secrets must be injected by secure runtime, not CORE request metadata")
