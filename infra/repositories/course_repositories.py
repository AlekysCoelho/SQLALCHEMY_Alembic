from typing import List, Type

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import aliased

from infra.entities import Course
from infra.entities.registration import Registration
from infra.entities.student import Student

registration_alias = aliased(Registration)


class CourseRepository:
    def __init__(self, ConnectHandler) -> None:
        self.__ConnectHandler = ConnectHandler

    def select_all(self) -> List[Type[Course]]:
        """Searching all courses."""

        with self.__ConnectHandler() as db:
            try:
                data = db.session.query(Course).all()
                return data
            except Exception as exception:
                raise exception

    def insert(self, name: str, codigo: str, id_teacher: int) -> None | str:
        """Inserting a new course."""
        with self.__ConnectHandler() as db:
            try:
                data_insert = Course(name=name, codigo=codigo, id_teacher=id_teacher)
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, name: str, codigo: str, id_teacher: int) -> str:
        """Updating the name and id_teacher fields in the courses table."""

        with self.__ConnectHandler() as db:
            db.session.query(Course).filter(Course.codigo == codigo).update(
                {"name": name, "id_teacher": id_teacher}
            )
            db.session.commit()
            return "Update was successful"

    def delete(self, codigo: str) -> str:
        """Deleting a course."""

        with self.__ConnectHandler() as db:
            db.session.query(Course).filter(Course.codigo == codigo).delete()
            db.session.commit()
            return "Deleting was successful"
