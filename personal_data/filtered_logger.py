#!/usr/bin/env python3
"""
Write a function called filter_datum that
returns the log message obfuscated:
"""

import logging
import csv
import re


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: tuple):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        log_message = super(RedactingFormatter, self).format(record)

        for field in self.fields:
            log_message = self.filter_datum(
                    [field], self.REDACTION, log_message, self.SEPARATOR)

        return log_message

    @staticmethod
    def filter_datum(fields, redaction, message, separator):
        pattern = '|'.join(map(re.escape, fields))
        return re.sub(
            r'({})(.*?)(?={}|\Z)'.format(pattern, re.escape(separator)),
            r'\1={}{}'.format(redaction, separator),
            message
        )

    def get_logger(self) -> logging.Logger:

        logger = logging.getLogger("user_data")
        logger.setLevel(logging.INFO)
        logger.propagate = False

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        redacting_formatter = RedactingFormatter(PII_FIELDS)
        stream_handler.setFormatter(redacting_formatter)

        logger.addHandler(stream_handler)

        return logger
