class DatabaseManager:
    """
    CENTRAL DATABASE MANAGER

    Controls the complete application database layer.
    """

    NAME = "CENTRAL DATABASE"
    VERSION = "1.0.0"

    def __init__(self, database_service):
        self.database = database_service
        self.status = "READY"

    def initialize(self):
        self.database.initialize()
        self.status = "RUNNING"

        return {
            "name": self.NAME,
            "version": self.VERSION,
            "status": self.status,
        }

    def health(self):
        return {
            "name": self.NAME,
            "version": self.VERSION,
            "status": self.status,
        }

    def shutdown(self):
        self.status = "STOPPED"

        return {
            "name": self.NAME,
            "status": self.status,
        }
