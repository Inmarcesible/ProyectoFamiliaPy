from django.urls import path
from AppFami.views import * #inicio, hijos, personas, padres, buscar_persona, persona_leer, persona_crear

urlpatterns = [
    path('', inicio, name='AppFamiInicio'),
    path('personas',personas, name = 'AppFamiPersonas'),
    path('hijos',hijos, name = 'AppFamiHijos'),
    path('padres',padres, name = 'AppFamiPadres'),
    path('buscar',buscar_persona, name = 'AppFamiBuscarPersona'),
    #urls persona
    path('persona/', persona_leer, name='AppFamiPersonaLeer'),
    path('persona/crear', persona_crear, name='AppFamiPersonaCrear'),
    path('persona/eliminar/<int:rutpersona>', persona_eliminar, name='AppFamiPersonaEliminar'),
    path('persona/editar/<int:rutpersona>', persona_editar, name='AppFamiPersonaEditar'),
]




