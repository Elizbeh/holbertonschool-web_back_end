import re
from typing import List

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate sensitive information in a log message.

    Args:
    - fields (List[str]): A list of strings representing fields to be obfuscated.
    - redaction (str): A string representing the value by which the fields will be obfuscated.
    - message (str): A string representing the log line that needs processing.
    - separator (str): A string representing the character by which fields are separated in the log line.

    Returns:
    - str: The log message with specified fields obfuscated
    """
    # Create a regex pattern by joining escaped field names
    pattern = '|'.join(map(re.escape, fields))
    
    # Use re.sub to perform the substitution with a single regex
    return re.sub(
        r'({})([^{}]*(?:{}|$))'.format(pattern, re.escape(separator), re.escape(separator)), 
        r'\1={}{}'.format(redaction, separator), 
        message
    )
