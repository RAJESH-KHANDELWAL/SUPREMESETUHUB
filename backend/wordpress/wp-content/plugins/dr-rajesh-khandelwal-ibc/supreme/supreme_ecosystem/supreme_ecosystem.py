"""Backend-side manifest for the SUPREME ECOSYSTEM submodule."""
MODULE_NAME = "SUPREME ECOSYSTEM"
DISPLAY_NAME = "SUPREME ECOSYSTEM by SUPREMESETUHUB"
PARENT_MODULE = "SUPREME"
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
        "parent_module": PARENT_MODULE,
        "identity_folders": list(IDENTITY_FOLDERS),
    }
