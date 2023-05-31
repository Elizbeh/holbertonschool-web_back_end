#!/usr/bin/env python3
"""
 Regex-ing
"""

import re
from typing import List


def filter_datum(
  fields: list[str], redaction: str, message: str, separator: str
  ) -> str:
    """A function that returns the log
gi    message obfuscated:
    """
    regex = re.compile(f'({"|".join(fields)})=[^{separator}]+(?={separator})')
    return regex.sub(f'\\1={redaction}', message)