# Product Ecosystem Standard

1. Preserve existing child package names and paths; classify each package under one canonical domain.
2. Add only files required by actual product responsibilities; avoid empty placeholder trees and duplicated shared managers.
3. Keep provider clients, OAuth and transport in the API layer.
4. Keep persistence, records, retention and backups in Storage/Database.
5. Keep queues, retries, scheduling and execution in Engine/Runtime.
6. Keep consent interfaces and user workflows in Application/Frontend.
7. Keep Core limited to registry, taxonomy, capability metadata, policy, lifecycle and readiness.
8. Adult-media providers are age-restricted and consent/rights gated; registration is not authorization to access or publish content.
9. Payment providers and ad networks are references only; do not imply approval, payout eligibility or live integration.
10. Healthcare/counselling listings are not proof of credentials; verify professional licensing before clinical referrals.
11. Use explicit CATALOG_ONLY, SCAFFOLD or VERIFIED states. Never claim connection without authenticated smoke tests.
12. Never store credentials, identity documents, intimate media or health records in Core catalog files.
