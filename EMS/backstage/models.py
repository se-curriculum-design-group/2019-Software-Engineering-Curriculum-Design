from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    code = models.CharField(max_length=128, unique=True, default='201600000')
    name = models.CharField(max_length=128, unique=False)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    age = models.CharField(max_length=128, unique=False)
    start_year = models.CharField(max_length=32, default='2019')
    length = models.CharField(max_length=128, unique=False)
    major = models.CharField(max_length=128, unique=False)
    department = models.ForeignKey("Dept", on_delete=models.CASCADE, default=1)
    mod_data = models.DateTimeField('Last modified', auto_now=True)

    def __str__(self):
        return self.codename


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    code = models.CharField(max_length=128, unique=True, default='201600')
    name = models.CharField(max_length=128, unique=False)
    department = models.ForeignKey("Dept", on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=128, unique=False)
    mod_data = models.DateTimeField('Last modified', auto_now=True)


class Dept(models.Model):
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


class Classes(models.Model):
    class_id = models.CharField(max_length=128, unique=True, default='EEE0001')
    name = models.CharField(max_length=128, unique=False)
    type = models.CharField(max_length=128, unique=False)
    size = models.CharField(max_length=128, unique=False)
    department = models.ForeignKey("Dept", on_delete=models.CASCADE, default=1)


class Major(models.Model):
    name = models.CharField(max_length=128, unique=False)
    length = models.CharField(max_length=128, unique=False)
    major_plan = models.CharField(max_length=128, unique=False)


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
