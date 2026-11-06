# Google API Ecosystem

Shared authentication helpers live in `google_api_runtime.py`; each API family exposes a `service.py` client factory. Gmail retains its dedicated OAuth send adapter.

**Status:** client factories are implemented; live connectivity remains unverified until credentials, API enablement, permissions, and integration tests succeed. See [deployment guide](README.md).
