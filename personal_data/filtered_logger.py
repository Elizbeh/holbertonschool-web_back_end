#!/usr/bin/env python3
"""
Main file
"""
import re
from typing import List, Tuple

def filter_datum(fields: List[str], redaction: str, message:str, separator:str) -> str:
    pattern = r"password=([^;\s]+).*date_of_birth=([^;\s]+)"

    result = re.sub(pattern, f"password={redaction};date_of_birth={redaction}", message)
    return result
