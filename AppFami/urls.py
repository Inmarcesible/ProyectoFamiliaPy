from django.urls import path
from AppFami.views import inicio, hijos, personas, padres, buscar_persona

urlpatterns = [
    path('', inicio, name='AppFamiInicio'),
    path('personas',personas, name = 'AppFamiPersonas'),
    path('hijos',hijos, name = 'AppFamiHijos'),
    path('padres',padres, name = 'AppFamiPadres'),
    path('buscar',buscar_persona, name = 'AppFamiBuscarPersona'),
]
