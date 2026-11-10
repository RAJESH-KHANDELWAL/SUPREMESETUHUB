"""Explicit APP lifecycle state machine; never starts the host process."""
from threading import RLock
class InvalidLifecycleTransition(RuntimeError):pass
class AppLifecycle:
    _ALLOWED={"NEW":{"CONFIGURED","STOPPED"},"CONFIGURED":{"STARTING","STOPPED"},"STARTING":{"RUNNING","FAILED"},"RUNNING":{"STOPPING","FAILED"},"STOPPING":{"STOPPED","FAILED"},"STOPPED":{"CONFIGURED","STARTING"},"FAILED":{"STOPPED","CONFIGURED"}}
    def __init__(self,initial_state="NEW"):
        state=str(initial_state).strip().upper()
        if state not in self._ALLOWED:raise ValueError(f"Unknown APP lifecycle state: {state}")
        self._state=state;self._lock=RLock()
    @property
    def state(self):
        with self._lock:return self._state
    def transition(self,target):
        nxt=str(target or "").strip().upper()
        with self._lock:
            if nxt not in self._ALLOWED[self._state]:raise InvalidLifecycleTransition(f"APP lifecycle cannot move from {self._state} to {nxt}")
            self._state=nxt;return self._state
    def snapshot(self):return {"state":self.state,"allowed_next_states":sorted(self._ALLOWED[self.state])}
__all__=["AppLifecycle","InvalidLifecycleTransition"]
