"""GitHub storage ecosystem foundation service; no live API calls."""
from dataclasses import asdict
from .ecosystem_models import EcosystemRecord

PACKAGE_ID = __package__.rsplit('.', 1)[-1]
ECOSYSTEM_ID = "GITHUB_STORAGE_ECOSYSTEM"


class EcosystemService:
    def __init__(self, *, config: dict | None = None):
        self.config = dict(config or {})
        self.enabled = self.config.get('enabled', True)

    def describe(self) -> dict:
        return {
            'ecosystem_id': ECOSYSTEM_ID,
            'package': PACKAGE_ID,
            'enabled': bool(self.enabled),
            'implementation_state': 'FOUNDATION_INITIALIZED',
            'connection_state': 'NOT_CONFIGURED',
            'external_connections_verified': False,
            'taxonomy_only': True,
            'capabilities': ['IDENTITY', 'CONFIGURATION', 'METADATA', 'HEALTH_CONTRACT', 'READ_ONLY_CATALOG'],
        }

    def health(self) -> dict:
        return {
            'success': True,
            'ecosystem_id': ECOSYSTEM_ID,
            'status': 'FOUNDATION_READY',
            'connection_state': 'NOT_CONFIGURED',
            'external_connections_verified': False,
            'storage_operations_enabled': False,
        }

    def serialize_record(self, record: EcosystemRecord) -> dict:
        return asdict(record)
