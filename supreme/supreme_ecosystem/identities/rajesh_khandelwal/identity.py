"""RAJESH KHANDELWAL identity metadata for SUPREME ECOSYSTEM.

Metadata only: do not put passwords, tokens, or private account data here.
"""
IDENTITY = {
    "slug": "rajesh_khandelwal",
    "display_name": "RAJESH KHANDELWAL",
    "username": "RAJESHKHANDELWAL",
    "scope": "SUPREME_ECOSYSTEM",
    "status": "REGISTERED_METADATA",
}
def get_identity() -> dict:
    """Return a copy of public identity metadata."""
    return dict(IDENTITY)
