"""Offline tests for SERVER orchestration boundaries."""
from backend.server.global_ecosystem.global_server_ecosystem import GlobalServerEcosystemService
from backend.server.global_ecosystem.global_server_ecosystem.models import ServerOrchestrationRequest
class FakeCore:
    def validate_request(self,request): return {**request,"validated":True}
class FakeEngine:
    def dispatch(self,operation,payload): return {"operation":operation,"payload":payload}
def test_server_starts_without_external_connections():
    status=GlobalServerEcosystemService().health()
    assert status["domain"]=="SERVER" and not status["status"]["ready"]
    assert status["provider_connections"]=="NOT_ATTEMPTED"
def test_server_dispatches_through_injected_layers():
    service=GlobalServerEcosystemService()
    service.register_layer("CORE",FakeCore()); service.register_layer("ENGINE",FakeEngine())
    result=service.dispatch(ServerOrchestrationRequest("inspect",{"id":"node-1"}))
    assert result.success and result.result["payload"]["validated"]
def test_server_requires_core_and_engine():
    result=GlobalServerEcosystemService().dispatch(ServerOrchestrationRequest("inspect"))
    assert not result.success and result.status=="NOT_READY"
