"""Provider package configuration loaded from its manifest."""
import json
from pathlib import Path
_MANIFEST = Path(__file__).with_name("ecosystem_manifest.json")
with _MANIFEST.open(encoding="utf-8") as _file:
    ECOSYSTEM_MANIFEST = json.load(_file)
PROVIDER_ID = ECOSYSTEM_MANIFEST["provider_id"]
LAYER = "CORE"
STATUS = "CORE_CATALOG_ONLY"
LIVE_CONNECTION_VERIFIED = False
API_TRANSPORT_OWNER = "API"
