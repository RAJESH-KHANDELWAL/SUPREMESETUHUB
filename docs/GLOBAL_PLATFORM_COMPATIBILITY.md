# SUPREMESETUHUB — Global Platform Compatibility Standard

## Purpose

Keep SUPREMESETUHUB / MAIN BASE FOUNDATION maintainable across common browsers, mobile devices, deployment environments, and future native app stores. GitHub is the source-control and automation center; it is not itself the production web/API host.

## Current capability status

| Target | Repository evidence | Status |
|---|---|---|
| Web app / website | HTML, CSS, JavaScript under `frontend/`; FastAPI backend | Exists; browser and accessibility testing still required |
| Android app | Gradle project under `mobile/android/`; release AAB workflow | Project exists; each release build and device flow must pass |
| iPhone / iPad web use | Website can be tested in Safari once deployed over HTTPS | Web compatibility must be verified on real iOS devices |
| Native iOS app / App Store | No complete native Xcode project is established by this standard | Not yet implemented; requires a macOS/Xcode build, signing, privacy declarations and App Store Connect submission |
| Desktop | Modern desktop browsers can use the web app | Browser matrix and responsive layout testing required |
| Other operating systems | Browser-based access is the broadest shared route | Not a guarantee of compatibility with every OS, device, application or network |

## Global compatibility rules

1. **One API contract:** Keep business logic and authorization in the backend API. Web, Android and any future iOS client must use documented, versioned HTTPS endpoints rather than duplicate security rules.
2. **Responsive web:** Support narrow phones, tablets and desktop widths; avoid fixed-width layouts and horizontal overflow.
3. **Browser baseline:** Test current stable Chrome, Edge, Firefox and Safari. Test iOS Safari separately; Android WebView is not identical to desktop Chrome.
4. **Accessibility:** Target WCAG 2.2 AA for key flows: keyboard operation, visible focus, labels, contrast, zoom/reflow, and accessible error messages.
5. **Internationalization:** Use UTF-8, Unicode-safe storage, locale-aware dates/numbers, explicit time zones and currency codes. Do not assume every user is in India or uses INR/English.
6. **Network resilience:** Handle slow, offline, interrupted and retrying connections; show useful loading and error states. Do not assume a third-party provider is always available.
7. **Security:** HTTPS in production; secrets only in deployment secret stores; server-side authorization on every private endpoint; rate limits on authentication and public abuse-prone endpoints; verify webhook signatures; avoid logging tokens or personal data.
8. **Data durability:** Use a persistent managed database or configured persistent disk in production, backups and restore tests. Local SQLite files inside ephemeral hosting are not a durable production database.
9. **Compatibility without unsafe fallbacks:** Feature-detect browser APIs, degrade gracefully, and never bypass certificate validation, store policy, device security or provider authorization to make something “work everywhere.”
10. **Automated quality gates:** Run backend tests and Android release builds in GitHub Actions for pull requests before merging. Test real deployed flows separately; a successful compile does not prove production readiness.

## Release gates

A release should not be labelled production-ready until the following evidence exists:

- Backend test suite passes in a clean CI environment.
- Android release AAB builds and is tested on representative physical/emulated devices.
- Web smoke tests pass on Chrome, Edge, Firefox, Safari and mobile viewports.
- Authentication, authorization, account recovery, API validation and cross-user data isolation are tested.
- Deployment health check, HTTPS certificate, database persistence, backup and restore are verified.
- Provider integrations are tested using authorized credentials and provider-approved sandbox/production setup.
- Privacy policy, terms, data retention/deletion, consent where required, and support contact are published.
- Google Play review requirements are met for the specific release.
- A native iOS build is produced and tested on macOS/Xcode, signed with the appropriate Apple developer credentials, and submitted through App Store Connect if iOS distribution is intended.

## Important limits

No repository setting can make an app “allowed everywhere” or guarantee Google Play / Apple App Store approval. Availability depends on local law, store rules, permissions, supported hardware/OS versions, third-party API access, certificates, developer accounts, privacy disclosures and review decisions. A web app can provide broad browser access, but it is not the same as a signed native iOS app.

## Suggested verification commands

From the repository root:

```bash
python -m pip install -r backend/requirements.txt
python -m pytest backend/tests -v
```

Build the Android release bundle:

```bash
cd mobile/android
gradle :app:bundleRelease --no-daemon
```

The Android command requires a compatible JDK, Android SDK and Gradle environment. Use the GitHub Actions workflow for a reproducible hosted build.

## Secrets and deployment

- Copy only placeholder values from `backend/.env.example`; never commit real credentials.
- Configure production values in the hosting provider's secret/environment settings.
- Configure exactly one Render Blueprint for a given service unless separate services are intentional.
- Keep the production API URL in a single documented configuration point for each client.
- Rotate any credential that was ever committed to Git history; deleting a file does not revoke an exposed secret.
