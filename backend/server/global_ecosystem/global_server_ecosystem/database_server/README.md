# DATABASE SERVER

Database-hosting server inventory and infrastructure-level health metadata only. Database engines, schemas and persistence implementations remain owned by DATABASE.

## Ownership

Owned by GLOBAL SERVER. This package must not import or duplicate API, CORE, ENGINE, DATABASE or STORAGE implementations.

## Safety

This package is a service-type namespace and contract boundary, not proof of a live service. Unconfigured actions must fail closed. Credentials must never be committed to source control.
