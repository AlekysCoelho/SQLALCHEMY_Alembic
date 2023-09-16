from typing import List, Tuple, Type

from infra.entities.course import Course
from infra.entities.registration import Registration
from infra.entities.student import Student


class StudentRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler

    def select_all(self) -> List[Type[Student]]:
        """Searching all students."""

        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Student).all()
                return data
            except Exception as exception:
                raise exception

    def select_all_courses(self, student_cpf: str) -> List[Tuple[str, str]]:
        """
        Make a query searching for the student and the courses in which the student is enrolled.
        It receives the student's CPF as a parameter.
        """

        with self.__ConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Student)
                    .where(Student.cpf == student_cpf)
                    .join(Registration, Student.id_student == Registration.id_student)
                    .join(Course, Registration.id_course == Course.id_course)
                    .with_entities(Student.name, Course.name)
                    .all()
                )
                return data
            except Exception as exception:
                raise exception

    def insert(self, name: str, cpf: str, fullname: str = "") -> str:
        """Inserting a new student."""

        try:
            with self.__ConnectionHandler() as db:
                data = Student(name=name, fullname=fullname, cpf=cpf)
                db.session.add(data)
                db.session.commit()
            return f"Student {name} successfully registered"
        except Exception as exception:
            db.session.rollback()
            raise exception

    def update(self, name: str, cpf: str, fullname: str = "") -> str:
        """Updating the name and fullname fields in the students table."""

        with self.__ConnectionHandler() as db:
            db.session.query(Student).filter(Student.cpf == cpf).update(
                {"name": name, "fullname": fullname}
            )
            db.session.commit()
            return "Update was successful"

    def delete(self, cpf: str) -> str:
        """Deleting a student."""

        with self.__ConnectionHandler() as db:
            db.session.query(Student).filter(Student.cpf == cpf).delete()
            db.session.commit()
            return "Deleting was successful"
