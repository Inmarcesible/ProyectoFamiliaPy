from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from datetime import datetime
from AppFami.models import Persona


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

def inicio(request):
    return HttpResponse("Vista Inicio")

def personas(request):
    contexto = {
        'personas': {
            'persona1': 'Nombre1',
            'persona2': 'Nombre2',
            'persona3': 'Nombre3',
        }
    }
    return render(request, 'personas.html', contexto)

def hijos(request):
    return render(request, 'hijos.html')

def padres(request):
    return redirect('AppFamiInicio')