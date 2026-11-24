# Salesforce API Ecosystem

Canonical provider-owned Salesforce ecosystem catalog and shared backend adapter.

- Provider ID: `salesforce`
- Service-family directories: 14
- Shared live-verification adapter: `backend/integrations/providers/salesforce.py`
- Verification route: `POST /api/v1/integrations/providers/salesforce/verify` (authenticated)
- Authentication mode implemented: Salesforce Connected App OAuth 2.0 client credentials
- Live connection: verified only when OAuth token exchange and an authenticated Salesforce REST request both succeed.

## One-time platform-owner setup

Set these server-side environment variables in the deployment secret manager:

- `SALESFORCE_CLIENT_ID` — Connected App / External Client App consumer key
- `SALESFORCE_CLIENT_SECRET` — consumer secret; never commit it
- `SALESFORCE_LOGIN_URL` — optional; defaults to `https://login.salesforce.com`; use `https://test.salesforce.com` for sandbox
- `SALESFORCE_API_VERSION` — optional; defaults to `v66.0`

In Salesforce:
1. Configure an OAuth Connected App / External Client App with the client credentials flow enabled.
2. Configure the run-as integration user according to Salesforce policy and grant only required API/object permissions.
3. Ensure API access is enabled for the org/user and the Connected App policy allows the intended client credentials flow.
4. Deploy the client ID/secret as server-side secrets and call the authenticated verification route.

The verifier obtains a token and calls `GET {instance_url}/services/data/{api_version}/limits`. It validates the returned HTTPS Salesforce instance host and never returns the access token.

## Service families

- Identity and OAuth
- REST API
- SOAP API
- Composite API
- Bulk API 2.0
- Platform Events and Pub/Sub
- Streaming API
- Metadata and Tooling APIs
- Apex APIs
- Files and Content
- Service Cloud
- Marketing Cloud
- Data Cloud
- Analytics and CRM Analytics

## Verification and security boundary

The current live verifier uses deployment-managed Connected App credentials and discards the access token after the request. It does **not** persist credentials or create per-customer OAuth connections. Each service family requires its own product entitlement, scopes/permissions, adapter operations, tests, and audit controls. A successful limits probe verifies REST API access only; it does not imply every Salesforce product is enabled.
