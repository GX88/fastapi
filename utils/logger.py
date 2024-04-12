# Description: Create a logger
# Author:      faith
# Date:        2021/8/3 10:00
# Version:     1.0
import logging
import os
from logging.handlers import RotatingFileHandler


class LoggerFactory(object):
    def __init__(self, log_file: str, error_file: str):
        log_dir = os.path.join(os.getcwd(), 'log')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        self.log_file = os.path.join(log_dir, log_file)
        self.error_file = os.path.join(log_dir, error_file)

    def create_logger(self) -> logging.Logger:
        log_level = logging.DEBUG
        logger = logging.getLogger("fastapi")
        logger.setLevel(log_level)

        handlers = []

        # add file handler for normal logs
        file_handler = RotatingFileHandler(filename=self.log_file, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT,
                                           encoding='utf-8')
        file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        file_handler.setLevel(log_level)
        handlers.append(file_handler)

        # add file handler for error logs
        error_handler = RotatingFileHandler(filename=self.error_file, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT,
                                            encoding='utf-8')
        error_handler.setFormatter(logging.Formatter(ERROR_FORMAT))
        error_handler.setLevel(logging.ERROR)
        handlers.append(error_handler)

        # add stream handler for console output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
        console_handler.setLevel(log_level)
        handlers.append(console_handler)

        # add all handlers to logger
        for handler in handlers:
            logger.addHandler(handler)

        return logger


logs_file = "app.log"
errors_file = "app_error.log"

MAX_LOG_SIZE = 2 * 1024 * 1024  # 2 MB
BACKUP_COUNT = 5  # Number of backup logs

LOG_FORMAT = '%(levelname)s :    %(asctime)s - %(message)s'
ERROR_FORMAT = '%(levelname)s:   %(asctime)s - %(module)s.py:%(lineno)d行 - %(message)s'

logger_factory = LoggerFactory(logs_file, errors_file)
logger = logger_factory.create_logger()
