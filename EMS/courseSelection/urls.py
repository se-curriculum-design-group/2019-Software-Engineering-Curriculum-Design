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
                  path('select_course', views.select_course, name="select_course"),
                  path('delete_course', views.delete, name="delete_course"),
                  path('find_course', views.find_course, name="find_course"),

                  path('adm_selection_manage', views.adm_selection_manage, name="adm_selection_manage"),
                  path('adm_class', views.adm_class, name="adm_class"),
                  path('adm_school', views.adm_school, name="adm_school"),
                  path('school_query', views.school_query, name="school_query"),
                  path('class_query', views.class_query, name="class_query"),
                  path('time_set', views.time_set, name="time_set"),
                  path('tables', views.tables, name="tables")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

