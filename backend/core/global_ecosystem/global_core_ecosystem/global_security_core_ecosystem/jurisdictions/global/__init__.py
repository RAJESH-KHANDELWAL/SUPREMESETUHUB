"""Global cross-border reference profile metadata."""
import json
from pathlib import Path
JURISDICTION_MANIFEST = json.loads(Path(__file__).with_name("jurisdiction_manifest.json").read_text(encoding="utf-8"))
def get_jurisdiction_manifest():
    return json.loads(json.dumps(JURISDICTION_MANIFEST))
