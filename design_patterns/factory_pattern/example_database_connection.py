from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "Connected to MySQL"

    def execute_query(self, query):
        return f"Executing MySQL query: {query}"

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return "Connected to PostgreSQL"

    def execute_query(self, query):
        return f"Executing PostgreSQL query: {query}"

def MongoDBConnection(DatabaseConnection):
    def connect(self):
        return "Connected to MongoDB"

    def execute_query(self, query):
        return f"Executing MongoDB query: {query}"

class DatabaseFactory:
    @staticmethod
    def get_connection(db_type, **config):
        connections = {
        'mysql': MySQLConnection,
        'postgresql': PostgreSQLConnection,
        'mongodb': MongoDBConnection
    }
        connection_class = connections.get(db_type.lower())
        if connection_class:
            return connection_class()
        raise ValueError(f"Unsupported database: {db_type}")

# Usage
db = DatabaseFactory.get_connection('mysql')
print(db.connect())
print(db.execute_query("SELECT * FROM users"))
