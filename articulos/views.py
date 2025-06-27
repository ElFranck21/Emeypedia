from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from articulos.models import Articulo
from django.contrib.auth.decorators import login_required

# Create your views here.
def showArticle(request):
    return render(request, 'articulos.html')


