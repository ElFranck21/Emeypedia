from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from articulos.forms import ArticuloForm
from articulos.models import Articulo
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def showArticle(request):
    return render(request, 'articulos.html')

from comentarios.forms import ComentarioForm

def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    C_form = ComentarioForm()
    return render(request, 'detalle_articulo.html', {
        'articulo': articulo,
        'C_form': C_form,
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



def buscar_articulos(request):
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = Articulo.objects.filter(
            Q(titulo__icontains=query) |
            Q(subcategoria__icontains=query) |
            Q(subcategoria2__icontains=query) |
            Q(subcategoria3__icontains=query) |
            Q(subcategoria4__icontains=query) |
            Q(subcategoria5__icontains=query) |
            Q(subcategoria6__icontains=query) |
            Q(subcategoria7__icontains=query) |
            Q(subcategoria8__icontains=query) |
            Q(subcategoria9__icontains=query) |
            Q(subcategoria10__icontains=query) |
            Q(contenido_texto__icontains=query) |
            Q(contenido_texto2__icontains=query) |
            Q(contenido_texto4__icontains=query) |
            Q(contenido_texto6__icontains=query) |
            Q(contenido_texto7__icontains=query) |
            Q(contenido_texto8__icontains=query) |
            Q(contenido_texto9__icontains=query) |
            Q(contenido_texto10__icontains=query) |
            Q(autor__username__icontains=query)
        ).distinct()

    return render(request, 'buscar_resultados.html', {
        'query': query,
        'resultados': resultados
    })


@login_required
def EditarArt(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)

    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('detalle_articulo', articulo_id=articulo.id)
    else:
        form = ArticuloForm(instance=articulo)

    return render(request, 'editarArt.html', {
        'form': form,
        'articulo': articulo
    })

@login_required
def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)

    if request.user != articulo.autor:
        return HttpResponse("No tienes permiso para eliminar este artículo.", status=403)

    if request.method == 'POST':
        articulo.delete()
        return redirect('perfil')

    return render(request, 'eliminarArt.html', {'articulo': articulo})
