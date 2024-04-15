from django.shortcuts import render, redirect
from locadora.models import *
from locadora.forms import *

def index(request):
    template_name = 'index.html'
    context = {
        'mensagem': 'Bem vindo ao seu catalogo de filmes'
    }
    return render(request, template_name, context)

