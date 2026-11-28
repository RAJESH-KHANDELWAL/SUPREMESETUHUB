# NSFWInfra ASYNCHRONOUS JOBS API ECOSYSTEM

- Provider: NSFWInfra
- API route: `GET /v1/jobs/{job_id}`
- Scope: Poll queued generation jobs until completed, failed, or cancelled. End-to-end lifecycle not implemented.
- Configuration: `NSFWINFRA_API_KEY` (server-side only)
- Implementation status: Officially documented/cataloged; project adapter not yet implemented.

Official API documentation: https://nsfwinfra.com/docs

Adult-content safety: enforce 18+ eligibility, applicable law, consent, and safeguards against minors and non-consensual intimate imagery. Never expose provider credentials to the client.
