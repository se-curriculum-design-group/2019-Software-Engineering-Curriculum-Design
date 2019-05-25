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

        url = ""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

        response = self.client.post('/mylogin', self.login_data)
        self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_score(self):
        response = self.client.get('/scoreManagement/student_view_score')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_own_study(self):
        response = self.client.get('/scoreManagement/student_own_study')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_major_course(self):
        response = self.client.get('/scoreManagement/std_view_major_course')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_major_plan(self):
        response = self.client.get('/scoreManagement/std_view_major_plan')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_my_personal_details(self):
        response = self.client.get('/my_personal_details')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_stu_tongshi(self):
        response = self.client.get('/courseSelection/stu_tongshi')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_stu_major(self):
        response = self.client.get('/courseSelection/stu_major')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_student_choose_project(self):
        response = self.client.get('/graduationManagement/student_choose_project')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_project(self):
        response = self.client.get('/graduationManagement/student_view_project')
        self.assertTemplateUsed()
        self.assertIn(response.status_code, [200, 301, 302])

    def test_student_view_score(self):
        response = self.client.get('/graduationManagement/student_view_score')
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

    def test_adm_view_all_stu(self):
        response = self.client.get('/adm_view_all_stu')
        self.assertIn(response.status_code, [200, 301, 302])
        self.assertTemplateUsed(response, '')

    def test_adm_view_major_course(self):
        response = self.client.get('/scoreManagement/adm_view_major_course')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_view_major_plan(self):
        response = self.client.get('/scoreManagement/adm_view_major_plan')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_adm_all_course_score(self):
        response = self.client.get('/scoreManagement/adm_all_course_score')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_send_announcements(self):
        response = self.client.get('/send_announcements')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_send_emails(self):
        response = self.client.get('/send_emails')
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

    def test_teacher_view_major_course(self):
        response = self.client.get('/scoreManagement/teacher_view_major_course')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_view_major_plan(self):
        response = self.client.get('/scoreManagement/teacher_view_major_plan')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_view_teaching(self):
        response = self.client.get('/scoreManagement/teacher_view_teaching')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_upload_score(self):
        response = self.client.get('/scoreManagement/teacher_upload_score')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_my_personal_details(self):
        response = self.client.get('/my_personal_details')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_submit_project(self):
        response = self.client.get('/graduationManagement/teacher_submit_project')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_choose_student(self):
        response = self.client.get('/graduationManagement/teacher_choose_student')
        self.assertIn(response.status_code, [200, 301, 302])

    def test_teacher_submit_score(self):
        response = self.client.get('/graduationManagement/teacher_submit_score')
        self.assertIn(response.status_code, [200, 301, 302])
