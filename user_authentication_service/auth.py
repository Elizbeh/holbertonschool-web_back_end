#!/usr/bin/env python3
""" A _hash_password method that takes in
a password string arguments and returns bytes.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes the input password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
