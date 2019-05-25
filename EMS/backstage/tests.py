from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from backstage.models import User
from backstage.views import make_encode
from mixer.backend.django import mixer
from .models import Student, Teacher
import django.http.request

app_name = 'backstage'

class TestAll(TestCase):
    def test_welcome(self):
        response = self.client.get('/backstage/welcome')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_register(self):
        response = self.client.get('/backstage/register')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_hello_student(self):
        response = self.client.get('/backstage/hello_student')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_hmy_personal_detailsello_teacher(self):
        response = self.client.get('/backstage/hmy_personal_detailsello_teacher')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_hello_admin(self):
        response = self.client.get('/backstage/hello_admin')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_backstage_manage(self):
        response = self.client.get('/backstage/backstage_manage')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_my_personal_details(self):
        response = self.client.get('/backstage/my_personal_details')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_check_announcements(self):
        response = self.client.get('/backstage/check_announcements')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_send_announcements(self):
        response = self.client.get('/backstage/send_announcements')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_send_emails(self):
        response = self.client.get('/backstage/send_emails')
        self.assertIn(response.status_code, [200, 301, 302])

class TestAdm(TestCase):
    def setUp(self):
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

    def test_adm_view_all_stu(self):
        response = self.client.get('/backstage/adm_view_all_stu')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_view_all_teacher(self):
        response = self.client.get('/backstage/adm_view_all_teacher')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_view_all_course(self):
        response = self.client.get('/backstage/adm_view_all_course')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_view_all_class_room(self):
        response = self.client.get('/backstage/adm_view_all_class_room')
        self.assertIn(response.status_code, [200, 301, 302])
