# NSF Winfra Package Standard

Packages are responsibility-driven and must contain only necessary source, contract, documentation and tests. Reuse root contracts and catalog patterns rather than duplicating shared registries/managers.

- Preserve each existing ecosystem ID and folder path.
- Provide a package manager and `get_manager()` entry point.
- Expose metadata, capabilities and status only; never fake runtime execution/connectivity.
- Keep auth, secrets, persistence, API transport and execution in their owning layers.
- Avoid empty placeholders, duplicate catalogs, redundant models/contracts and speculative integrations.
- Test identity, capabilities, result structure and false-live status.
