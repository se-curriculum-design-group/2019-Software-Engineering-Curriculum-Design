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
        student1.password = make_encode(student1.password)
        student1.save()
        self.login_data = {
            'username': student1.username,
            'password': student1.password
        }

    def test_student_login(self):
        url = ""
        response = self.client.post(url, data=self.login_data)
        self.client.session['user_type'] = '学生'
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

    def test_teacher_login(self):
        url = ""
        response = self.client.post(url, data=self.log_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
