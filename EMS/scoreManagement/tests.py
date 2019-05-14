from django.test import TestCase, Client, RequestFactory
from backstage.models import User
from .models import Student, Teacher
import django.http.request


class TestStudent(TestCase):
    def test1(self):
        student1 = User.objects.get(username='2016000001')
        student2 = User.objects.get(username='2016000002')
        self.assertEqual(student1.name, '孙章衡')
        self.assertEqual(student2.name, '韩带庐')


class HomePageTest(TestCase):
    def test_home_view_status_code(self):
        url = ""
        data = {
            'username': '2016000001',
            'password': '2016000001'
        }
        respone = self.client.post(url, data=data)
        print(respone)
        self.assertEqual(respone.status_code, 200)


class DemoTest(TestCase):
    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test_demo1(self):
        print("test_demo_1")

    def test_demo2(self):
        print("test_demo2")
