from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

app_name = "backstage"
urlpatterns = [
                path('', views.welcome, name="welcome"),
                url(r'^goto_login/$', views.goto_login, name='goto_login'),
                url(r'^mylogin/$', views.mylogin, name='mylogin'),
                url(r'^mylogout/$', views.mylogout, name='mylogout'),
                url(r'^register/$', views.register, name='register'),
                # path('register_t/', views.register_t, name='register_t'),
                # path('homepage/', views.homepage, name='homepage'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
