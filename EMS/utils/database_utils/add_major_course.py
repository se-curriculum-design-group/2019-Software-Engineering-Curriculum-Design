import os
import re
import math
import pandas as pd
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching, MajorCourses
from django.db.utils import IntegrityError


base_dir = '../others/'
xls_file = '2016-CS-courses.xlsx'
data_frame = pd.read_excel(os.path.join(base_dir, xls_file))


def get_index():
    print(data_frame.columns)


college = College.objects.get(name='信息科学与技术学院')

cs_courses = []


def ana_data():
    for item1, item2, item3 in zip(data_frame['课程代码'], data_frame['课程名称'], data_frame['学分']):
        try:
            c = Course.objects.filter(
                cno=item1
            )[0]
            cs_courses.append(c)
        except:
            pass
            # print(item1)

# print(len(cs_courses))
# print(len(data_frame))

year = 2016
major = Major.objects.get(mname='计算机科学与技术')
major_plan = MajorPlan.objects.get(major=major, year=year)

# print(major, major_plan)


def add_major_course(df):
    for item in zip(df['课程代码'], df['课程名称'], df['学分'], df['课程代码'], df['总学时'], df['讲课总学时']):
        try:
            c = Course.objects.filter(cno=item[0])[0]
            exam_method = True if '必修' in c.course_type else False
            if not item[5]:
                item[5] = 0
            try:
                MajorCourses.objects.create(
                    cno=c,
                    mno=major_plan,
                    hour_total=item[4],
                    hour_class=item[5],
                    hour_other=item[4] - item[5],
                    year=choice([year, year+1, year+2, year+3]),
                    semester=choice([1, 1, 1, 1, 2, 2, 2, 2, 3]),
                    exam_method=exam_method
                )
            except:
                # print(c, major_plan, item[4], item[5], item[4] - item[5])
                pass
        except:
            print(item)
            pass


def add_hard():
    first_major_course = MajorCourses.objects.first()
    cse_courses = Course.objects.filter(cno__contains='CSE')[:30]
    math_course = Course.objects.filter(cno__contains='MAT')[:10]
    max_course = Course.objects.filter(cno__contains='MAX')
    for courses in [cse_courses, math_course, max_course]:
        for course in courses:
            # try:
            MajorCourses.objects.create(
                cno=course,
                mno=major_plan,
                hour_total=first_major_course.hour_total,
                hour_class=first_major_course.hour_class,
                hour_other=first_major_course.hour_other,
                year=choice([year, year+1, year+2, year+3]),
                semester=choice([1, 2, 3]),
                exam_method=True
            )
            # except:
            #     print(len(MajorCourses.objects.all()))

print(len(MajorCourses.objects.all()))
if __name__ == '__main__':
    # add_major_course(data_frame)
    add_hard()
    pass

