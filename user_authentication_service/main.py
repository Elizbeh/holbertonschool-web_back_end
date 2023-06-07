from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print("DB.add_user returns a user object:", isinstance(user_1, User))

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print("DB.add_user returns a user object:", isinstance(user_2, User))

