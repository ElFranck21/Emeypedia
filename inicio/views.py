import os
from django.conf import settings
from django.http import FileResponse, Http404
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

def contactanos(request):
    return render(request, 'contactanos.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def terminosyc(request):
    return render(request, 'terminosyc.html')

def service_worker(request):
    # ajusta la ruta al archivo según tu estructura
    sw_path = os.path.join(settings.BASE_DIR, 'public', 'service-worker.js')
    if not os.path.exists(sw_path):
        raise Http404("Service worker no encontrado")
    return FileResponse(open(sw_path, 'rb'), content_type='application/javascript')

from django.views.generic import View
from django.http import FileResponse
import os
from django.conf import settings

from django.shortcuts import render

def offline(request):
    return render(request, 'offline.html')