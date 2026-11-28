# CLOUD SERVER

Cloud compute server taxonomy and provider-neutral cloud-instance operations. Concrete cloud actions require an explicitly configured provider adapter.

## Ownership

Owned by GLOBAL SERVER. This package must not import or duplicate API, CORE, ENGINE, DATABASE or STORAGE implementations.

## Safety

This package is a service-type namespace and contract boundary, not proof of a live service. Unconfigured actions must fail closed. Credentials must never be committed to source control.
