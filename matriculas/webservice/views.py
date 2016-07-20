from django.shortcuts import render

# Create your views here.
from gestion.models import Alumno, Materia
from .serializable import AlumnoSerializable,MateriaSerializable
from rest_framework import viewsets


class AlumnoViewSet(viewsets.ModelViewSet):
	#llamo al objeto serializable
	serializer_class= AlumnoSerializable
	#defino la consulta de datos que se enviara en el web service
	queryset = Alumno.objects.all().order_by('apellidos')
class MateriaViewSet(viewsets.ModelViewSet):
	#llamo al objeto serializable
	serializer_class= MateriaSerializable
	#defino la consulta de datos que se enviara en el web service
	queryset = Materia.objects.filter(cupos__lte=29)




