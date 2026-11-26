# Backend Global Android Ecosystem

This namespace is the Backend-wide Android entry point. It delegates project ownership and configuration to the canonical Android Foundation component; it does not create a second Android Gradle project.

## Canonical Android project

- Project: `backend/mobile/android`
- App module: `backend/mobile/android/app`
- Package / application ID: `com.mainbasefoundation.android`
- Namespace: `com.mainbasefoundation.android`
- Compile SDK / Target SDK: `36`
- Minimum SDK: `26`
- Java compatibility: `17`
- Release task: `:app:bundleRelease`
- Release artifact: `backend/mobile/android/app/build/outputs/bundle/release/app-release.aab`

## Adapter

- `manager.py` exposes `GlobalAndroidEcosystemManager` and `get_manager()`.
- The manager delegates to `AndroidFoundationManager`.
- The adapter reports configuration status separately from build verification.

## Boundaries

- Backend Android namespace: ecosystem-level entry point and integration adapters.
- Backend Foundation Android: canonical app contract and shared foundation-owned project.
- Backend Infrastructure Android: build/runtime, CI, deployment and operational integration.
- Frontend Android: UI/navigation/presentation/client features.

No Android release build is considered verified until CI or a local Gradle build produces and validates the AAB.
