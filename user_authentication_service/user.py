#!/usr/bin/env python3
"""
User Model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    Create a SQLAlchemy model named
    User for a database table named users
    """

    __tablename__ = "users"

    id = Column("id",  Integer, primary_key=True)
    email = Column("email", String(250), nullable=None)
    hashed_password = Column("hashed_password", String(250), nullable=True)
    session_id = Column("session_id", String(250), nullable=True)
    reset_token = Column("reset_token", String(250), nullable=True)
