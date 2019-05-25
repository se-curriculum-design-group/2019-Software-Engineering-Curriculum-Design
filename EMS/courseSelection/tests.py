from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from backstage.models import User
from backstage.views import make_encode
from mixer.backend.django import mixer
from .models import Student, Teacher
import django.http.request

app_name = 'courseSelection'


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

        url = ""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        response = self.client.post('/mylogin', self.login_data)
        self.assertIn(response.status_code, [200, 301, 302])

    def test_stu_major(self):
        response = self.client.get('/courseSelection/stu_major')
        self.assertIn(response.status_code, [200, 301, 302])


class TestAdm(TestCase):
    def setUp(self) -> None:
        adm = mixer.blend(User)
        adm.is_superuser = True
        adm.username = 'LuoD'
        adm.password = make_encode('19980818')
        adm.save()
        self.log_data = {
            'username': adm.username,
            'password': '19980818'
        }
        data = {
            'username': 'LuoD',
            'password': '19980818'
        }

        url = ""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        url = '/mylogin'
        response = self.client.post(url, data=self.log_data)
        self.assertIn(response.status_code, [200, 301, 302])
    def test_adm_selection_manage(self):
        response = self.client.get('/courseSelection/adm_selection_manage')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_class(self):
        response = self.client.get('/courseSelection/adm_class')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_school(self):
        response = self.client.get('/courseSelection/adm_school')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_text(self):
        response = self.client.get('/courseSelection/text')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_class_query(self):
        response = self.client.get('/courseSelection/class_query')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_school_query(self):
        response = self.client.get('/courseSelection/school_query')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_time_set(self):
         response = self.client.get('/courseSelection/time_set')
         self.assertIn(response.status_code, [200, 301, 302])