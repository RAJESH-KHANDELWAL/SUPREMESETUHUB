# Global Infrastructure Models

Provider-neutral model vocabulary for infrastructure resources, relationships, providers and lifecycle metadata.

## Boundary
This package defines shared model contracts only. It does not replace:
- `backend/infrastructure/model.py` and its existing resource/relationship models
- `backend/database/` persistence models
- `backend/storage/` storage implementations
- provider-specific SDK objects or runtime adapters

Domain modules remain the owners of their operational models. This package supplies normalized descriptors and validation for cross-domain catalog exchange.

Status: model-contract foundation; no provider connectivity or persistence is implemented here.
