from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # Django Auth模块中User模型含有的字段
    # username
    # email
    # password
    # first_name
    # last_name    # is_active
    # is_staff
    # is_superuser
    # date_joined

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    codename = models.CharField(max_length=128, unique=True, default='201600000')
    # org = models.CharField('Organization', max_length=128, blank=True,)
    department = models.ForeignKey("Dept", on_delete=models.CASCADE, default=1)
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
