from django.db import models


# Create your models here.
class User(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    codename = models.CharField(max_length=128, unique=True, default='2016')
    nickname = models.CharField(max_length=128, unique=False)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True, default="")
    department = models.ForeignKey("Dept", on_delete=models.CASCADE)
    grant = models.CharField(max_length=32, default='3')
    sex = models.CharField(max_length=32, choices=gender, default='男')
    start_year = models.CharField(max_length=32, default='2019')
    end_year = models.CharField(max_length=32, default='2023')

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'users'


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
