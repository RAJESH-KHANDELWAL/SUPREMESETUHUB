# COHERE SHARED SECURITY

Provider-wide security boundaries for Cohere CORE.

- Tenant and actor identity must come from the authenticated application layer.
- Provider credentials are represented only by opaque secret-manager references.
- Secret-like fields are rejected recursively in request metadata.
- Destructive, administrative, deployment and billing operations require explicit authorization and an approved API/ENGINE workflow.
- CORE does not exchange tokens, store secrets, authorize Cohere accounts or perform provider writes.

The PHP authentication-context contracts live in each capability package's `authentication/contract.php`.
