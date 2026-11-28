"""SUPREME module manifest for backend-side Python tooling."""
MODULE_NAME = "SUPREME"
DISPLAY_NAME = "SUPREME by SUPREMESETUHUB"
PARENT_BRAND = "DR RAJESH KHANDELWAL IBC"
IDENTITY_FOLDERS = [
    "dr_rajesh_khandelwal_ibc",
    "dr_rajesh_khandelwal_ibc_official",
    "rajesh_khandelwal",
    "rajesh_khandelwal_official"
]

def module_manifest() -> dict:
    return {
        "module": MODULE_NAME,
        "display_name": DISPLAY_NAME,
        "parent_brand": PARENT_BRAND,
        "identity_folders": list(IDENTITY_FOLDERS),
    }
