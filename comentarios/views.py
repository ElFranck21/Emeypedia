# comentarios/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comentario
from .forms import ComentarioForm
from articulos.models import Articulo

@login_required
def agregar_comentario(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.articulo = articulo
            comentario.save()
            return redirect('detalle_articulo', articulo_id=articulo.id)
    else:
        form = ComentarioForm()
    return redirect('detalle_articulo', articulo_id=articulo.id)
