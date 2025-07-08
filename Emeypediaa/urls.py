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
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.index, name='index'),
    path('articulos/', include('articulos.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('comentarios/', include('comentarios.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
