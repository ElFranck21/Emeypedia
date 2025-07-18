from django.urls import path
from . import views

urlpatterns = [
    path('', views.showArticle, name='show_article'),
    path('articulo/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
    path('crear/', views.crear_articulo, name='crear_articulo'),
    path('buscar/', views.buscar_articulos, name='buscar_articulos'),
    path('editar/<int:articulo_id>/', views.EditarArt, name='editar_articulo'),
    path('eliminar/<int:articulo_id>/', views.eliminar_articulo, name='eliminar_articulo'),
    path('detalle/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
]