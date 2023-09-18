from pathlib import Path
from typing import Type

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

file = Path(__file__)
course_database_path = file.parent.parent.parent / "database" / "enterprise.db"


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = f"sqlite:////{course_database_path}"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self) -> Type[Engine]:
        """Private method for Engine connection."""
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self) -> Type[Engine]:
        """Method to return the Engine connection."""
        return self.__engine

    def __enter__(self) -> Type[Session]:
        """Magic method used in context managers. Starting session."""
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        self.session.expire_on_commit = False
        return self

    def __exit__(self, *exc) -> None:
        """Magic method used in context managers. Make sure the session gets closed"""
        self.session.expunge_all()
        self.session.close()
