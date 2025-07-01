from django.urls import path
from . import views

urlpatterns = [
    path('', views.showArticle, name='show_article'),
    path('articulo/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
]