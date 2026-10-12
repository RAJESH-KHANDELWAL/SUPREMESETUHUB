from backend.core.readiness import CoreReadinessService


class FakeDatabase:
    def __init__(self, healthy=True):
        self.healthy = healthy

    def health(self):
        return {
            "database": "SQLITE",
            "healthy": self.healthy,
            "connected": self.healthy,
        }


class FakeStorage:
    def __init__(self, registry="READY"):
        self.registry = registry

    def health(self):
        return {
            "health": "DEGRADED" if self.registry == "READY" else "UNHEALTHY",
            "database_registry": self.registry,
            "physical_storage": "NOT_CONFIGURED",
            "physical_storage_configured": False,
        }


def test_readiness_reports_core_database_and_metadata_storage_truthfully():
    result = CoreReadinessService(FakeDatabase(), FakeStorage()).snapshot()

    assert result["overall"] == "DEGRADED"
    assert result["components"]["core"]["status"] == "READY"
    assert result["components"]["database"]["status"] == "READY"
    assert result["components"]["storage"]["status"] == "METADATA_ONLY"
    assert result["components"]["storage"]["physical_storage"] == "NOT_CONFIGURED"
    assert result["components"]["storage"]["physical_storage_configured"] is False


def test_readiness_fails_closed_when_database_is_unavailable():
    result = CoreReadinessService(FakeDatabase(False), FakeStorage()).snapshot()

    assert result["overall"] == "UNHEALTHY"
    assert result["components"]["core"]["status"] == "DEGRADED"
    assert result["components"]["database"]["status"] == "UNAVAILABLE"


def test_readiness_fails_closed_when_storage_registry_is_unavailable():
    result = CoreReadinessService(FakeDatabase(), FakeStorage("UNAVAILABLE")).snapshot()

    assert result["overall"] == "UNHEALTHY"
    assert result["components"]["storage"]["status"] == "UNAVAILABLE"
