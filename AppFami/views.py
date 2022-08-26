from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from datetime import datetime

from AppFami.forms import PersonaForm, BuscaPersona, HijoForm, PadreForm
from AppFami.models import Persona, Hijo, Padre

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
"""
def personas(request):
    #personas = Persona.object.all() #lista
    return render(request, 'AppFami/personas.html', personas_dto)
"""
def personas(request):
    if request.method == 'POST':
        my_form = PersonaForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            persona_date = Persona(nombre=data.get('nombre'),rutpersona=data.get('rutpersona'),genero=data.get('genero'),fecnacimiento=data.get('fecnacimiento'))
            persona_date.save()

    personas = Persona.objects.all()
    contexto = {
        'personas': personas,
        'my_form': PersonaForm
    }

    return render(request, 'AppFami/personas.html', contexto)

def buscar_persona(request):

    persona_buscar = []
    if request.method == 'POST':
        rut = request.POST.get('rutpersona')
        persona_buscar = Persona.objects.filter(rutpersona__icontains=rut)
        #persona_buscar = Persona.objects.filter(rutpersona__icontains=rut).first() #Trae la primera persona que encuentre
    else:
        redirect('AppFamiPersonas')

    contexto = {
        'my_form': BuscaPersona(),
        'personab': persona_buscar
    }
    return render(request, 'AppFami/buscar_perrsona.html', contexto)

def hijos(request):
    if request.method == 'POST':
        my_form = HijoForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            hijo_date = Hijo(rutperosna=data.get('rutperosna'),ruthijo=data.get('ruthijo'))
            hijo_date.save()

    hijos = Hijo.objects.all()
    contexto = {
        'hijos': hijos,
        'my_form': HijoForm
    }
    return render(request, 'AppFami/hijos.html', contexto)

def padres(request):
    if request.method == 'POST':
        my_form = PadreForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            padre_date = Padre(rutperosna=data.get('rutperosna'),rutpadre=data.get('rutpadre'))
            padre_date.save()

    padres = Padre.objects.all()
    contexto = {
        'padres': padres,
        'my_form': PadreForm
    }
    return render(request, 'AppFami/padres.html', contexto)

    #return redirect('AppFamiInicio')
    #return render(request, 'AppFami/padres.html')


