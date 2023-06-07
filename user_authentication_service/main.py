from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print("DB.add_user returns a user object:", isinstance(user_1, User) and user_1.email == "test@test.com" and user_1.hashed_password == "SuperHashedPwd")

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print("DB.add_user returns a user object:", isinstance(user_2, User) and user_2.email == "test1@test.com" and user_2.hashed_password == "SuperHashedPwd1")

