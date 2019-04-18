from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "backstage"
urlpatterns = [
                path('', views.welcome, name="welcome"),
                path('goto_login/', views.goto_login, name='goto_login'),
                path('mylogin/', views.mylogin, name='mylogin'),
                path('mylogout/', views.mylogout, name='mylogout'),
                path('register/', views.register, name='register'),
                # path('register_t/', views.register_t, name='register_t'),
                # path('homepage/', views.homepage, name='homepage'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
