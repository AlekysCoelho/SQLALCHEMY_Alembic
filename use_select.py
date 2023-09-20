"""
SELECT statements are produced by the select() function which returns a Select object. 
The entities and/or SQL expressions to return (i.e. the “columns” clause) are passed positionally 
to the function. From there, additional methods are used to generate the complete statement.

link -> https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#joins
"""

from sqlalchemy import select
from sqlalchemy.orm import Session, aliased

from infra.configs.connection import DBConnectionHandler
from infra.entities.course import Course
from infra.entities.registration import Registration
from infra.entities.student import Student
from infra.entities.teacher import Teacher

engine = DBConnectionHandler().get_engine()
session = Session(engine)

# teachers = select(Teacher).where(Teacher.name == "Roberta")
# result = session.execute(teachers)
# for teacher in result.scalars():
#     print(teacher.fullname)
# >>> Roberta Lima

# students = session.execute(select(Student).order_by(Student.id_student)).all()
# print(students)
# >>> [(Student (id=1, name=Ana),), (Student (id=2, name=Maria),)]

# results = (
#     select(Teacher, Course)
#     .join(Teacher.courses)
#     .order_by(Teacher.id_teacher, Course.id_course)
# )
# for result in session.execute(results):
#     print(f"{result.Teacher.name} - {result.Course.name}")
# >>>   Professor1 - Python
#       Professor2 - Django
#       Professor3 - UX
#       Professor4 - JavaScript


# teacher_cls = aliased(Teacher, name="teacher_cls")
# course_cls = aliased(Course, name="course_cls")
# results = (
#     select(teacher_cls, course_cls)
#     .join(teacher_cls.courses.of_type(course_cls))
#     .order_by(teacher_cls.id_teacher, course_cls.id_course)
# )
# result = session.execute(results).first()
# print(f"{result.teacher_cls.name} - {result.course_cls.name}")
# print()
# for res in session.execute(results):
#     print(f"{res.teacher_cls.name} - {res.course_cls.name}")
# >>>   Professor1 - Python
#       Professor2 - Django
#       Professor3 - UX
#       Professor4 - JavaScript


# results_add_columns = (
#     select(Teacher)
#     .join(Teacher.courses)
#     .add_columns(Course)
#     .order_by(Teacher.id_teacher, Course.id_course)
# )
# for res_columns in session.execute(results_add_columns):
#     print(f"{res_columns.Teacher.name} - {res_columns.Course.name}")
# >>>   Professor1 - Python
#       Professor2 - Django
#       Professor3 - UX
#       Professor4 - JavaScript
