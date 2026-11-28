# NSFWInfra WEBHOOKS API ECOSYSTEM

- Provider: NSFWInfra
- API route: `Dashboard webhook configuration`
- Scope: Receive job events and verify provider HMAC signatures before trusting callbacks. Verification not implemented.
- Configuration: `NSFWINFRA_API_KEY` (server-side only)
- Implementation status: Officially documented/cataloged; project adapter not yet implemented.

Official API documentation: https://nsfwinfra.com/docs

Adult-content safety: enforce 18+ eligibility, applicable law, consent, and safeguards against minors and non-consensual intimate imagery. Never expose provider credentials to the client.
