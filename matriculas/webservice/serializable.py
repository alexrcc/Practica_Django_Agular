#transformar los objetos y dar propiedades para que se puedan representar en otros formatos

from rest_framework import serializers
from gestion.models import Alumno, Materia


class AlumnoSerializable(serializers.ModelSerializer):
	class Meta:
		model = Alumno
		fields = ('cedula','nombres','apellidos')

class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model = Materia
		fields = ('nombreMateria','cupos')

