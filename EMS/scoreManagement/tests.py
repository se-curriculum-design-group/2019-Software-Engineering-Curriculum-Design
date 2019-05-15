from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from backstage.models import User
from backstage.views import make_encode
from mixer.backend.django import mixer
from .models import Student, Teacher
import django.http.request


app_name = 'scoreManagement'


class TestStudent(TestCase):
    def setUp(self) -> None:
        student1 = mixer.blend(Student)
        student1.username = '2016000474'
        student1.password = make_encode('2016000474')
        student1.save()
        self.login_data = {
            'username': student1.username,
            'password': student1.username
        }
        data = {
            'username': '2016000474',
            'password': '2016000474'
        }

    def test_student_login(self):
        url = ""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class TestAdm(TestCase):
    def setUp(self) -> None:
        adm = mixer.blend(User)
        adm.is_superuser = True
        adm.password = make_encode(adm.password)
        adm.save()
        self.log_data = {
            'username': adm.username,
            'password': adm.password
        }
        data = {
            'username': 'LuoD',
            'password': '19980818'
        }

    def test_adm_login(self):
        url = ""
        response = self.client.post(url, data=self.log_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


class TestTeacher(TestCase):
    def setUp(self) -> None:
        teacher = mixer.blend(Teacher)
        teacher.password = make_encode(teacher.password)
        teacher.save()
        self.log_data = {
            'username': teacher.username,
            'password': teacher.password
        }
        data = {
            'username': '198500038',
            'password': '198500038'
        }

    def test_teacher_login(self):
        url = ""
        response = self.client.post(url, data=self.log_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
