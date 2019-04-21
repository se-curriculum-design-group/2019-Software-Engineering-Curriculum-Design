from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'graduationManagement'
urlpatterns = [
    #path('',views.index,name='index'),
    path('edit_title/', views.edit_title, name='edit_title'),
    path('view_titles/',views.view_titles,name='view_titles'),
]