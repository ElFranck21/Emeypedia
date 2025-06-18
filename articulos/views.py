from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from articulos.models import Articulo

# Create your views here.
def hello(request):
    articulo = Articulo.objects.first()
    return render(request, 'articulos.html', {'article': articulo})