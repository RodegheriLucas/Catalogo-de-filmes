from django.urls import path
from locadora.views import *
from genero.views import *
from filme.views import index

app_name = 'filme'

urlpatterns = [
    path('genero_list/', genero_list, name='genero_list'),  
    path('genero_new/', genero_new, name='genero_new'),  
    path('genero_del/<int:pk>/', genero_del, name='genero_del'),
    path('genero_edit/<int:pk>/', genero_edit, name='genero_edit'),
]