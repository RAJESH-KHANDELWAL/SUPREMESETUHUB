# Global Model Ecosystem

Provider-neutral model contracts shared across infrastructure domains.

## Language layout

Each contract is maintained in both languages:
- `.py`: executable implementation used by the current Python backend.
- `.php`: PHP counterpart for PHP-based services and integrations.

The two implementations share the same field names and vocabulary. They are maintained as
parallel source files; this does not imply cross-language runtime loading or automatic
synchronization. Keep changes aligned and validate each language in its own runtime.

## Scope

- Resource identity and provider references (never credentials)
- Resource categories and types
- Resource relationships and topology
- Lifecycle, location, and capacity metadata
- Validation of the minimum resource record

Persistence remains owned by `backend/database/`; this package defines contracts only.
