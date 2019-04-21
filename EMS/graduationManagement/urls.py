from django.conf.urls import url
from django.urls import path, include
from . import views


app_name = 'graduationManagement'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
                  path('graduation_home_page', views.graduation_home_page, name="graduation_home_page"),
              ]
