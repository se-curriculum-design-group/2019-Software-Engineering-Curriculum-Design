from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = 'scoreManagement'
urlpatterns = [
                  path('welcome', views.welcome, name="welcome"),
                  path('score_home_page', views.score_home_page, name="score_home_page"),
                  path('adm_all_course_score', views.adm_all_course_score, name="adm_all_course_score"),
                  path('assess_teacher', views.assess_teacher, name = "assess_teacher"),
                  path('submit_result', views.submit_result, name = "submit_result"),
                  path('submit_all', views.submit_all, name="submit_all"),

]
