# iOS / iPhone / iPad readiness

This directory documents the native iOS delivery requirements. It is **not yet a complete native iOS application**.

## Why a native iOS build is not generated here

A production iOS application requires an Xcode project, Apple platform SDKs, signing/provisioning, device testing, privacy manifests where applicable, and an App Store Connect release workflow. Building and signing a distributable iOS app requires macOS with a supported version of Xcode and appropriate Apple developer credentials.

## Planned implementation sequence

1. Confirm the production HTTPS web/API URLs and authentication contract.
2. Decide whether a responsive website/PWA is sufficient or a native iOS client is required.
3. If native is required, create a maintained Xcode project (Swift/SwiftUI or an explicitly selected cross-platform framework).
4. Reuse the documented HTTPS API; never embed server secrets in the app.
5. Implement secure token storage using the platform Keychain, session expiry, sign-out and account deletion where applicable.
6. Add VoiceOver support, Dynamic Type, safe-area handling, localization and network failure states.
7. Test supported iOS/iPadOS versions and real devices.
8. Complete App Privacy details, privacy policy, permissions disclosures, signing and TestFlight checks.
9. Submit through App Store Connect and resolve review feedback.

## Current alternative

Until a native app is implemented, users may access the deployed responsive website through Safari on iPhone/iPad, provided the site is deployed over HTTPS and its flows are verified on real devices. This does not by itself guarantee App Store eligibility.
