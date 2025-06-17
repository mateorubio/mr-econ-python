from django.shortcuts import render, redirect
from django.db import models
from .models import Receta, Autor, Destino
from .forms import RecetaForm, AutorForm, DestinoForm

def home(request):
    query = request.GET.get('q')
    if query:
        recetas = Receta.objects.filter(
            models.Q(titulo__icontains=query) |
            models.Q(destino__nombre__icontains=query)
        )
    else:
        recetas = Receta.objects.all()
    return render(request, 'core/home.html', {'recetas': recetas})

def nueva_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecetaForm()
    return render(request, 'core/receta_form.html', {'form': form})

def nueva_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'core/autor_form.html', {'form': form})

def nuevo_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DestinoForm()
    return render(request, 'core/destino_form.html', {'form': form})

def detalle_receta(request, receta_id):
    receta = Receta.objects.get(id=receta_id)
    return render(request, 'core/receta_detalle.html', {'receta': receta})

def detalle_destino(request, destino_id):
    destino = Destino.objects.get(id=destino_id)
    return render(request, 'core/destino_detalle.html', {'destino': destino})

def detalle_autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    return render(request, 'core/autor_detalle.html', {'autor': autor})