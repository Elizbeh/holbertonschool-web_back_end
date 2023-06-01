#!/usr/bin/env python3
"""connect to Secure database
"""
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection

def get_db() -> MySQLConnectionQL:
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    conn = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )

    return conn
