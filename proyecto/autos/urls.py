
from django.urls import path
from proyecto.views import inicio
from proyecto.views import template
from autos.views import create_autos , list_autos , servicio , inicio , primer_formulario
 



urlpatterns = [
    path("", inicio),
    path('template/', template, name="template"),
    path('create_autos/', create_autos, name = "create_autos"),
    path('list_autos/', list_autos, name = "list_autos"),
    path('servicio/', servicio, name="servicio"),
    path('primer-formulario/', primer_formulario, name="primer-formulario"),


]



