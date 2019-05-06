from backstage.models import Student, User, Major
from scoreManagement.models import Course, CourseScore, MajorCourses
from scoreManagement.utils import stu_search_course


def test_stu_search_score():
    student = Student.objects.first()
    print(stu_search_course(student))

test_stu_search_score()
