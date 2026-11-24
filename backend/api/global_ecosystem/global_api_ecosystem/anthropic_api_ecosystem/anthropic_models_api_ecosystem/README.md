# Models API

Anthropic API family catalog for SUPREMESETUHUB.

## Scope
Model discovery and metadata such as model identifiers and capability information; never hard-code assumptions about model availability.

## Integration rules
- Implement through the shared backend integration layer; do not create a second provider credential store.
- Keep provider secrets server-side and redact them from logs and responses.
- Apply authentication, workspace permissions, input validation, rate limits, retries, timeouts and audit logging appropriate to this API family.
- Treat provider errors and partial responses explicitly; never report success without a verified provider response.

## Status
This folder is a **catalog/documentation scaffold**. It does not claim that this API family has a working live adapter or has passed integration tests.
