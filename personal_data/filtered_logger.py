#!/usr/bin/env python3
"""
Main file
"""
import logging
from logging import StreamHandler
from typing import Tuple


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Custom log formatter that
    redacts PII fields in log messages.
    """
    def __init__(self, pii_fields):
        super().__init__()
        self.pii_fields = pii_fields

    def format(self, record):
        """
        Formats the log record, redacting
        any PII fields in the log message.
        """
        for field in self.pii_fields:
            if field in record.msg:
                record.msg = record.msg.replace(record.msg, "*" * 8)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    A function that returns a logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = StreamHandler
    stream_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
