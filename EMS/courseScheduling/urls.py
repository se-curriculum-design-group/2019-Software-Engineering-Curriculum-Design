from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'courseScheduling'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
                  path('scheduling_home_page', views.scheduling_home_page, name="scheduling_home_page"),
              ]
