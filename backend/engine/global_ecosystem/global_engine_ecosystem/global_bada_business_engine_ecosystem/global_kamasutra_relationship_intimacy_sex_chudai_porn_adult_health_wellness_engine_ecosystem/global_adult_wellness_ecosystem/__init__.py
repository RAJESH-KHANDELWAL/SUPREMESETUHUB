"""ENGINE package marker and metadata for this independent package."""
LAYER = "ENGINE"
PACKAGE_NAME = __name__.rsplit(".", 1)[-1]
ECOSYSTEM_NAME = PACKAGE_NAME.replace("_", " ").upper()
ECOSYSTEM_ID = PACKAGE_NAME.upper().replace("_", "-")
__all__ = ["LAYER", "PACKAGE_NAME", "ECOSYSTEM_NAME", "ECOSYSTEM_ID"]
