"""Namespaced Bada Business configuration service."""

from ..service import GlobalConfigService
from .models import BadaBusinessConfig
from .policies import validate_bada_business_values


class BadaBusinessConfigService:
    def __init__(self, overrides=None, environ=None):
        defaults = dict(BadaBusinessConfig().as_dict())
        self._service = GlobalConfigService(
            defaults=defaults,
            overrides=overrides,
            env_prefix="BADA_BUSINESS_",
            environ=environ,
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
            "source": base.source,
            "valid": not errors,
            "errors": list(errors),
        }

    def diagnostics(self):
        result = self._service.diagnostics()
        result.update({"namespace": "bada_business", "configuration_valid": self.snapshot()["valid"]})
        return result
