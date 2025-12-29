from abc import ABC, abstractmethod
from datetime import datetime


class Logger(ABC):
    @abstractmethod
    def log(self, message, level):
        pass


class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log(self, message, level):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"[{timestamp}] [{level}] Writing to {self.filename}: {message}"


class ConsoleLogger(Logger):
    def log(self, message, level):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"[{timestamp}] [{level}] Console: {message}"


class DatabaseLogger(Logger):
    def __init__(self, db_name):
        self.db_name = db_name

    def log(self, message, level):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"[{timestamp}] [{level}] DB({self.db_name}): {message}"


class LoggerFactory:
    @staticmethod
    def create_logger(logger_type, **kwargs):
        if logger_type == 'file':
            return FileLogger(kwargs.get('filename', 'app.log'))
        elif logger_type == 'console':
            return ConsoleLogger()
        elif logger_type == 'database':
            return DatabaseLogger(kwargs.get('db_name', 'logs'))
        else:
            raise ValueError(f"Unknown logger type: {logger_type}")


# Usage
file_logger = LoggerFactory.create_logger('file', filename='errors.log')
print(file_logger.log("Application started", "INFO"))

console_logger = LoggerFactory.create_logger('console')
print(console_logger.log("Debug message", "DEBUG"))
