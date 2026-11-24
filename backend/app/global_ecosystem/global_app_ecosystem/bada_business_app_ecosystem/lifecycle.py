"""Explicit APP composition lifecycle; does not start servers or execute hooks."""
from __future__ import annotations
from enum import Enum

class AppState(str, Enum):
    CREATED = "created"
    REGISTERED = "registered"
    READY = "ready"
    STOPPED = "stopped"

class InvalidAppTransition(RuntimeError):
    pass

_ALLOWED = {
    AppState.CREATED: {AppState.REGISTERED, AppState.STOPPED},
    AppState.REGISTERED: {AppState.READY, AppState.STOPPED},
    AppState.READY: {AppState.STOPPED},
    AppState.STOPPED: set(),
}

class BadaBusinessAppLifecycle:
    def __init__(self) -> None:
        self._state = AppState.CREATED

    @property
    def state(self) -> AppState:
        return self._state

    def transition(self, target: AppState) -> AppState:
        if target not in _ALLOWED[self._state]:
            raise InvalidAppTransition(f"INVALID_APP_TRANSITION:{self._state.value}->{target.value}")
        self._state = target
        return self._state
