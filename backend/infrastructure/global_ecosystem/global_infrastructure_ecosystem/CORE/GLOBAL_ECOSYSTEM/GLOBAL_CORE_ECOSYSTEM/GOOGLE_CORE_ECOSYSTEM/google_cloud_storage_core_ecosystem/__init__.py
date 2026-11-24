import json
from pathlib import Path
def _manifest():return json.loads((Path(__file__).with_name("ecosystem_manifest.json")).read_text(encoding="utf-8"))
