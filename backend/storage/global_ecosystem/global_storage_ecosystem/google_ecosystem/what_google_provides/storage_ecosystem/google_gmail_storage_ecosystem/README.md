# GOOGLE GMAIL STORAGE ECOSYSTEM

Storage-domain catalog for Gmail mailbox data and user-authorized exports.

## Scope
- Gmail messages and conversation metadata
- Labels, folders/views, and mailbox organization metadata
- User-authorized message attachments
- Trash, spam, archive, and retention-state metadata
- Mailbox export and backup workflows, where supported by Google

## Ownership boundary
This package describes storage objects and lifecycle metadata only. Gmail API access, OAuth scopes, message retrieval, sending, and provider operations belong in the Google API/integration layer.

## Safety and readiness
No live Gmail account is connected by this scaffold. Do not store OAuth tokens, message bodies, attachments, or personal data in source control. Enable an integration only after consent, least-privilege scopes, authorization, health checks, and end-to-end tests.
