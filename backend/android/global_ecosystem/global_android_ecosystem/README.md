# Backend Global Android Ecosystem

This is the Backend-owned Android ecosystem entry point.

## Canonical structure

- Backend Android root: `backend/android/`
- Backend ecosystem: `backend/android/global_ecosystem/global_android_ecosystem/`
- Frontend Android root: `frontend/android/`
- Frontend ecosystem: `frontend/android/global_ecosystem/global_android_ecosystem/`

Backend and Frontend Android are independent top-level namespaces. Android is not nested under Foundation or Infrastructure.

## Build boundary

The deleted `backend/mobile/android/` project is not part of this setup. No Gradle project, APK, or AAB build is claimed. Native Android build configuration must be added under the approved Android-owned structure before a native build workflow is enabled.

## Manager

`manager.py` exposes `GlobalAndroidEcosystemManager` and `get_manager()`. Its status reports structural readiness only; it does not claim runtime or native-build verification.
