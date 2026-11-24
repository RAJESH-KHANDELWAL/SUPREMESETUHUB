# COHERE SHARED TESTING

Provider-wide unit and contract tests live in `tests/`. Capability-specific contract tests remain in each capability package's `tests/` directory.

Run from the repository root:

```bash
python -m unittest discover -s backend/core/global_ecosystem/global_core_ecosystem/cohere_core_ecosystem -t . -p "test_*.py"
```

Test execution must be confirmed in CI or a configured local environment before claiming verified readiness. Integration tests require separately configured API/ENGINE adapters and approved credentials.
