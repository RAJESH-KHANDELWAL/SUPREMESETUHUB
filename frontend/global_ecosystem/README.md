# Frontend Global Ecosystem

Frontend-owned ecosystem modules for the SUPREMESETUHUB user experience.

## Structure
- `global_android_ecosystem/` — frontend integration contracts and user-experience surfaces for Android capabilities.
- `global_foundation_ecosystem/` — shared frontend design, application, and interaction foundations.
- `global_infrastructure_ecosystem/` — frontend-facing infrastructure integration surfaces such as configuration and client adapters.

## Boundaries
- UI and client-side behavior belong here; backend business rules and persistence remain in backend-owned modules.
- Reuse existing `frontend/foundation` and `frontend/infrastructure` code. Do not duplicate or move it without import, route, asset, and build validation.
