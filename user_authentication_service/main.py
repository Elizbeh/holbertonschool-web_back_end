#!/usr/bin/env python3
"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)
assert isinstance(user_1, User)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)
assert isinstance(user_2, User)
