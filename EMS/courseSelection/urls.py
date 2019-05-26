from django.conf.urls import url
from django.urls import path, include
from . import views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'courseSelection'
urlpatterns = [
                  path('stu_major', views.stu_major, name="stu_major"),
                  path('select_course', views.select_course, name="select_course"),
                  path('delete_course', views.delete, name="delete_course"),
                  path('find_course', views.find_course, name="find_course"),
                  path('teacher_course', views.teacher, name="teacher_course"),
                  path('show_students/?cno=<cno>&course_type=<course_type>', views.show_students, name="show_students"),
                  path('adm_selection_manage', views.adm_selection_manage, name="adm_selection_manage"),
                  path('adm_school', views.adm_school, name="adm_school"),
                  path('time_set', views.time_set, name="time_set"),
                  path('tables', views.tables, name="tables")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
