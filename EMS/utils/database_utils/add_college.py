import os
import re
import pandas as pd
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching
from django.db.utils import IntegrityError


base_dir = '../others/'
xls_file = '2018-2019-1semester.xls'
data_frame = pd.read_excel(os.path.join(base_dir, xls_file))

colleges = list(data_frame['开课学院'].unique())
colleges.remove('网络')
college_short_names = [
    '学工办',
    '文法学院',
    '化工学院',
    '机电学院',
    '经管学院',
    '国教学院',
    '理学院',
    '材料学院',
    '马克思学院',
    '信息学院',
    '生命学院',
    '工程师学院',
    '侯德榜学院',
    '能院',
]

csv_file = '2016-info-major_plan.csv'
major_plan = pd.read_csv(os.path.join(base_dir, csv_file))


class InfoInit:
    def __init__(self, csv_file):
        self.major_plan = pd.read_csv(os.path.join(base_dir, csv_file))
        self.columns = self.major_plan.columns

    def insert(self):
        for row in self.major_plan.iterrows():
            major = Major.objects.get(mno=row[1][1])

            mp = MajorPlan.objects.create(
                major=major,
                year=row[1][0],
                people_num=row[1][4],
                course_num=row[1][5],
                cls_num=row[1][6],
                score_grad=row[1][7],
                stu_years=4
            )
            mp.save()
        pass

    def views(self):
        college = College.objects.get(name='信息科学与技术学院')
        for row in self.major_plan.iterrows():
            Major.objects.create(
                mno=row[1][1],
                mname=row[1][2],
                short_name=row[1][3],
                in_college=college
            )

    def create_adm(self):
        major_plans = MajorPlan.objects.all()
        for major_plan in major_plans:
            prefix = major_plan.major.short_name
            for i in range(major_plan.cls_num):
                subfix = str(major_plan.year)[2:]+"%02d"%(i+1)
                adm_class = AdmClass.objects.create(
                    name=prefix+subfix,
                    major=major_plan
                )
                adm_class.save()

    def create_student(self):
        major_plans = MajorPlan.objects.all()
        last_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        first_name = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
        cnt = 1
        for major_plan in major_plans:
            adm_set = AdmClass.objects.filter(name__contains=major_plan.major.short_name)
            for i in range(major_plan.people_num):
                year = major_plan.year
                sno = str(year) + "%06d" % cnt
                name = choice(last_name) + "".join(choice(first_name) for i in range(2))
                student = Student.objects.create(
                    username=sno,
                    password=sno,
                    name=name,
                    sex=choice([True, False]),
                    score_got=int(major_plan.score_grad*0.8),
                    in_cls=choice(adm_set),
                    in_year=year
                )
                student.save()
                cnt += 1
                print("Success: %d" % len(Student.objects.all()))


def add_college():
    for name, short_name in zip(colleges, college_short_names):
        college = College.objects.create(
            name=name,
            short_name=short_name
        )
        college.save()


def college_information():
    info = College.objects.get(name='信息科学与技术学院')
    print(info)
    print(type(info))


if __name__ == '__main__':
    # print(len(colleges))
    # add_college()
    # college_information()
    # info_init = InfoInit(csv_file)
    # info_init.views()
    # info_init.insert()
    # info_init.create_adm()
    # info_init.create_student()
    pass
