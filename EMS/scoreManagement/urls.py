from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = 'scoreManagement'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
              ]
