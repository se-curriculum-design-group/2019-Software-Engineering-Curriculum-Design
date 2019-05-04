import os
import re
import math
import pandas as pd
from random import choice, randint, choices, sample
from backstage.models import College, Major, AdmClass, Student, \
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching, MajorCourses
from django.db.utils import IntegrityError

year = 2016
college = College.objects.get(name='信息科学与技术学院')
major = Major.objects.get(mname='计算机科学与技术')
major_plan = MajorPlan.objects.get(major=major, year=year)


def add_teaching_hard():
    # 找到所有2016级的计科要上的课程
    cs_major_major_courses = MajorCourses.objects.filter(mno=major_plan)
    for major_course in cs_major_major_courses:
        college = major_course.cno.college
        teachers = Teacher.objects.filter(college=college)
        teacher = sample(list(teachers), k=randint(1, 3))
        # try:
        teaching = Teaching.objects.create(weight=choice([0.7, 0.6, 0.8, 0.75, 0.8]))
        teaching.tno.set(teacher)
        teaching.mcno.set([major_course])
        teaching.save()
        # except:
        #     print(len(Teaching.objects.all()))
    print(len(Teaching.objects.all()))


# add_teaching_hard()


def add_teaching_hard2():
    # 找到所有2016级的计科要上的课程
    cs_major_major_courses = MajorCourses.objects.filter(mno=major_plan)
    for major_course in cs_major_major_courses:
        college = major_course.cno.college
        teacher_set = Teacher.objects.filter(college=college)
        teachers = sample(list(teacher_set), k=randint(1, 3))
        for teacher in teachers:
            Teaching.objects.create(
                tno=teacher,
                mcno=major_course,
                weight=choice([0.7, 0.6, 0.8, 0.75, 0.8])
            )


# add_teaching_hard2()

def add_teaching_hard3():
    # 找到所有2016级的计科要上的课程
    cs_major_major_courses = MajorCourses.objects.filter(mno=major_plan)
    college = College.objects.get(name='信息科学与技术学院')
    for teacher in Teacher.objects.filter(college=college):
        college = teacher.college
        course_set = cs_major_major_courses
        if len(course_set) == 0:
            continue
        courses = choices(list(course_set), k=randint(1, len(course_set)))
        for course in courses:
            try:
                Teaching.objects.create(
                    tno=teacher,
                    mcno=course,
                    weight=choice([0.7, 0.6, 0.8, 0.75, 0.8])
                )
            except:
                print("Error %d" %len(Teaching.objects.all()))
    print(len(Teaching.objects.all()))


add_teaching_hard3()


def show_teaching_10():
    print(Teaching.objects.all()[:10])


show_teaching_10()
