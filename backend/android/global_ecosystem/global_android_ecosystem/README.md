# Backend Global Android Ecosystem

This is the Backend-owned Android ecosystem entry point.

## Canonical structure

- Backend Android root: `backend/android/`
- Backend ecosystem: `backend/android/global_ecosystem/global_android_ecosystem/`
- Native Android Gradle project: `backend/android/global_ecosystem/global_android_ecosystem/native_android_app/`
- Frontend Android root: `frontend/android/`
- Frontend ecosystem: `frontend/android/global_ecosystem/global_android_ecosystem/`

Backend and Frontend Android are independent top-level namespaces. Android is not nested under Foundation or Infrastructure.

## Build boundary

The native Android Gradle project is owned by the Backend Global Android Ecosystem. Its Gradle configuration, manifest, Kotlin sources, resources, and ProGuard rules live under `native_android_app/`.

The obsolete `backend/mobile/android/` path is not used. The native build workflow targets the canonical Android project path. A configured build is not the same as a verified build: `build_verified` remains false until CI successfully produces and validates the release AAB.

## Backend endpoint configuration

The app does not hard-code a Render, Hostinger, or other unverified API host. Configure the actual deployed backend HTTPS URL at build time using either:

- Gradle property: `-PSUPREME_API_BASE_URL=https://your-verified-api-host`
- Environment variable: `SUPREME_API_BASE_URL=https://your-verified-api-host`

The value is intentionally blank by default. API calls fail closed until a verified HTTPS backend URL is supplied. Do not place API keys, passwords, database credentials, or other secrets in Gradle properties committed to the repository.

## Manager

`manager.py` exposes `GlobalAndroidEcosystemManager` and `get_manager()`. Its status reports structural readiness and native build configuration; it does not claim that a native build has passed.
