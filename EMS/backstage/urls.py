from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "backstage"
urlpatterns = [
                  path('', views.welcome, name="welcome"),
                  path('login/', views.login, name='login'),
                  path('register/', views.register3, name='register'),
                  path('log_out/', views.log_out, name='log_out'),
                  path('homepage/', views.homepage, name='homepage'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
