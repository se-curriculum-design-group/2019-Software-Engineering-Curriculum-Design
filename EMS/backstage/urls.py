from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

app_name = "backstage"
urlpatterns = [
                  path('welcome', views.welcome, name="welcome"),
                  path('', views.goto_login, name='goto_login'),
                  path('mylogin', views.mylogin, name='mylogin'),
                  path('mylogout', views.mylogout, name='mylogout'),
                  path('register', views.register, name='register'),
                  path('hello_student', views.student_view, name='student_view'),
                  path('hmy_personal_detailsello_teacher', views.teacher_view, name='teacher_view'),
                  path('hello_admin', views.admin_view, name='admin_view'),
                  path('backstage_manage', views.backstage_manage, name='backstage_manage'),
                  path('my_personal_details', views.my_personal_details, name='my_personal_details'),
                  path('check_announcements', views.check_announcement, name='check_announcements'),
                  path('send_announcements', views.send_announcement, name='send_announcements'),
                  path('send_emails', views.send_emails, name='send_emails'),

                    # 查看所有的学生信息
                  path('adm_view_all_stu', views.adm_view_all_stu, name='adm_view_all_stu'),
                    # 查看所有的教师信息
                  path('adm_view_all_teacher', views.adm_view_all_teacher, name='adm_view_all_teacher'),
                    # 查看所有的课程信息
                  path('adm_view_all_course', views.adm_view_all_course, name='adm_view_all_course'),
                    # 查看所有的教室信息
                  path('adm_view_all_class_room', views.adm_view_all_class_room, name='adm_view_all_class_room'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
