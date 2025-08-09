from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from usuarios.views import CustomLoginView, dashboard_admin, dashboard_cliente, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('redireccion_dashboard/', views.redireccion_dashboard, name='redireccion_dashboard'),
    path('dashboard_admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard_cliente/', views.dashboard_cliente, name='dashboard_cliente'),
]