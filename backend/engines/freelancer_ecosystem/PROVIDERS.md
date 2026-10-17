# GLOBAL FREELANCER ECOSYSTEM — Provider Integrations

The provider registry is exposed through:

- `GET /api/v1/global-freelancer-ecosystem/providers`
- `GET /api/v1/global-freelancer-ecosystem/status`
- `GET /api/v1/global-freelancer-ecosystem/catalog`

## Provider inventory

| Provider | Intended role | Current implementation state |
|---|---|---|
| Google Drive | Owner-authorized files and sync | Readiness scaffold; OAuth flow and live API checks still required |
| Google Cloud Storage | App-managed object storage | Readiness scaffold; SDK, identity and bucket checks still required |
| Microsoft OneDrive / Graph | Owner-authorized files and sync | Readiness scaffold; Entra OAuth and Graph permissions still required |
| AWS S3 | App-managed object storage | Existing adapter inventory; credentials/role and live connection still unverified |
| Apple Sign in | Optional account identity | Readiness scaffold; Apple token validation and callback flow still required |

Apple Sign in is identity, not iCloud Drive file storage. The registry does not
claim that an external provider is connected. It reports missing environment
variable *names* only and never returns secret values or tokens.

## Environment variable names

- Google Drive: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`
- Google Cloud Storage: `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_STORAGE_BUCKET`
- Microsoft: `MICROSOFT_CLIENT_ID`, `MICROSOFT_TENANT_ID`
- AWS S3: `AWS_S3_BUCKET` (AWS SDK credential chain / IAM role may supply credentials)
- Apple Sign in: `APPLE_CLIENT_ID`, `APPLE_TEAM_ID`, `APPLE_KEY_ID`, `APPLE_PRIVATE_KEY`

Set secrets only in the deployment's secret manager/environment configuration,
never in source control. Environment configuration alone is not a successful
provider connection. Provider-specific OAuth callbacks, token storage/rotation,
least-privilege scopes, upload/download operations, and end-to-end health checks
must be implemented and tested before marking any provider connected.
