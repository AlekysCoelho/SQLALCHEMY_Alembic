from typing import List, Tuple, Type

from sqlalchemy.orm import aliased

from infra.entities.course import Course
from infra.entities.registration import Registration
from infra.entities.student import Student

registration_alias = aliased(Registration)


class RegistrationRepositoy:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler

    def __search_student_course(
        self, id_student: int, id_course: int
    ) -> Tuple[str, str]:
        """Private method to search for the student's name and course, using parameters."""

        with self.__ConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Registration)
                    .filter(Registration.id_course == id_course)
                    .where(Registration.id_student == id_student)
                    .one()
                )
                data = (data.student.name, data.course.name)
                return data
            except Exception as exception:
                raise exception

    def select_all(self) -> List[Tuple[int, str, str]]:
        """Searching all registrations"""

        with self.__ConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Registration)
                    .join(Student, Registration.id_student == Student.id_student)
                    .join(Course, Registration.id_course == Course.id_course)
                    .with_entities(Registration.id_student, Student.name, Course.name)
                    .all()
                )
                return data
            except Exception as exception:
                raise exception

    def searching_course(self, id_student: int) -> List[Tuple[str, int]]:
        """Searches all courses in which the student is enrolled"""

        with self.__ConnectionHandler() as db:
            try:
                data = (
                    db.session.query(Course)
                    .join(
                        registration_alias,
                        Course.id_course == registration_alias.id_course,
                    )
                    .filter(registration_alias.id_student == id_student)
                    .with_entities(Course.name, Course.id_course)
                    .all()
                )
                return data
            except Exception as exception:
                raise exception

    def insert(self, id_student: int, id_course: int) -> str:
        """Inserting a new registration."""

        with self.__ConnectionHandler() as db:
            try:
                data = Registration(id_student=id_student, id_course=id_course)
                db.session.add(data)
                db.session.commit()
                student, course = self.__search_student_course(id_student, id_course)
                message = f"Student registration: {student} in course: {course} completed successfull."
                return message
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update(self, id_student: int, id_course: int) -> str:
        """Updating the id_course field in the registrations table."""

        with self.__ConnectionHandler() as db:
            db.session.query(Registration).filter(
                Registration.id_student == id_student
            ).update({"id_course": id_course})
            db.session.commit()
            return "Update was successful"

    def delete(self, id_student: int) -> str:
        """Deleting a registration."""

        with self.__ConnectionHandler() as db:
            db.session.query(Registration).filter(
                Registration.id_student == id_student
            ).delete()
            db.session.commit()
            return "Deletion was successful"
