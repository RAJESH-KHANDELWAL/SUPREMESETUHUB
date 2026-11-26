# Android Application Ecosystem

Top-level home for native Android application code and Android-specific build assets.

## Structure
- `global_ecosystem/` contains the Android application ecosystem packages.

## Boundaries
- Native Android UI, app lifecycle, device integrations, and Android build configuration belong here.
- Backend services remain in `backend/`; browser/frontend assets remain in `frontend/`.
- Existing Android workflows and release configuration must remain intact during future migrations.
