#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import User, Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Creates User
        """

        user_added: User = User(email=email, hashed_password=hashed_password)

        self._session.add(user_added)
        self._session.commit()
        return user_added

    def find_user_by(self, **kwargs) -> User:
        """ Finds a user by given criteria.
        If no result found, Raises NoResultFound
        If wrong query arguments are passed,
        raises InvalideRequestError
        """
        try:
            response: User = self._session.query(
                    User).filter_by(**kwargs).first()
        except InvalidRequestError:
            raise InvalidRequestError
        if response is None:
            raise NoResultFound
        return response

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Updates the user with the given user_id
        using the provided keyword arguments.
        Raises ValueError for invalid user
        attribute arguments.
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError(f"Invalid user attribute: {key}")
            self._session.commit()
        except NoResultFound:
            raise ValueError(f"User with ID {user_id} not found")
        except InvalidRequestError as e:
            self.session.rollback()
            raise e
