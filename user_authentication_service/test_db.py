#!/usr/bin/env python3
"""
Test file
"""
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User, Base
from db import DB


class DBTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test database and session
        self.engine = create_engine("sqlite:///test.db", echo=True)
        Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def tearDown(self):
        # Clean up the test database and session
        Base.metadata.drop_all(self.engine)
        self.session.close()

    def test_add_user(self):
        # Test adding a user to the database
        db = DB()
        email = "test@example.com"
        hashed_password = "hashedpwd"
        user = db.add_user(email, hashed_password)

        # Verify that the user object is returned
        self.assertIsInstance(user, User)

        # Verify that the user's email and hashed_password fields are correct
        self.assertEqual(user.email, email)
        self.assertEqual(user.hashed_password, hashed_password)


if __name__ == '__main__':
    unittest.main()

