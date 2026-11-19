import json
from pathlib import Path

from ..ecosystem_config import ECOSYSTEM_ID, LIVE_CONNECTION_ENABLED, PROVIDER_ID, PROVIDER_NAME
from ..schemas.provider_schema import validate


def test_provider_identity_and_catalog_only_boundary():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "ecosystem_manifest.json").read_text(encoding="utf-8"))
    assert manifest["provider_id"] == PROVIDER_ID
    assert manifest["ecosystem_id"] == ECOSYSTEM_ID
    assert manifest["provider_name"] == PROVIDER_NAME
    assert manifest["live_connection"] is False
    assert LIVE_CONNECTION_ENABLED is False
    assert validate(manifest)


def test_provider_service_never_claims_live_connection():
    from ..service import readiness
    assert readiness()["live_connection"] is False
