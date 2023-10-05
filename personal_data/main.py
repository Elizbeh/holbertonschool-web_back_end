#!/usr/bin/env python3
"""
Main file
"""

import logging
from filtered_logger import RedactingFormatter, PII_FIELDS

# Create an instance of RedactingFormatter with PII_FIELDS
formatter = RedactingFormatter(fields=PII_FIELDS)

# Create a logger using the formatter
logger = formatter.get_logger()

# Print the type of the logger and the length of PII_FIELDS
print(type(logger))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))
