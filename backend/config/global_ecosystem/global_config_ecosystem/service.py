"""Core global configuration loading and access service."""

import os
from collections.abc import Mapping

from .models import ConfigSnapshot
from .validation import redact_values, validate_required


class GlobalConfigService:
    def __init__(self, defaults=None, overrides=None, env_prefix="APP_", environ=None, namespace="global"):
        self.namespace = namespace
        self.env_prefix = env_prefix
        self._environ = os.environ if environ is None else environ
        self._defaults = dict(defaults or {})
        self._overrides = dict(overrides or {})
        self._values = {}
        self._source = "defaults"
        self.reload()

    def reload(self):
        values = dict(self._defaults)
        if self._overrides:
            values.update(self._overrides)
            self._source = "explicit_overrides"
        env_values = {
            key[len(self.env_prefix):].lower(): value
            for key, value in self._environ.items()
            if self.env_prefix and key.startswith(self.env_prefix)
        }
        if env_values:
            values.update(env_values)
            self._source = "environment"
        self._values = values
        return self.snapshot()

    def get(self, key, default=None):
        return self._values.get(key, default)

    def snapshot(self, redact=True, required_keys=()):
        errors = validate_required(self._values, required_keys)
        values = redact_values(self._values) if redact else dict(self._values)
        return ConfigSnapshot(self.namespace, values, self._source, not errors, errors)

    def diagnostics(self):
        snapshot = self.snapshot(redact=True)
        return {"namespace": self.namespace, "source": self._source, "valid": snapshot.valid, "keys_loaded": len(self._values), "secrets_exposed": False}
