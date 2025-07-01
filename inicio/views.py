from django.shortcuts import render
from articulos.models import Articulo

# Create your views here.
def index(request):
    juegos = Articulo.objects.filter(tipo='juego')
    series = Articulo.objects.filter(tipo='serie')
    peliculas = Articulo.objects.filter(tipo='pelicula')

    context = {
        'juegos': juegos,
        'series': series,
        'peliculas': peliculas
    }

    return render(request, 'index.html', context)