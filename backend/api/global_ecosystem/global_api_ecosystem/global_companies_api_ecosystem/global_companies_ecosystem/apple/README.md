# APPLE API ECOSYSTEM

Canonical Apple company-specific API ecosystem package under GLOBAL COMPANIES API ECOSYSTEM.

- Parent provider catalog: `backend/api/global_api_ecosystem_catalog.py`
- Shared readiness adapter: `backend/integrations/providers/apple.py`
- Related existing platform package: Apple App Store under GLOBAL PLATFORMS API ECOSYSTEM.

Sign in with Apple and App Store Connect are separate feature/credential flows. The shared adapter checks for configuration presence only; it does not verify a signed token, user authorization or live Apple API access. Add feature-specific signature, permission and sandbox tests before marking any connection live.
