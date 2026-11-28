"""Foundation safety checks."""
import json
from pathlib import Path
ROOT = Path(__file__).parents[1]
def test_manifest_defaults_to_disabled_operations():
    data = json.loads((ROOT / "ecosystem_manifest.json").read_text())
    assert data["foundation_status"] == "NOT_CONFIGURED"
    assert data["storage_operations_enabled"] is False
