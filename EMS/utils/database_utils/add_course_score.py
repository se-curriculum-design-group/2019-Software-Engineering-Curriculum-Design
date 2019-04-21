import os
import re
import math
import pandas as pd
from random import choice, randint, choices, sample
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching, MajorCourses, CourseScore
from django.db.utils import IntegrityError


def get_major_students(major_name, year):
    """
    获取到给定年级和专业的所有学生
    :param major_name:
    :param year:
    :return: QueryDict
    """
    major = Major.objects.get(mname=major_name)
    major_plan = MajorPlan.objects.get(major=major)
    return Student.objects.filter(in_cls__major=major_plan)


major_name = '计算机科学与技术'
year = 2016
cs_students = get_major_students(major_name, year)

