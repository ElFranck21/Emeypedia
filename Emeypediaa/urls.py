
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from articulos import views  
from django.contrib.auth import views as auth_views
from usuarios.views import dashboard, register



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articulos.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
