from __future__ import unicode_literals

from django.db import models


class Alumno(models.Model):
	nombres=models.CharField(max_length=30)
	apellidos=models.CharField(max_length=30)
	cedula=models.CharField(max_length=10, unique=True)
	def __str__(self):
		return self.cedula

class Materia(models.Model):
	nombreMateria=models.CharField(max_length=30)
	cupos=models.IntegerField(max_length=2)
	def __str__(self):
		return self.nombreMateria