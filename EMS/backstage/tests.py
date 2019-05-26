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


class TestAdm(TestCase):
    def setUp(self):
        adm = mixer.blend(User)
        adm.is_superuser = True
        adm.username = 'superuser10'
        adm.password = make_encode('superuser10')
        adm.save()
        self.log_data = {
            'username': adm.username,
            'password': 'superuser10'
        }
        data = {
            'username': 'superuser10',
            'password': 'superuser10'
        }

        url = ""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        url = '/mylogin'
        response = self.client.post(url, data=self.log_data)
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_view_all_stu(self):
        response = self.client.get('/adm_view_all_stu')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_view_all_teacher(self):
        response = self.client.get('/adm_view_all_teacher')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_view_all_course(self):
        response = self.client.get('/adm_view_all_course')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_view_all_class_room(self):
        response = self.client.get('/adm_view_all_class_room')
        self.assertIn(response.status_code, [200, 301, 302])
