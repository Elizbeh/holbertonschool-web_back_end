#!/usr/bin/env python3
"""
Log formatter
"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
         method to filter values in incoming log records using filter_datum
        """
        log_message = super().format(record)
        return self.__class__.filter_datum(
            self.fields, self.REDACTION, log_message, self.SEPARATOR
        )


    @staticmethod
    def filter_datum(fields, redaction, message, separator):
        """
        """
        pattern = re.compile(f'({"|".join(fields)})=[^;]+')
        return pattern.sub(f'\\1={redaction}', message)
    