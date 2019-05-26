import os
import re
import math
import pandas as pd
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching
from django.db.utils import IntegrityError

# from . import make_encoding


base_dir = '../others/'
xls_file = '2018-2019-1semester.xls'
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
                # password = make_encoding.make_encode(username)
                password = username
                try:
                    teacher = Teacher.objects.create(
                        name=name,
                        username=username,
                        sex=choice([True, False]),
                        college=choice(colleges),
                        password=password,
                        in_year=year,
                        edu_background=choice(['博士', '博士后']),
                        title=choice(['教授', '副教授', '副教授', '副教授', '副教授', '讲师', '讲师', '讲师', '讲师', '讲师'])
                    )
                    cnt += 1
                except:
                    pass
        else:
            name = t
            year = randint(1980, 2018)
            try:
                teacher = Teacher.objects.create(
                    name=name,
                    username=str(year) + "%05d" % cnt,
                    sex=choice([True, False]),
                    college=choice(colleges),
                    in_year=year,
                    edu_background=choice(['博士', '博士后']),
                    title=choice(['教授', '副教授', '副教授', '副教授', '副教授', '讲师', '讲师', '讲师', '讲师', '讲师'])
                )
                cnt += 1
            except:
                pass


def ana_course():
    print(len(data_frame[['课程号', '课程名称', '课程性质', '开课学院', '学分']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称', '课程性质', '学分']].drop_duplicates()))
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
        try:
            college = College.objects.get(name=ccollege)
            # print(ctype)
            course = Course.objects.create(
                cno=cno,
                cname=cname,
                college=college,
                course_type=ctype,
                score=score
            )
            print("Success: %d" % cnt)
            cnt += 1
        except:
            print(ccollege)
            print("Error: %d" % len(Course.objects.all()))


if __name__ == '__main__':
    ana_course()
    # insert_teacher()
    # print(len(Teacher.objects.all()))
    insert_course()
    # print(len(Course.objects.all()))
