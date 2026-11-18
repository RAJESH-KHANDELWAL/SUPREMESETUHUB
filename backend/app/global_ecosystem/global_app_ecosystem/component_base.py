"""Explicitly injected APP component adapter boundary."""
class AppComponentAdapter:
    def __init__(self,component_id,handler):
        self.component_id=str(component_id or "").strip()
        if not self.component_id:raise ValueError("component_id is required")
        if not callable(handler):raise TypeError("handler must be callable")
        self._handler=handler
    def invoke(self,*args,**kwargs):return self._handler(*args,**kwargs)
    def describe(self):return {"component_id":self.component_id,"configured":True,"execution":"EXPLICIT_INVOCATION_ONLY"}
__all__=["AppComponentAdapter"]
