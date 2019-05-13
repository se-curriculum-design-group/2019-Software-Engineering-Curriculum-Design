from django.urls import path, include

from django.conf.urls import url
from . import views

app_name = 'scoreManagement'
urlpatterns = [
    path('welcome', views.welcome, name="welcome"),
    path('score_home_page', views.score_home_page, name="score_home_page"),
    path('student_score', views.student_score, name="student_score"),
    path('student_own_study', views.student_own_study, name="student_own_study"),
    path('adm_all_course_score', views.adm_all_course_score,
         name="adm_all_course_score"),
    path('std_view_major_course', views.std_view_major_course,
         name="std_view_major_course"),
    path('std_view_major_plan', views.std_view_major_plan,
         name="std_view_major_plan"),
    path('assess_teacher', views.assess_teacher, name="assess_teacher"),
    path('submit_result', views.submit_result, name="submit_result"),
    path('submit_all', views.submit_all, name="submit_all"),
    path('teacher_view_teaching', views.teacher_view_teaching, name="teacher_view_teaching"),
    path('teacher_upload_score', views.teacher_upload_score, name="teacher_upload_score"),
]
