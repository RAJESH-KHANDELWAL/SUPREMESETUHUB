# SUPREME ECOSYSTEM

This package is the backend home for SUPREME's ecosystem modules. MAIN SUPREME owns the central security and permission model; this package implements ecosystem capabilities and provider connections.

## Planned capability boundaries

- Identity and account lifecycle: signup, signin, session validation, profile and account management use the central backend authentication and identity services.
- External providers: Google/Gmail and Microsoft Graph require explicit OAuth consent and provider-side app registration.
- WhatsApp: use the official WhatsApp Business Platform Cloud API. Incoming webhooks must be verified and idempotent; replies must follow WhatsApp's policy and messaging windows/templates.
- AI responder: only process inbound messages after webhook verification and user-consent/business configuration. Keep tokens, app secrets and model keys in deployment environment variables.
- Privacy: provider tokens and user conversations must not be written to source control or exposed by status/profile APIs.

The provider folders are integration scaffolding, not proof of a live connection. Complete provider OAuth/webhook handlers and run end-to-end tests before enabling automatic replies.
