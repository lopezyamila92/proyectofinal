from django.shortcuts import render
from servicio.models import Servicios


def create_service(request):
    new_service = Servicios.objects.create(name = "cambio de aceite", price = 1000, stock = 1 )
    context = {
        "new_service" : new_service
    }
    return render (request, "new service.html", context=context)

def list_service(request):
    service = Servicios.objects.all()
    context = {
        "service" : service
        }
    return render (request, "service_list.html", context=context)