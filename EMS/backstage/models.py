from django.db import models
from django.contrib.auth.models import User


# 学院
class College(models.Model):
    # 学院名
    name = models.CharField(unique=True, max_length=128)
    # 学院简称
    short_name = models.CharField(unique=True, max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'college'


# 专业
class Major(models.Model):
    # 专业代码,如0403。
    # 04是所在学院的排序，03是专业在院中的排序
    mno = models.CharField(unique=True, max_length=20)
    # 专业名称，唯一，如：计算机科学与技术， 化学工程与工艺
    mname = models.CharField(max_length=128, default="")
    # 专业简称，如：计算机科学与技术--计科， 化学工程与工业--化工
    short_name = models.CharField(max_length=20)
    # 所属学院，外键
    in_college = models.ForeignKey(to=College, on_delete=models.CASCADE)

    def __str__(self):
        return "-".join([self.mno, self.mname])

    class Meta:
        db_table = 'major'


# 专业信息
class MajorPlan(models.Model):
    # 学年，该专业下的那个年级的学生
    year = models.IntegerField()
    # 专业名称，对应了需要的专业
    major = models.ForeignKey(to=Major, on_delete=models.CASCADE)
    # 专业计划班级数
    cls_num = models.IntegerField()
    # 专业计划人数
    people_num = models.IntegerField()
    # 毕业最低学分
    score_grad = models.IntegerField()
    # 学制：毕业需要学习的年数, 4
    stu_years = models.IntegerField()
    # 该年级专业需要修学的课程数,80, 88...
    course_num = models.IntegerField()

    def __str__(self):
        return str(self.year) + '-' + str(self.major)

    class Meta:
        db_table = 'major_plan'
        unique_together = (
            'year', 'major'
        )


# 行政班
class AdmClass(models.Model):
    # 行政班名，如：计科1605
    name = models.CharField(max_length=10, unique=True)
    # 行政班所属专业，由 major.short_name + in_year + 编号（自增）构成
    # 例如：计科1605， 化工1606
    major = models.ForeignKey(to=MajorPlan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'adm_class'


# 学生
class Student(User):
    # 学生姓名
    name = models.CharField(max_length=128)
    # 学号，必须10位，例如：2016011186
    # username = models.CharField()
    # 登录所需密码，初始密码设置为学号
    # password = models.CharField()
    # 学生性别
    sex = models.BooleanField(default=True)
    # 目前已修学分
    score_got = models.IntegerField()
    # 所在的行政班级，外键
    in_cls = models.ForeignKey(to=AdmClass, on_delete=models.CASCADE)

    # 入学年份，用int表示即可，该学生入学的年份
    # 考虑可能留级的情况，入学年份与专业年级不对应
    in_year = models.IntegerField()

    def __str__(self):
        return "-".join([self.username, self.name])

    class Meta:
        db_table = 'student'


# 教师
class Teacher(User):
    # 教师姓名
    name = models.CharField(max_length=128)
    # username, 自带字段
    # 同时也就是教师工号，设置为9位，与学生区分
    # password, 自带字段，默认与工号相同
    sex = models.BooleanField(default=True)
    # 教师所属学院
    college = models.ForeignKey(to=College, on_delete=models.CASCADE)
    # 教师入职的年份
    in_year = models.IntegerField()
    # 学历，在个人信息中显示。如：博士，博士后...
    edu_background = models.CharField(null=True, max_length=128)
    # 在校职位，如：教授，副教授，讲师等
    title = models.CharField(default='讲师', max_length=128)
    # 教师个人简介，可空
    description = models.TextField(null=True)

    def __str__(self):
        return "-".join([self.username, self.name])

    class Meta:
        db_table = 'teacher'


# 教室
class ClassRoom(models.Model):
    # 教室编号，如：A-302， B阶-202
    crno = models.CharField(primary_key=True, max_length=128)
    # 教室类型，阶教180人，中等教室120人，小教室50人
    # 教室类型需要和教室编号对应
    crtype = models.CharField(null=False, max_length=10)

    # 教室能够容纳的学生数目，需要与类型对应
    contain_num = models.IntegerField()

    def __str__(self):
        return self.crno

    class Meta:
        db_table = 'class_room'

