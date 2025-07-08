from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import login
from usuarios.forms import RegistroUsuarioForm
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


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
            return redirect('dashboard')  

    else:
        form = RegistroUsuarioForm()

    return render(request, 'register.html', {'form': form})