from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = 'scoreManagement'
urlpatterns = [
                  path('welcome/', views.welcome, name="welcome"),
              ]
