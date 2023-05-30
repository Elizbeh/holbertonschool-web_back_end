#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator:str) -> str:
    """
     Returns the log message
     obfuscated
    """
    pattern = f"({separator}|^)({'|'.join(fields)})=.*?({separator}|$)"
    return re.sub(pattern, fr"\1\2={redaction}\3", message)
