from django.conf.urls import url
from django.urls import path, include
from . import views


app_name = 'courseSelection'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
                  path('selection_home_page', views.selection_home_page, name="selection_home_page"),
              ]
