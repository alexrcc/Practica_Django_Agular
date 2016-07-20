
from django.shortcuts import render, redirect
from .forms import FormularioAlumno, FormularioMateria
from .models import Alumno, Materia

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def listar(request):
	alumnos = Alumno.objects.all()
	materias = Materia .objects.all()
	context={
		'alumnos':alumnos,
		'materias':materias,
	}
	return render(request,"listar.html",context)

def crear_alumno(request):
	f=FormularioAlumno(request.POST or None)

	if request.method == 'POST':

		if f.is_valid():
			f_data=f.cleaned_data
			cl = Alumno()
			cl.nombres=f_data.get("nombres")
			cl.apellidos=f_data.get("apellidos")
			cl.cedula=f_data.get("cedula")

			if (cl.save() != True):
				return redirect(listar)
	context={
		"form":f,
	}
	return render(request,"crearAlumno.html",context)

def crear_materia(request):
	f=FormularioMateria(request.POST or None)

	if request.method == 'POST':

		if f.is_valid():
			f_data=f.cleaned_data
			cl = Materia()
			cl.nombreMateria=f_data.get("nombreMateria")
			cl.cupos=f_data.get("cupos")

			if (cl.save() != True):
				return redirect(listar)
	context={
		"form":f,
	}
	return render(request,"crearMateria.html",context)