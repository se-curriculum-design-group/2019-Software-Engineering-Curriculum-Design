from django.conf.urls import url
from django.urls import path, include
from . import views


app_name = 'graduationManagement'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
                  path('graduation_home_page', views.graduation_home_page, name="graduation_home_page"),
                  path('student_choose_project',views.student_choose_project,name="student_choose_project"),
                  path('student_submit_project',views.student_submit_project,name="student_submit_project"),
                  path('teacher_edit_project',views.teacher_edit_project,name="teacher_edit_project"),
                  path('student_view_score',views.student_view_score,name="student_view_score")
              ]
