# Global Infrastructure Models

Provider-neutral model vocabulary for infrastructure resources, relationships, providers and lifecycle metadata.

## Location and ownership

This is the canonical shared model-contract package:

`backend/models/infrastructure/global_infrastructure_models/`

It defines normalized descriptors and validation for cross-domain catalog exchange.

It does not replace:
- `backend/infrastructure/model.py` and its existing operational resource/relationship models
- `backend/database/` persistence models and database services
- `backend/storage/` storage implementations
- provider-specific SDK objects or runtime adapters

Domain modules remain owners of operational behavior. This package supplies shared contracts only.

Status: model-contract foundation; no provider connectivity or persistence is implemented here.
