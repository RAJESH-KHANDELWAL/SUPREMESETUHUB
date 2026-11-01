# Global Business Ecosystem

Canonical public package boundary for the general-purpose Global Business Ecosystem.

## Scope
- General business discovery, classification, lifecycle and operating-model concepts.
- Business records and services that are not specific to the Bada Business product.
- India-first and global-ready domain boundaries.

## Existing implementation and compatibility

The established domain implementation remains in the existing modules:
- `backend/businesses/model.py`
- `backend/businesses/controller.py`
- `backend/businesses/service.py`
- `backend/businesses/connection.py`

This package exports `Business`, `BusinessController` and `BusinessService` as the canonical ecosystem import surface. The established modules remain the implementation source during incremental migration; logic is not copied.

Business records are stored in the dedicated `business_profiles` table through the shared `backend.database.service.DatabaseService`. The legacy generic `business` table is not repurposed or overwritten.

## Boundaries
- This package is distinct from Company, Corporate Group, Platform and Person/Freelancer records.
- Bada Business-specific functionality belongs under `backend/bada_business/global_ecosystem/global_bada_business_ecosystem/`.
- Existing API routes under `backend/api/businesses.py` remain available for backward compatibility.
- Do not duplicate registries or claim live provider/government integrations without verified sources.

The package is now connected to the existing Business domain, but API route relocation and further service decomposition remain incremental tasks requiring dedicated tests.
