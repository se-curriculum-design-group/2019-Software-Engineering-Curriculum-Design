from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):  # 学生表
    gender = (  # 性别选择
        ('male', '男'),
        ('female', '女'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')  # 一对一关联到User，定义关联名为student
    code = models.CharField(max_length=128, unique=True, default='201600000')  # 定义学生学号
    name = models.CharField(max_length=128, unique=False)  # 定义学生姓名
    sex = models.CharField(max_length=32, choices=gender, default='男')  # 定义学生性别
    age = models.CharField(max_length=128, unique=False)  # 定义学生年龄
    start_year = models.CharField(max_length=32, default='2019')  # 定义入学年
    length = models.CharField(max_length=128, unique=False)  # 定义学制
    major = models.ForeignKey("Major", on_delete=models.CASCADE, default=1)  # 外键关联主修
    department = models.ForeignKey("Dept", on_delete=models.CASCADE, default=1)  # 外键部门
    mod_data = models.DateTimeField('Last modified', auto_now=True)


class Teacher(models.Model):  # 定义teacher表
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')  # 一对一关联到User，连接名teacher，
    code = models.CharField(max_length=128, unique=True, default='201600')  # 定义编号
    name = models.CharField(max_length=128, unique=False)  # 定义姓名
    department = models.ForeignKey("Dept", on_delete=models.CASCADE, default=1)  # 外键关联学院
    title = models.CharField(max_length=128, unique=False)  # 定义职级
    mod_data = models.DateTimeField('Last modified', auto_now=True)


class Dept(models.Model):  # 定义学院
    dep = (
        ('信息科学与技术学院', '信息科学与技术学院'),
        ('化学工程学院', '化学工程学院'),
        ('材料科学与工程学院', '材料科学与工程学院'),
        ('机电工程学院', '机电工程学院'),
        ('经济管理学院', '经济管理学院'),
        ('理学院', '理学院'),
        ('文法学院', '文法学院'),
        ('生命科学与技术学院', '生命科学与技术学院'),
        ('继续教育学院', '继续教育学院'),
        ('马克思主义学院', '马克思主义学院'),
        ('国际教育学院', '国际教育学院'),
        ('侯德榜工程师学院', '侯德榜工程师学院'),
        ('能源学院', '能源学院'),
        ('巴黎居里工程师学院', '巴黎居里工程师学院'),
    )
    name = models.CharField(max_length=32, choices=dep, default="BUCT", unique=True)

    class Meta:
        db_table = 'department'


class Classes(models.Model):  # 定义课程表
    class_id = models.CharField(max_length=128, unique=True, default='EEE0001')  # 定义课程ID
    name = models.CharField(max_length=128, unique=False)  # 定义课程名
    type = models.CharField(max_length=128, unique=False)  # 定义课程类型
    size = models.CharField(max_length=128, unique=False)  # 定义课程容量
    department = models.ForeignKey("Dept", on_delete=models.CASCADE, default=1)  # 定义开课学院


class Major(models.Model):  # 定义主修表
    name = models.CharField(max_length=128, unique=False)  # 定义专业名字
    length = models.CharField(max_length=128, unique=False)  # 定义专业学制
    major_plan = models.CharField(max_length=128, unique=False)  # 定义专业培养计划


class Announcement(models.Model):
    dep = (
        ('全体成员', '全体成员'),
        ('信息科学与技术学院', '信息科学与技术学院'),
        ('化学工程学院', '化学工程学院'),
        ('材料科学与工程学院', '材料科学与工程学院'),
        ('机电工程学院', '机电工程学院'),
        ('经济管理学院', '经济管理学院'),
        ('理学院', '理学院'),
        ('文法学院', '文法学院'),
        ('生命科学与技术学院', '生命科学与技术学院'),
        ('继续教育学院', '继续教育学院'),
        ('马克思主义学院', '马克思主义学院'),
        ('国际教育学院', '国际教育学院'),
        ('侯德榜工程师学院', '侯德榜工程师学院'),
        ('能源学院', '能源学院'),
        ('巴黎居里工程师学院', '巴黎居里工程师学院'),
        ('个人', '个人'),
    )
    title = models.TextField(max_length=150, default='通知')
    messages = models.TextField(max_length=150)
    author = models.CharField(max_length=128)
    receiver = models.CharField(max_length=32, choices=dep, default='全体成员')
    year = models.CharField(max_length=32, default='2016')
    receiver_grade = models.CharField(max_length=32, default="2016"),
    visible = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'announcement'
