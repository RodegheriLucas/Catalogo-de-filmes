from django.contrib import admin
from locadora.models import Generos, Filmes

class FilmesAdmin(admin.ModelAdmin):
    list_display = ['filme', 'genero', 'quantidade', 'preco']
    ordering = ['-preco']
    search_fields = ['filme', 'genero']
    list_filter = ['genero', 'preco']
    list_editable = ['quantidade', 'preco']

class GenerosAdmin(admin.ModelAdmin):
    list_display = ['genero']
    ordering = ['genero']
    search_fields = ['genero']
    list_filter = ['genero']

    
admin.site.register(Filmes, FilmesAdmin)
admin.site.register(Generos, GenerosAdmin)
