from django.urls import path
from AppFami.views import inicio, hijos, personas, padres

urlpatterns = [
    path('', inicio, name='AppFamiInicio'),
    path('personas',personas),
    path('hijos',hijos),
    path('padres',padres),
]
