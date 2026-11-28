# Backend Global iOS Ecosystem

This namespace is the Backend-wide iOS entry point. It delegates native project ownership to the canonical iOS Foundation component; it does not create a second Xcode project.

## Canonical iOS project

- Project: `backend/mobile/ios`
- Native source package: `backend/mobile/ios/Sources/SupremeSetuHubIOS`
- Platform minimum: iOS 16+
- Build verification: not yet verified; native Xcode builds require a macOS/Xcode runner.

## Adapter

The Backend iOS ecosystem adapter exposes `GlobalIOSEcosystemManager` and `get_manager()`. It delegates to the canonical iOS Foundation manager and reports build verification separately from configuration status.

## Boundaries

- Backend iOS: ecosystem-level entry point and backend integration adapters.
- Backend Foundation iOS: canonical native project contract and shared foundation-owned project.
- Backend Infrastructure iOS: build/runtime, CI, deployment and operational integration.
- Frontend iOS: UI, navigation, presentation and client features.

No iOS build is considered verified until an Xcode build succeeds on a supported macOS runner.
