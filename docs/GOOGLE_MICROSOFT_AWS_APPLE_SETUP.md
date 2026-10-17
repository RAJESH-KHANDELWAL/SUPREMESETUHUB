# SUPREMESETUHUB — Google, Microsoft, AWS and Apple setup

## What this setup delivers

The provider registry reports whether server-side configuration is present. It deliberately does **not** claim an account is connected merely because environment variables exist. The current adapters are readiness/configuration scaffolding; OAuth consent, token persistence, provider API calls, permission enforcement, and live verification still need feature-specific implementation and tests.

## Required accounts and setup

### Google / Google Cloud
1. Choose the Google Cloud project and confirm billing only for services that need it.
2. Configure the OAuth consent screen and publish/test-user settings appropriate to the audience.
3. Create a Web OAuth client; add the exact HTTPS callback URL used by the deployed app.
4. Set `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GOOGLE_REDIRECT_URI` in the hosting secret store.
5. Request only the scopes needed for the specific feature. Do not ask for broad Gmail/Drive access by default.
6. Google Cloud workloads should prefer workload identity/service-account access with least privilege over user OAuth when appropriate.

### Microsoft 365 / Entra ID / Azure
1. Register an application in Microsoft Entra ID.
2. Select supported account types and configure the exact HTTPS redirect URI.
3. Add only required Microsoft Graph delegated/application permissions; obtain admin consent when required.
4. Set `MICROSOFT_CLIENT_ID`, `MICROSOFT_CLIENT_SECRET`, `MICROSOFT_TENANT_ID`, and `MICROSOFT_REDIRECT_URI` in the hosting secret store. Use `common` only if the app is designed for multiple account types.
5. Azure resource access should use managed identity where supported.

### AWS
1. Select the AWS account, region, services and monthly budget first.
2. Prefer an attached IAM role or web identity federation. Use a dedicated least-privilege policy.
3. Set `AWS_REGION` and configure the platform's supported role/web-identity mechanism. If long-lived access keys are unavoidable, keep them in a secret store and rotate them.
4. Never use root-account credentials in the application. Start with a non-destructive STS identity check before any S3 read/write test.

### Apple
1. For Sign in with Apple, configure the Apple Developer identifier/Services ID, Team ID, Key ID, private key, and exact HTTPS return URL.
2. For App Store Connect, create a role-limited API key and use its issuer ID, key ID, and private key.
3. These are distinct features and credentials. Set only the variables for the feature actually being enabled.
4. Keep private keys in a hosting secret manager; do not commit them to Git or put them in browser code. Apple developer membership and platform restrictions may apply.

## Environment variable names

- Google: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI`
- Microsoft: `MICROSOFT_CLIENT_ID`, `MICROSOFT_CLIENT_SECRET`, `MICROSOFT_TENANT_ID`, `MICROSOFT_REDIRECT_URI`
- AWS: `AWS_REGION` plus a role/web-identity configuration, or `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` only when required
- Apple Sign in: `APPLE_SERVICES_ID`, `APPLE_TEAM_ID`, `APPLE_KEY_ID`, `APPLE_PRIVATE_KEY`, `APPLE_REDIRECT_URI`
- App Store Connect: `APPLE_ISSUER_ID`, `APPLE_APP_STORE_KEY_ID`, `APPLE_APP_STORE_PRIVATE_KEY`

Use `backend/.env.example` as a names-only reference. It contains no working credentials. Put actual values in the deployment's encrypted environment/secret settings, not in source files, commits, issues, or chat.

## Permanent operation: realistic release gates

“Lifetime permanent” cannot be guaranteed by source code: provider policies, OAuth consent, billing, API availability, domains, certificates, keys, and account status can change. The durable implementation target is maintainable code plus renewable credentials, least privilege, monitoring, backups, and tested recovery.

Before production activation:
- verify existing database and upload persistence and restore from a tested backup;
- implement encrypted, durable token storage and token revocation/rotation;
- implement provider-specific OAuth/API operations and user consent;
- add integration tests against test accounts and least-privilege resources;
- run non-destructive live checks and confirm authorization boundaries;
- record cost, quota, rate limits, retention, and recovery procedures.

No production resource, account, paid service, credential, database migration, or cutover is created by this code change. Existing hosting/domains remain untouched.
