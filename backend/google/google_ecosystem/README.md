# Google Ecosystem

The Google domain directory is `backend/google/`; this package is
`backend/google/google_ecosystem/`.

## Google Cloud read-only connection check

An authenticated administrator can call:

`GET /api/v1/google-ecosystem/cloud/connection`

The endpoint uses Google Application Default Credentials (ADC) and Google Cloud
Resource Manager to read the configured project's metadata. It does not create,
update, or delete resources.

Configure the environment outside the repository:

- `GOOGLE_CLOUD_PROJECT`: target Google Cloud project ID.
- ADC credentials: prefer Workload Identity Federation on supported cloud
  platforms. If using a service account, keep its key outside source control and
  grant only the permissions needed to read project metadata (for example,
  `resourcemanager.projects.get`).

Enable the Cloud Resource Manager API for the project if required. The endpoint
returns explicit states such as `AUTHENTICATION_NOT_CONFIGURED`,
`PROJECT_NOT_CONFIGURED`, `PERMISSION_DENIED`, and
`CONNECTED_READ_ONLY`. A successful check only verifies read access to project
metadata; it does not mean every Google API or subsystem is connected.

The route is protected by the existing admin dependency. No credentials or
access tokens are returned in the response.

## Subsystem scope

CORE, ENGINE, DATABASE, STORAGE, DNS, VPS, VPN, and CLOUD catalog folders remain
separate. Only the Cloud read-only connection check is implemented in this step;
other subsystem integrations are deferred.
