from pyexpat.errors import messages
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse
from articulos.models import Articulo
from comentarios.models import Comentario
from usuarios.forms import RegistroUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'index.html'
    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return reverse('dashboard_admin')
        else:
            return reverse('dashboard_cliente')

def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "El usuario ya existe")
                return render(request, 'register.html', {'form': form})

            user = form.save()
            login(request, user)
            if user.is_staff or user.is_superuser:
                return redirect('dashboard_admin')
            else:
                return redirect('dashboard_cliente')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'register.html', {'form': form})

@login_required
def perfil_view(request):
    articulos_usuario = Articulo.objects.filter(autor=request.user)
    
    return render(request, 'perfil.html', {
        'articulos_usuario': articulos_usuario
    })


@login_required
def redireccion_dashboard(request):
    if  request.user.is_superuser or request.user.is_staff:
        return redirect('dashboard_admin')
    else:
        return redirect('dashboard_cliente')

@login_required
def dashboard_admin(request):
    articulos_usuario = Articulo.objects.filter(autor=request.user)
    comentarios_usuario = Comentario.objects.filter(usuario=request.user).order_by('-fecha_creacion')[:5]
    if not ( request.user.is_superuser or request.user.is_staff):
        return HttpResponseForbidden("No tienes permiso para ver este dashboard.")
    return render(request, 'usuarios/dashboard_admin.html',{
        'articulos': articulos_usuario,
        'comentarios': comentarios_usuario,
    })

@login_required
def dashboard_cliente(request):
    articulos_usuario = Articulo.objects.filter(autor=request.user)
    comentarios_usuario = Comentario.objects.filter(usuario=request.user).order_by('-fecha_creacion')[:5]
    if request.user.is_superuser or request.user.is_staff:
        return HttpResponseForbidden("No tienes permiso para ver este dashboard.")
    return render(request, 'usuarios/dashboard_cliente.html',{
        'articulos': articulos_usuario,
        'comentarios': comentarios_usuario,
    }) 


