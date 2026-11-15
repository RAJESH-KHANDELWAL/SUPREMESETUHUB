# BADA BUSINESS CORE ECOSYSTEM

This package owns Bada Business domain rules and orchestration contracts.

## Programs domain

The `programs/` package provides program discovery, lookup, search and
enrollment-request validation. It reads program facts from the canonical
resource catalog at `backend/global_ecosystem/global_bada_business_ecosystem/platform_resources/`.

Provider facts are not copied into CORE. Registration submission, payment
processing, API transport, AI recommendations and live provider connectivity
are outside this package's current implementation.

## Public interface

```python
from backend.core.global_ecosystem.global_core_ecosystem.bada_business_core_ecosystem import (
    BadaBusinessProgramsManager,
)

manager = BadaBusinessProgramsManager()
print(manager.list_programs())
```

Current status: CORE programs domain scaffold implemented; live provider
registration and payment processing are disabled.
