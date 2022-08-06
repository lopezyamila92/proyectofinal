
from re import search
from django.urls import path
from proyecto.views import inicio
from proyecto.views import template
from autos.views import create_autos , list_autos , servicio , inicio , primer_formulario, search_products
 



urlpatterns = [
    path("", inicio),
    path('template/', template, name="template"),
    path('create_autos/', create_autos, name = "create_autos"),
    path('list_autos/', list_autos, name = "list_autos"),
    path('servicio/', servicio, name="servicio"),
    path('primer-formulario/', primer_formulario, name="primer-formulario"),
    path('search-products/', search_products, name="search_products")


]



