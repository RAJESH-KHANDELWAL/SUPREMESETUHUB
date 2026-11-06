class DatabaseHealth:
    """
    DATABASE HEALTH CHECK
    """

    def __init__(self, database_service):
        self.database = database_service

    def check(self):
        try:
            self.database.initialize()

            return {
                "database": "CENTRAL DATABASE",
                "status": "HEALTHY",
            }

        except Exception as error:
            return {
                "database": "CENTRAL DATABASE",
                "status": "UNHEALTHY",
                "error": str(error),
            }
