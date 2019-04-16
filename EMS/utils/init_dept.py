import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'EMS.settings'
django.setup()

import sys

sys.path.append('..')
from backstage.models import College
from random import choice

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


def init_dept():
    name = choice(dep)[0]
    for i in dep:
        d = College.objects.create(name=i[0], short_name=i[1])
        d.save()


if __name__ == '__main__':
    init_dept()
