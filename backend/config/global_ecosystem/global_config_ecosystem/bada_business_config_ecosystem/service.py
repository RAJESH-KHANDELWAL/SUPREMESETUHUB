"""Namespaced Bada Business configuration service."""

import os

from ..service import GlobalConfigService
from .models import BadaBusinessConfig
from .policies import validate_bada_business_values


def _parse_environment_value(key, value):
    if key in ("enabled", "require_approval"):
        normalized = str(value).strip().lower()
        if normalized in ("1", "true", "yes", "on"):
            return True
        if normalized in ("0", "false", "no", "off"):
            return False
        return value  # Invalid values are rejected by validation.
    if key == "request_timeout_seconds":
        try:
            return int(value)
        except (TypeError, ValueError):
            return value  # Invalid values are rejected by validation.
    return value


class BadaBusinessConfigService:
    def __init__(self, overrides=None, environ=None):
        defaults = dict(BadaBusinessConfig().as_dict())
        source = os.environ if environ is None else environ
        env_overrides = {
            key[len("BADA_BUSINESS_"):].lower(): _parse_environment_value(key[len("BADA_BUSINESS_"):].lower(), value)
            for key, value in source.items()
            if key.startswith("BADA_BUSINESS_")
        }
        merged_overrides = dict(overrides or {})
        merged_overrides.update(env_overrides)
        self._service = GlobalConfigService(
            defaults=defaults,
            overrides=merged_overrides,
            env_prefix="",
            environ={},
            namespace="bada_business",
        )

    def get(self, key, default=None):
        return self._service.get(key, default)

    def snapshot(self):
        base = self._service.snapshot()
        errors = tuple(base.errors) + validate_bada_business_values(self._service._values)
        return {
            "namespace": "bada_business",
            "values": dict(base.values),
            "source": "environment" if self._service._values != dict(BadaBusinessConfig().as_dict()) else base.source,
            "valid": not errors,
            "errors": list(errors),
        }

    def diagnostics(self):
        result = self._service.diagnostics()
        result.update({"namespace": "bada_business", "configuration_valid": self.snapshot()["valid"]})
        return result
