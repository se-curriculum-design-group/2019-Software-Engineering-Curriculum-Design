"""
添加其他专业的学生（非信息学院）
"""
import os
import re
import pandas as pd
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan, User
from scoreManagement.models import Course, Teaching, MajorCourses, CourseScore
from django.db.utils import IntegrityError


hgxy = College.objects.get(name='化学工程学院')
cailiao = College.objects.get(name='材料科学与工程学院')
shengming = College.objects.get(name='生命科学与技术学院')
jingguan = College.objects.get(name='经济管理学院')
lixueyuan = College.objects.get(name='理学院')
jidian = College.objects.get(name='机电工程学院')

hg = Major.objects.create(in_college=hgxy, mname='化学工程与工艺', short_name='化工')
huangong = Major.objects.create(in_college=hgxy, mname='环境工程', short_name='环工')
nengyuan = Major.objects.create(in_college=hgxy, mname='能源化学工程', short_name='能源')


