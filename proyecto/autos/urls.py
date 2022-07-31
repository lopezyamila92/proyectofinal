
from django.urls import path
from proyecto.views import ford
from proyecto.views import template
from autos.views import create_autos , list_autos
 



urlpatterns = [
    path('template/', template, name="template"),
    path('create_autos/', create_autos, name = "create_autos"),
    path('list_autos/', list_autos, name = "list_autos"),
]



