from django.conf.urls import url
from django.contrib import admin



urlpatterns = [
    url(r'^$', 'gestion.views.listar'),
    url(r'^crearAlumno/$', 'gestion.views.crear_alumno'),
    url(r'^crearMateria/$', 'gestion.views.crear_materia'),
    ]