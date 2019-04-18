import os
import re
import math
import pandas as pd
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching
from django.db.utils import IntegrityError


base_dir = '../others/'
xls_file = '2018-2019-3semester.xls'
data_frame = pd.read_excel(os.path.join(base_dir, xls_file))
data_frame = data_frame[data_frame['开课学院'] != '网络']


def insert_teacher():
    colleges = College.objects.all()
    teachers = data_frame['任课教师'].unique()
    cnt = 1
    for t in teachers:
        if ';' in t:
            for tt in t.split(';'):
                name = tt
                year = randint(1980, 2018)
                username = str(year) + "%05d" % cnt
                teacher = Teacher.objects.create(
                    name=name,
                    username=username,
                    sex=choice([True, False]),
                    college=choice(colleges),
                    password=username,
                    in_year=year,
                    edu_background=choice(['博士', '博士后']),
                    title=choice(['教授', '副教授', '副教授', '副教授', '副教授', '讲师', '讲师', '讲师', '讲师', '讲师'])
                )
                teacher.save()
                cnt += 1
        else:
            name = t
            year = randint(1980, 2018)
            teacher = Teacher.objects.create(
                name=name,
                username=str(year) + "%05d" % cnt,
                sex=choice([True, False]),
                college=choice(colleges),
                in_year=year,
                edu_background=choice(['博士', '博士后']),
                title=choice(['教授', '副教授', '副教授', '副教授', '副教授', '讲师', '讲师', '讲师', '讲师', '讲师'])
            )
            teacher.save()
            cnt += 1


def ana_course():
    print(len(data_frame[['课程号', '课程名称', '课程性质', '开课学院', '学分']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称', '课程性质', '开课学院']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称', '课程性质']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称']].drop_duplicates()))
    print(len(data_frame[['课程号']].drop_duplicates()))
    pass


def insert_course():
    cnt = 1
    for row in data_frame[data_frame['开课学院'] != '网络'][['课程号', '课程名称', '课程性质', '开课学院', '学分']].drop_duplicates().iterrows():
        cno = row[1][0]
        cname = row[1][1]
        ctype = row[1][2]
        ccollege = row[1][3]
        score = row[1][4]
        college = College.objects.get(name=ccollege)
        # print(ctype)
        try:
            course = Course.objects.create(
                cno=cno,
                cname=cname,
                college=college,
                course_type=ctype,
                score=score
            )
            course.save()
            print("Success: %d" % cnt)
            cnt += 1
        except:
            print("Error: %d" % len(Course.objects.all()))


if __name__ == '__main__':
    # ana_course()
    insert_course()
