#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    regex = r"password=([^;\s]+).*date_of_birth=([^;\s]+)"

    return re.sub(regex, f"password={redaction};date_of_birth={redaction}", message)
