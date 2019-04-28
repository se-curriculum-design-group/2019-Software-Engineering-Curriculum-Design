from backstage.models import Student, User, Major
from scoreManagement.models import Course, CourseScore, MajorCourses
from scoreManagement.utils import stu_search_course, \
    teacher_search_course, stu_view_stat


def test_stu_search_score():
    student = Student.objects.first()
    print(stu_search_course(student))


# test_stu_search_score()


def test_stu_view_stat():
    student = Student.objects.first()
    print(stu_view_stat(student))


# test_stu_view_stat()
del stu_view_stat


def test1():
    for course_score in CourseScore.objects.all()[:10]:
        for teacher in course_score.teaching.tno.all():
            print(teacher.name)
        print('-' * 10)
        for major_course in course_score.teaching.mcno.all():
            print(major_course.cno.cname)
        print('-' * 10)


def test2():
    for course_score in CourseScore.objects.all()[:50]:
        for major_course in course_score.teaching.mcno.all():
            print(major_course.cno.cname)
        print('-' * 10)


# test2()

def test3():
    for course_score in CourseScore.objects.all()[:50]:
        for major_course in course_score.teaching.mcno.all():
            print(major_course)
        print('-' * 20)


# test3()


def test4():
    for course_score in CourseScore.objects.all():
        assert len(course_score.teaching.mcno.all()) == 1

# 因为是对所有的major_course进行一次的遍历，所以只出现一门课被多门老师上的情况。
# test4()

# for course_score in CourseScore.objects.all()[:20]:
#     for major_course in course_score.teaching.mcno.all():

def test5():
    for course_score in CourseScore.objects.all()[:10]:
        print(course_score.teaching.mcno.year)
        print(course_score.teaching.mcno.semester)


print(CourseScore.objects.filter(sno=Student.objects.get(username='2016000002')))