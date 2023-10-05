#!/usr/bin/env python3
"""
Write a function called filter_datum that
returns the log message obfuscated:
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
        Format the log record, redacting specified fields.

        Args:
        record (logging.LogRecord): The log record to be formatted.

        Returns:
        str: The formatted log message with redacted fields.
        """
        log_message = super(
                RedactingFormatter, self).format(record)
        for field in self.fields:
            log_message = filter_datum(
                    [field], self.REDACTION, log_message, self.SEPARATOR)
        return log_message


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate sensitive information in a log message.

    Args:
    - fields (List[str]): A list of strings
    representing fields to be obfuscated.
    - redaction (str): A string representing
    the value by which the fields will be obfuscated.
    - message (str): A string representing
    the log line that needs processing.
    - separator (str): A string representing
    the character by which fields are separated in the log line.

    Returns:
    - str: The log message with specified fields obfuscated
    """
    # Create a regex pattern by joining escaped field names
    pattern = '|'.join(map(re.escape, fields))

    # Use re.sub to perform the substitution with a single regex
    return re.sub(
            r'({})([^{}]*(?:{}|$))'.format(
                pattern, re.escape(separator), re.escape(separator)),
            r'\1={}{}'.format(redaction, separator), message
    )
