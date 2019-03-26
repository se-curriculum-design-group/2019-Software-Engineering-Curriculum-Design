from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "backstage"
urlpatterns = [
                  path('', views.Welcome, name="Welcome"),
                  path('Login/', views.Login, name='Login'),
                  path('Log_out/', views.Log_out, name='Log_out'),
                  path('Register/', views.Register, name='Register'),
                  path('Homepage/', views.Homepage, name='Homepage'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
