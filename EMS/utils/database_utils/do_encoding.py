from backstage.models import Teacher, Student, User
from make_encoding import make_encode


for t in Teacher.objects.all():
    t.password = make_encode(t.username)
    t.save()


for s in Student.objects.all():
    s.password = make_encode(s.username)
    s.save()
