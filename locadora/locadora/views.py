from django.shortcuts import render, redirect
from .models import *
from .forms import *

def filme_list(request):
    filmes = Filmes.objects.all()
    template_name = 'filme_list.html'
    context = {
        'filmes' : filmes
    }
    return render(request, template_name, context)

def filme_new(request):
    if request.method == 'POST':
        form = FilmesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filmes:filme_list')
    else:
        template_name = 'filme_new.html'
        context = {'form': FilmesForm()}
        return render(request, template_name, context)

def filme_edit(request, pk):
    filme = Filmes.objects.get(id=pk)
    if request.method == 'POST':
        form = FilmesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filmes:filme_list')
    else:
        form = FilmesForm(instance=filme)
        template_name = 'filme_edit.html'
        context = {
            'form': form,
            'pk': pk
        }    
        return render(request, template_name, context)
 
def filme_del(request, pk):
    filme = Filmes.objects.get(id=pk)
    filme.delete()
    return redirect('filmes:filme_list')
