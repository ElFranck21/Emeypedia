from django.urls import path
from . import views

urlpatterns = [
    path('', views.showArticle, name='show_article'),
]