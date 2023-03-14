#from django.contrib import admin
from django.urls import path

from gestionCursos.views import cursos, estudiantes, profesores


urlpatterns = [
    #path('admin/', admin.site.url),
    path('inicio/', cursos),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
  
    ]