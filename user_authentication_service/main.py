#!/usr/bin/env python3
"""
Main file
"""

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User

my_db = DB()

user = my_db.add_user("test@test.com", "PwdHashed")
print(user.id)

try:
    find_user = my_db.find_user_by(email="test@test.com")
    if find_user is not None:
        print(find_user.id)
    else:
        print("User not found")
except NoResultFound:
    print("User not found")

try:
    find_user = my_db.find_user_by(email="test2@test.com")
    if find_user is not None:
        print(find_user.id)
    else:
        print("User not found")
except NoResultFound:
    print("User not found")

try:
    find_user = my_db.find_user_by(no_email="test@test.com")
    if find_user is not None:
        print(find_user.id)
    else:
        print("User not found")
except InvalidRequestError as e:
    print(e)

