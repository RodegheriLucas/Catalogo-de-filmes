from django.shortcuts import render, redirect
from locadora.models import Generos
from .forms import *

def genero_list(request):
    generos = Generos.objects.all()
    template_name = 'genero_list.html'
    context = {
        'generos' : generos
    }
    return render(request, template_name, context)

def genero_new(request):
    if request.method == 'POST':
        form = GenerosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('generos:genero_list')
    else:
        template_name = 'genero_new.html'
        context = {'form': GenerosForm()}
        return render(request, template_name, context)

def genero_edit(request, pk):
    genero = Generos.objects.get(id=pk)
    if request.method == 'POST':
        form = GenerosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('generos:genero_list')
    else:
        form = GenerosForm(instance=genero)
        template_name = 'genero_edit.html'
        context = {
            'form': form,
            'pk': pk
        }    
        return render(request, template_name, context)
 
def genero_del(request, pk):
    genero = Generos.objects.get(id=pk)
    genero.delete()
    return redirect('generos:genero_list')
