import os
import re
import math
import pandas as pd
from random import choice, randint, choices, sample
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching, MajorCourses
from django.db.utils import IntegrityError


year = 2016
college = College.objects.get(name='信息科学与技术学院')
major = Major.objects.get(mname='计算机科学与技术')
major_plan = MajorPlan.objects.get(major=major, year=year)

def add_teaching_head():
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

if __name__ == '__main__':
    add_teaching_head()
