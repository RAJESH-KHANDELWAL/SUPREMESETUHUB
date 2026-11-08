# VPN SERVER

Secure tunnelling, VPN gateway lifecycle and server-side network configuration. This package defines the SERVER-owned service boundary; provider-specific execution must be injected and authorized.

## Ownership

Owned by GLOBAL SERVER. This package must not import or duplicate API, CORE, ENGINE, DATABASE or STORAGE implementations.

## Safety

This package is a service-type namespace and contract boundary, not proof of a live service. Unconfigured actions must fail closed. Credentials must never be committed to source control.
