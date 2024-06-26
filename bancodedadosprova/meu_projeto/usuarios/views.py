from django.shortcuts import render, get_object_or_404, redirect
from .models import Eventos
from .forms import EventosForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'base.html')


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})


def fazer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('eventos_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def fazer_logout(request):
    logout(request)
    return redirect('login')


def eventos_list(request):
    eventos = Eventos.objects.all()
    return render(request, 'eventos_list.html', {'eventos': eventos})


def eventos_create(request):
    if request.method == 'POST':
        form = EventosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos_list')
    else:
        form = EventosForm()
    return render(request, 'eventos_form.html', {'form': form})


def eventos_update(request, pk):
    eventos = get_object_or_404(Eventos, pk=pk)
    if request.method == 'POST':
        form = EventosForm(request.POST, instance=eventos)
        if form.is_valid():
            form.save()
            return redirect('eventos_list')
    else:
        form = EventosForm(instance=eventos)
    return render(request, 'eventos_form.html', {'form': form})


def eventos_delete(request, pk):
    eventos = get_object_or_404(Eventos, pk=pk)
    if request.method == 'POST':
        eventos.delete()
        return redirect('eventos_list')
    return render(request, 'eventos_confirm_delete.html', {'eventos': eventos})


