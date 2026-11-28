# COHERE SHARED VALIDATION

Provider-wide, dependency-free request-shape validation helpers.

Capability-specific business rules remain in the corresponding capability package's `contracts.py`. Provider routing dispatches to those validators and rejects unsupported fields rather than silently ignoring them.

No provider SDK calls, network access, persistence or execution belong here.
