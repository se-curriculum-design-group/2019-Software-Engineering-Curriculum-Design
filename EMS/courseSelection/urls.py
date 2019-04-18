from django.conf.urls import url
from . import views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'courseSelection'
urlpatterns = [
        path('courseHome/', views.courseSelection, name='courseHome'),
        path('personalTable/', views.personalTable, name='personalTable'),
        path('courseSelecting/', views.courseSelecting, name='courseSelecting'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
