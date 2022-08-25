from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from datetime import datetime
from AppFami.models import Persona

from AppFami.dtos import personas_dto

def persona(request, nombre, rutpersona, genero, fecnacimiento):
    per = Persona(nombre=nombre, rutpersona=rutpersona, genero=genero, fecnacimiento=fecnacimiento)
    per.save()
    plantilla = loader.get_template('persona.html')
    contexto = {
        "nombre": per.nombre,
        "rutpersona": per.rutpersona,
        "genero": per.genero,
        "fecnacimiento": per.fecnacimiento
    }
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

# Nuevo
def inicio(request):
    return render(request, 'AppFami/index.html')

"""
def personas(request):
    contexto = {
        'personas': {
            'persona1': 'Nombre1',
            'persona2': 'Nombre2',
            'persona3': 'Nombre3',
        }
    }
    return render(request, 'AppFami/personas.html', contexto)
"""
def personas(request):
    #personas = Persona.object.all() #lista
    return render(request, 'AppFami/personas.html', personas_dto)

def hijos(request):
    return render(request, 'AppFami/hijos.html')

def padres(request):
    #return redirect('AppFamiInicio')
    return render(request, 'AppFami/padres.html')


