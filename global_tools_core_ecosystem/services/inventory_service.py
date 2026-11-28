"""Unified read-only inventory snapshot."""
from ..orchestrator import GlobalToolsCoreOrchestrator
class ToolsInventoryService:
 def __init__(self): self.core=GlobalToolsCoreOrchestrator()
 def snapshot(self): return {"providers":self.core.providers(),"products":self.core.products(),"domains":self.core.domains(),"health":self.core.health()}
