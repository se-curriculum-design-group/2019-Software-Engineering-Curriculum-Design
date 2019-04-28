from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = 'scoreManagement'
urlpatterns = [
                  path('welcome', views.welcome, name="welcome"),
                  path('score_home_page', views.score_home_page, name="score_home_page"),
                  path('adm_all_course_score', views.adm_all_course_score, name="adm_all_course_score"),
              ]
