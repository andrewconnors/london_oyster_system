from sqlite3 import sqlite3, Connection

class Database:
    # Create a singleton class so we're not 
    # recreating the connection all the time.
    class __Database:
        connection: Connection = None
        database: str = None

        def __init__(self):
            self.database: str = "./locations.db"
            self.connection: Connection = sqlite3.connect(self.database)

    instance: __Database = None

    def __init__(self) -> None:
        if not self.instance:
            self.instance = self.__Database()

    def get_location(self, name: str):
        return self.instance.connection.cursor().execute(f"SELECT * FROM locations WHERE name={name}")