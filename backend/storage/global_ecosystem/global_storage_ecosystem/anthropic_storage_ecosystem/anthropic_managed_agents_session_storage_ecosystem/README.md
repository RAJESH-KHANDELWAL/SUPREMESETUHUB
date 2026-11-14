# Anthropic Managed Agents Session Storage Ecosystem

Models file resources and generated output artifacts associated with Anthropic Managed Agents sessions and environments.

## Scope

- Files uploaded for use as Managed Agents session resources.
- Files mounted into a supported session sandbox or referenced by file ID in supported session events.
- Output artifacts created by supported agent tools and exposed for download through documented file-content operations.
- Session/environment ownership, output metadata and lifecycle boundaries.

## Constraints

- This is session-oriented resource storage, not a general-purpose user drive or permanent backup destination.
- Availability depends on Managed Agents API access, account entitlement, workspace permissions and the provider's current session/file lifecycle.
- Do not assume that all uploaded files are downloadable; downloadability depends on how the file was created.
- Keep application tenant/user ownership mapping on the server and enforce authorization before exposing any file ID or output.
- API calls, authentication, session creation and endpoint schemas belong to the Anthropic API ecosystem, not this storage package.

## Status

`DOCUMENTED_API_NOT_CONNECTED`. This folder defines the storage boundary only; it does not create Managed Agents sessions or access provider files.
