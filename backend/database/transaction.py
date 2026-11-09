class DatabaseTransaction:
    """
    CENTRAL DATABASE TRANSACTION HELPER
    """

    def __init__(self, connection):
        self.connection = connection

    def begin(self):
        self.connection.execute("BEGIN")

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
