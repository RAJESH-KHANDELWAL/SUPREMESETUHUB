from datetime import datetime, timezone


class FoundationAuditService:
    """
    MAIN BASE FOUNDATION audit service.

    Foundation-level events को record और retrieve करता है।

    यह application business logic या user activity
    का replacement नहीं है।
    """

    NAME = "FOUNDATION AUDIT SERVICE"

    def __init__(self):
        self._events = []

    def record(self, event, source="foundation", details=None):
        if not event:
            raise ValueError("Audit event is required.")

        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": event,
            "source": source,
            "details": details or {},
        }

        self._events.append(entry)

        return entry

    def list_events(self):
        return {
            "service": self.NAME,
            "count": len(self._events),
            "events": list(self._events),
        }

    def last_event(self):
        if not self._events:
            return None

        return self._events[-1]

    def clear(self):
        self._events.clear()

        return {
            "service": self.NAME,
            "status": "CLEARED",
        }
