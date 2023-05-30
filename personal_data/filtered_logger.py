#!/usr/bin/env python3
"""
Regex-ing
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
     Returns the log message
     obfuscated
    """
    pattern = f"({separator}|^)({'|'.join(fields)})=.*?({separator}|$)"
    return re.sub(pattern, fr"\1\2={redaction}\3", message)
