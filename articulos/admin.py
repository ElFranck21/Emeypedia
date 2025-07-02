from django.contrib import admin
from .models import Articulo
from .forms import ArticuloAdminForm

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    form = ArticuloAdminForm