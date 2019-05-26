from hashlib import sha3_256
from random import choice, randint, choices
from backstage.models import College, Major, AdmClass, Student, \
    Teacher, ClassRoom, MajorPlan, User
from courseScheduling.models import Course, Teaching
from django.db.utils import IntegrityError


def make_encode(password: str):
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


def encode_adm():
    users = User.objects.filter(is_superuser=True)
    for u in users[1:]:
        u.password = make_encode(u.username)
        u.save()

def view_adm_password():
    for s in User.objects.filter(is_superuser=True):
        print(s.username)
        print(s.password)


if __name__ == '__main__':
    # encode_stu()
    # encode_teacher()
    # view_adm_password()
    encode_adm()
