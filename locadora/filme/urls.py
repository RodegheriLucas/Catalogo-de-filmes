from django.urls import path
from locadora.views import *
from genero.views import *
from .views import index

app_name = 'filme'

urlpatterns = [
    path('', index, name='index'),
    path('filme_list/', filme_list, name='filme_list'),  
    path('filme_new/', filme_new, name='filme_new'),  
    path('filme_del/<int:pk>/', filme_del, name='filme_del'),
    path('filme_edit/<int:pk>/', filme_edit, name='filme_edit'),
]
