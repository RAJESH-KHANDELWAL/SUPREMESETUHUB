"""Prevent credentials from leaking into ordinary request metadata."""
SECRET_FIELD_NAMES = frozenset({"api_key", "token", "secret", "password", "authorization"})
def assert_no_secret_fields(mapping):
    found = SECRET_FIELD_NAMES.intersection(str(key).lower() for key in mapping)
    if found:
        raise ValueError("Secret material must be injected by a secure runtime, not passed in request metadata")
