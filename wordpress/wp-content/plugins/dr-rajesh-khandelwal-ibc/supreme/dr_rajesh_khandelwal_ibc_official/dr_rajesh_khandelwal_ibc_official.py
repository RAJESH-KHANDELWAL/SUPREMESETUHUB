"""Backend-side identity manifest for dr_rajesh_khandelwal_ibc_official."""
IDENTITY_NAME = "dr_rajesh_khandelwal_ibc_official"
PARENT_MODULE = "SUPREME"
PARENT_BRAND = "DR RAJESH KHANDELWAL IBC"

def identity_manifest() -> dict:
    return {
        "identity": IDENTITY_NAME,
        "parent_module": PARENT_MODULE,
        "parent_brand": PARENT_BRAND,
    }
