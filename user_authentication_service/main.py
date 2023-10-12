#!/usr/bin/env python3
"""
"""
# main.py
from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
assert isinstance(user_1, User)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
assert isinstance(user_2, User)


assert user_2.email == "test1@test.com"
assert user_2.hashed_password == "SuperHashedPwd1"

print("All tests passed.")

