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
        self._engine = create_engine("sqlite:///a.db", echo=True)
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
            response: User = self._session.query(User).filter_by(**kwargs).first()
            return response
        except NoResultFound:
            self._session.rollback()
            raise NoResultFound("No user found")
        except InvalidRequestError as e:
            self._session.rollback()
            raise e
