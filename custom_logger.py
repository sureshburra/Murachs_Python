import logging
import logging.handlers
import sys

class CustomLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CustomLogger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        self.logger = logging.getLogger("AppLogger")
        self.logger.setLevel(logging.DEBUG)

        # Create handlers
        c_handler = logging.StreamHandler(sys.stdout)
        f_handler = logging.FileHandler('app.log')

        c_handler.setLevel(logging.DEBUG)
        f_handler.setLevel(logging.DEBUG)

        # Create formatters and add it to handlers
        format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        c_format = logging.Formatter(format_str)
        f_format = logging.Formatter(format_str)

        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        # Add handlers to the logger
        if not self.logger.handlers:
            self.logger.addHandler(c_handler)
            self.logger.addHandler(f_handler)

    def get_logger(self):
        return self.logger

    def add_email_handler(self, mailhost, fromaddr, toaddrs, subject, credentials=None):
        """
        Adds an SMTP handler to the logger.
        """
        email_handler = logging.handlers.SMTPHandler(
            mailhost=mailhost,
            fromaddr=fromaddr,
            toaddrs=toaddrs,
            subject=subject,
            credentials=credentials
        )
        email_handler.setLevel(logging.ERROR)
        format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        email_handler.setFormatter(logging.Formatter(format_str))
        self.logger.addHandler(email_handler)
