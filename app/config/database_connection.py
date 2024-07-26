import sqlite3


class DatabaseConnection:

    def __init__(self):
        self.db_connection = sqlite3.connect(':memory:')
        self.db_connection.row_factory = sqlite3.Row

    def __del__(self):
        self.db_connection.close()
