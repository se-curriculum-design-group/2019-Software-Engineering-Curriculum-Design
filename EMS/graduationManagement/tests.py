
from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from backstage.models import User
from backstage.views import make_encode
from mixer.backend.django import mixer
from .models import Student, Teacher
import django.http.request

app_name = 'graduationManagement'


class TestStudent(TestCase):
    def setUp(self):
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

    def test_student_choose_project(self):
            response = self.client.get('/graduationManagement/student_choose_project')
            self.assertIn(response.status_code, [200, 301, 302])

    def test_student_submit_project(self):
            response = self.client.get('/graduationManagement/student_submit_project')
            self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_project(self):
            response = self.client.get('/graduationManagement/student_view_project')
            self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_score(self):
            response = self.client.get('/graduationManagement/student_view_score')
            self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_project_detail(self):
            response = self.client.get('/graduationManagement/student_view_project_detail')
            self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_project_ischoosen(self):
            response = self.client.get('/graduationManagement/student_view_project_ischoosen')
            self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_project_ischoosendetail(self):
            response = self.client.get('/graduationManagement/student_view_project_ischoosendetail')
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

    def test_teacher_submit_project(self):
        response = self.client.get('/graduationManagement/teacher_submit_project')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_edit_project(self):
        response = self.client.get('/graduationManagement/teacher_edit_project')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_view_project_detail(self):
        response = self.client.get('/graduationManagement/teacher_view_project_detail')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_change_project(self):
        response = self.client.get('/graduationManagement/teacher_change_project')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_delete_project(self):
        response = self.client.get('/graduationManagement/teacher_delete_project')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_choose_student(self):
        response = self.client.get('/graduationManagement/teacher_delete_project')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_view_projectfiles(self):
        response = self.client.get('/graduationManagement/teacher_view_projectfiles')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_view_projectfiles_detail(self):
        response = self.client.get('/graduationManagement/teacher_view_projectfiles_detail')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_submit_score(self):
        response = self.client.get('/graduationManagement/teacher_submit_score')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_submit_score_detail(self):
        response = self.client.get('/graduationManagement/teacher_submit_score_detail')
        self.assertIn(response.status_code, [200, 301, 302])
