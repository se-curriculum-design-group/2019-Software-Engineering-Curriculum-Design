from backstage.models import Student, User, Major
from scoreManagement.models import Course, CourseScore, MajorCourses
from scoreManagement.utils import stu_search_course,\
teacher_search_course,stu_view_stat


def test_stu_search_score():
    student = Student.objects.first()
    print(stu_search_course(student))

# test_stu_search_score()


def test_stu_view_stat():
    student = Student.objects.first()
    print(stu_view_stat(student))


test_stu_view_stat()
del stu_view_stat



