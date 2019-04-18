from hashlib import sha3_256
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student,\
    Teacher, ClassRoom, MajorPlan
from scoreManagement.models import Course, Teaching
from django.db.utils import IntegrityError


def make_encode(password):
    m = sha3_256(password.encode())
    return m.hexdigest()


def encode_stu():
    for stu in Student.objects.all():
        password = make_encode(stu.password)
        stu.password = password
        stu.save()


def encode_teacher():
    for teacher in Teacher.objects.all():
        password = make_encode(teacher.password)
        teacher.password = password
        teacher.save()


if __name__ == '__main__':
    # encode_stu()
    encode_teacher()
