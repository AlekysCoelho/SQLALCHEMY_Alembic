from infra.configs.connection import DBConnectionHandler
from infra.repositories.course_repositories import CourseRepository
from infra.repositories.registration_repositories import RegistrationRepositoy
from infra.repositories.student_repositories import Student, StudentRepository
from infra.repositories.teacher_repositories import TeacherRepository

repo = TeacherRepository(DBConnectionHandler)
repo_course = CourseRepository(DBConnectionHandler)
repo_regist = RegistrationRepositoy(DBConnectionHandler)
repo_student = StudentRepository(DBConnectionHandler)

# repo_insert = repo.insert("Lucia", "544121693-71", "Lucia Costa")
# print(repo_insert)

# query_teacher = repo.select_all()

# Paulo, Ana, Lucia = query_teacher

# print(Paulo.id_teacher)

# respo_course = repo_course.insert(
#     name="JavaScript", codigo="004", id_teacher=Lucia.id_teacher
# )
# print(respo_course)

# respo_course = repo_course.insert(name="UX", codigo="003", id_teacher=Ana.id_teacher)
# print(respo_course)

# respo_course = repo_course.delete("003")

# response = repo.select_all()
# for teacher in response:
#     teacher_course = teacher.courses
#     for item in teacher_course:
#         print(item.name)

# response_t = repo.select_all()
# print(response_t[0].courses[0].name)

# response = repo_course.select_all()
# print(response[0].teacher.name)

# response = repo.selecting_through_a_course("Python")
# print(type(response))

# response = repo_student.insert("Ikky", "87854236985", "Ikky de Fênix")
# print(response)

# response = repo_student.select_all_courses("87854236985")
# print(response)
# print(type(response))

# response = repo_regist.select_all()
# print(response)
