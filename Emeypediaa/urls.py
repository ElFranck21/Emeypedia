from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import articulos
from inicio import views  
from django.contrib.auth import views as auth_views
from usuarios.forms import LoginForm
from usuarios.views import dashboard, register
from articulos import views as articulos_views



urlpatterns = [
    path('', views.index, name='index'),
    path('articulos/', include('articulos.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
