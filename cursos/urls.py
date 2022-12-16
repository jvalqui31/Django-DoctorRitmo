from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add, name='add_curso'),
    path('prueba/', prueba_views.cursos, name='prueba'),
]
