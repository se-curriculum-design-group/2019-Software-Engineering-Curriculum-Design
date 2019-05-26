from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'courseScheduling'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
                  path('scheduling_home_page', views.scheduling_home_page, name="scheduling_home_page"),
                  path('find_vacant_room', views.find_vacant_room, name="find_vacant_room"),
                  path('time_exam', views.time_exam, name="time_exam"),
                  path("search_time_room", views.search_time_room, name="search_time_room"),
                  path("search_time_room_teacher", views.search_time_room_teacher, name="search_time_room_teacher"),
]
    
    
