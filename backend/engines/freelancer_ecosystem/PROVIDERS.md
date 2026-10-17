# GLOBAL FREELANCER ECOSYSTEM — Provider Integrations

Provider readiness and integration inventory are exposed through:

- `GET /api/v1/global-freelancer-ecosystem/providers`
- `GET /api/v1/global-freelancer-ecosystem/status`
- `GET /api/v1/global-freelancer-ecosystem/catalog`

## Provider implementation state

| Provider | Backend adapter capability | Still required before user-facing production connection |
|---|---|---|
| Google Drive | OAuth authorization URL and real Drive file-list API adapter | State/PKCE callback lifecycle, code exchange, encrypted refresh-token storage, upload/download tests |
| Google Cloud Storage | Provider inventory only | SDK adapter, workload identity/service-account configuration, bucket permissions and tests |
| Microsoft OneDrive / Graph | OAuth authorization URL and real Graph root-list API adapter | State/PKCE callback lifecycle, code exchange, encrypted refresh-token storage, upload/download tests |
| AWS S3 | Real S3 list-object operation via boto3 credential chain/IAM role | Configure IAM/bucket and run live permission, upload/download and deletion-safety tests |
| Apple Sign in | Apple identity-token verification against Apple's JWKS | Complete sign-in callback, nonce/state lifecycle, account linking and end-to-end tests |

Apple Sign in is identity, not iCloud Drive file storage. Google Drive and Microsoft
adapters use delegated access tokens provided by a separately authorized flow.
The adapters do not store access or refresh tokens.

## Environment variable names

- Google Drive: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`
- Google Cloud Storage: `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_STORAGE_BUCKET`
- Microsoft: `MICROSOFT_CLIENT_ID`, `MICROSOFT_TENANT_ID`
- AWS S3: `AWS_S3_BUCKET` and the AWS SDK credential chain or IAM role
- Apple Sign in: `APPLE_CLIENT_ID`

Set secrets only in the deployment secret manager/environment configuration,
never in source control. Environment configuration alone is not a successful
provider connection. Do not mark any provider connected until authorization,
least-privilege scopes, token lifecycle, upload/download operations where relevant,
and end-to-end health checks have passed.
