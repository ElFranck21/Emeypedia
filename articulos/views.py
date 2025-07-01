from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

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



