from typing import List, Type

from sqlalchemy.exc import NoResultFound

from infra.entities import Teacher


class TeacherRepository:
    def __init__(self, ConnectHandler) -> None:
        self.__ConnectHandler = ConnectHandler

    def select_all(self) -> List:
        """Searching all teachers."""

        with self.__ConnectHandler() as db:
            try:
                data = db.session.query(Teacher).all()
                return data
            except Exception as exception:
                raise exception

    def selecting_through_a_course(self, course_name: str) -> Type[Teacher] | str:
        """Seeking teacher. Selecting through a course"""

        with self.__ConnectHandler() as db:
            try:
                data = (
                    db.session.query(Teacher)
                    .filter(Teacher.courses.any(name=course_name))
                    .one()
                )
                return data
            except NoResultFound:
                return "No results found"
            except Exception as exception:
                db.session.rollback()
                raise exception

    def insert(self, name: str, cpf: str, fullname: str = "") -> None | str:
        """Inserting a new teacher."""

        with self.__ConnectHandler() as db:
            try:
                data = Teacher(name=name, fullname=fullname, cpf=cpf)
                db.session.add(data)
                db.session.commit()
                return data
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, name: str, cpf: str, fullname: str = "") -> str:
        """Updating the name and fullname fields in the teachers table."""

        with self.__ConnectHandler() as db:
            db.session.query(Teacher).filter(Teacher.cpf == cpf).update(
                {"name": name, "fullname": fullname}
            )
            db.session.commit()
            return "Update was successful"

    def delete(self, cpf: str) -> str:
        """Deleting a teacher."""

        with self.__ConnectHandler() as db:
            db.session.query(Teacher).filter(Teacher.cpf == cpf).delete()
            db.session.commit()
            return "Deleting was successful"
