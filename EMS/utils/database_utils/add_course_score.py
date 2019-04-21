import os
import re
import math
import pandas as pd
from random import choice, randint, choices, sample
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching, MajorCourses, CourseScore
from django.db.utils import IntegrityError


major_name = '计算机科学与技术'
year = 2016


def rand_score_choice():
    """
    返回一个看似合理分布的成绩
    :return: int
    """
    score_choice = [randint(30, 40), randint(40, 60), randint(60, 80), randint(60, 80), randint(70, 90), randint(80, 100)]
    return choice(score_choice)


def get_major_students(major_name, year):
    """
    获取到给定年级和专业的所有学生
    :param major_name: 专业名称，如‘计算机科学与技术’
    :param year: 年级，16级
    :return: QueryDict
    """
    major = Major.objects.get(mname=major_name)
    major_plan = MajorPlan.objects.get(major=major, year=year)
    return Student.objects.filter(in_cls__major=major_plan)

cs_students = get_major_students(major_name, year)


def get_teaching_by_teacher(tno):
    """
    通过教师工号，获取到教师所教的课程
    :param tno: str,教师工号
    :return: QueryDict
    """
    try:
        teacher = Teacher.objects.get(username=tno)
    except Teacher.DoesNotExist:
        raise NameError
    return Teaching.objects.filter(tno=teacher)


def all_teacher_teaching():
    for teacher in Teacher.objects.all():
        print(get_teaching_by_teacher(teacher.username))


# all_teacher_teaching()


def show_all_teaching():
    for teaching in Teaching.objects.all():
        print(teaching)
    print(len(Teaching.objects.all()))

# show_all_teaching()


def get_all_teaching():
    return Teaching.objects.all()


def add_course_score():
    # 对单个学生进行修改，假设其课程都选上了
    for student in Student.objects.all():
        for teaching in get_all_teaching():
            CourseScore.objects.create(
                teaching=teaching,
                sno=student,
                score=rand_score_choice()
            )
    print(len(CourseScore.objects.all()))

# add_course_score()


def show_10_course_score():
    for cs in CourseScore.objects.all()[:10]:
        print(cs)

show_10_course_score()