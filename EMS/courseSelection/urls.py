from django.conf.urls import url
from django.urls import path, include
from . import views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'courseSelection'
urlpatterns = [

          path('', views.welcome, name="welcome"),
                  path('selection_home_page', views.selection_home_page, name="selection_home_page"),
                  path('stu_tongshi', views.stu_tongshi, name="stu_tongshi"),
                  path('stu_major', views.stu_major, name="stu_major"),
                  path('resultAdd',views.resultAdd,name="resultAdd"),
                  path('teacher_course',views.teacher,name="teacher_course"),
                  path('select_course', views.select_course, name="select_course"),
                  path('delete_course', views.delete, name="delete_course"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                
              
