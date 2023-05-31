#!/usr/bin/env python3
"""
Main file
"""
import logging
from logging import StreamHandler
from typing import Tuple


PII_FIELDS = ("name", "email", "phone",
              "ssn", "password")


def get_logger() -> logging.Logger:
    """
    A function that  returns a
    logging.Logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    stream_handler = StreamHandler()
    stream_handler.setLevel(logging.INFO)
    
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger