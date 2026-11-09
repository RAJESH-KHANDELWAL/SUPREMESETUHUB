# Domain and technical ownership contracts

## Business-domain ownership
This package defines cultural-business concepts, taxonomy, participant journeys, consent and rights requirements, commercial policy expectations and business workflow requirements.

## Technical ownership
- API: endpoints, transport contracts, boundary validation and versioning.
- CORE: canonical entities, invariants and business rules.
- ENGINE: orchestration and workflow coordination; never absorbs API or CORE.
- AI: model interactions, AI safety and evaluation.
- DATABASE: persistence models, migrations and queries.
- STORAGE: object/file storage and retention implementation.
- AUTHENTICATION / AUTHORIZATION: identity and access decisions.
- PAYMENT: payment-provider integrations, transactions and reconciliation.
- APP: user-facing applications and presentation.

## Contract rules
1. Exchange data through documented, versioned contracts.
2. Never duplicate another layer's implementation here.
3. Never commit API keys, tokens, passwords or private participant data.
4. Mark integrations planned until credentials, contracts, tests and approvals exist.
5. Keep human approval for cultural rights, consent, partner verification and sensitive publication.
