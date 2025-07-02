from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from articulos.forms import ArticuloForm
from articulos.models import Articulo
from django.contrib.auth.decorators import login_required

# Create your views here.
def showArticle(request):
    return render(request, 'articulos.html')

from comentarios.forms import ComentarioForm

def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    form = ComentarioForm()
    return render(request, 'detalle_articulo.html', {
        'articulo': articulo,
        'form': form,
    })

@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = ArticuloForm()
    
    return render(request, 'crear_articulo.html', {'form': form})


