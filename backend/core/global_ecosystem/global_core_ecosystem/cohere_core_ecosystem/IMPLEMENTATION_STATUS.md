# Cohere CORE implementation status

## Implemented
- Shared CORE contracts, manager and validation service
- Capability registry for classify, command, embed, rerank and tokenize
- Request schema helpers, secret-field policy and operation guard
- PHP interoperability contract
- Unit tests for capability registration and validation

## Not enabled
- Live Cohere API calls
- Credential storage or authentication
- Provider-side operations, billing or model lifecycle writes
- Persistence and asynchronous execution

These require approved ENGINE/API/DATABASE integrations and verified provider credentials.
