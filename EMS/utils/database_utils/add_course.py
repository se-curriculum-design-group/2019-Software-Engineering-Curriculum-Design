import os
import pandas as pd
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching



base_dir = '../others/'
xls_file = '2017-2018-1semester.xls'
data_frame = pd.read_excel(os.path.join(base_dir, xls_file))
data_frame = data_frame[data_frame['开课学院'] != '网络']


def ana_course():
    print(len(data_frame[['课程号', '课程名称', '课程性质', '开课学院', '学分']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称', '课程性质', '学分']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称', '课程性质', '开课学院']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称', '课程性质']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称', '开课学院']].drop_duplicates()))
    print(len(data_frame[['课程号', '课程名称']].drop_duplicates()))
    print(len(data_frame[['课程号']].drop_duplicates()))
    pass


def insert_course(data_frame):
    cnt = 1
    for row in data_frame[data_frame['开课学院'] != '网络'][['课程号', '课程名称', '课程性质', '开课学院', '学分']].drop_duplicates().iterrows():
        cno = row[1][0]
        cname = row[1][1]
        ctype = row[1][2]
        ccollege = row[1][3]
        score = row[1][4]
        try:
            college = College.objects.get(name=ccollege)
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


# ana_course()
# insert_course(data_frame)
# print(len(Course.objects.all()))


def add_course(xls_file):
    df = pd.read_excel(xls_file)
    df = df[df['开课学院'] != '网络']
    insert_course(df)


def add_all_course():
    file_path = [
        '2017-2018-1semester.xls',
        '2017-2018-2semester.xls',
        '2017-2018-3semester.xls',
        '2018-2019-1semester.xls',
        '2018-2019-2semester.xls',
        '2018-2019-3semester.xls',
    ]
    for path in file_path:
        add_course(os.path.join(base_dir, path))

add_all_course()

