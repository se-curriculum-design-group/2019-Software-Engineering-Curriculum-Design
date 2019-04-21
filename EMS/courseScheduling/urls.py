from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'courseScheduling'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
              ]
