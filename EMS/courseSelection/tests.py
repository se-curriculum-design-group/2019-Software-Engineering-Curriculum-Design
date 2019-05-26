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
    def test_stu_tables(self):
        response = self.client.get('/courseSelection/tables')
        self.assertIn(response.status_code, [200, 301, 302])
    def test_stu_selectcourse(self):
        response = self.client.get('/courseSelection/select_course')
        self.assertIn(response.status_code, [200, 301, 302])
    def test_stu_deletecourse(self):
        response = self.client.get('/courseSelection/delete_course')
        self.assertIn(response.status_code, [200, 301, 302])
    def test_stu_findcourse(self):
        response = self.client.get('/courseSelection/find_course')
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

    def test_adm_school(self):
        response = self.client.get('/courseSelection/adm_school')
        self.assertIn(response.status_code, [200, 301, 302])


    def test_time_set(self):
        response = self.client.get('/courseSelection/time_set')
        self.assertIn(response.status_code, [200, 301, 302])
class TestTeacher(TestCase):
    def setUp(self) -> None:
        teacher = mixer.blend(Teacher)
        teacher.username = '198500038'
        teacher.password = make_encode('198500038')
        teacher.save()
        self.log_data = {
            'username': teacher.username,
            'password': teacher.username
        }
        data = {
            'username': '198500038',
            'password': '198500038'
        }

        url = ""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        url = '/mylogin'
        response = self.client.post(url, data=self.log_data)
        self.assertIn(response.status_code, [200, 301, 302])
    def test_teachercourse(self):
        response = self.client.get('/courseSelection/teacher_course')
        self.assertIn(response.status_code, [200, 301, 302])


