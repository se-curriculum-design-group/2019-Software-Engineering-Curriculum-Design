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
for item1, item2, item3 in zip(data_frame['课程代码'], data_frame['课程名称'], data_frame['学分']):
    try:
        c = Course.objects.filter(
            cno=item1
        )[0]
        cs_courses.append(c)
    except:
        print(item1)

print(len(cs_courses))
print(len(data_frame))


for course in cs_courses:
    MajorCourses.objects.create(
        cno=course
    )
