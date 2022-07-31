from enum import auto
from hashlib import new
from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from autos.models import Autos


def inicio (self):
    return HttpResponse("vista de inicio")


def create_autos(request):
    create_autos = Autos.objects.create(name = "ford ranger", price = 1000, stock = 30)
    context = {
        "new_product": create_autos
    }
    return render(request, "new_product.html", context=context)

def list_autos(request):
    products = Autos.objects.all()
    context = {
        "products": products
    } 
    return render(request, "products_list.html", context=context)





def ford_autos(request):
    new_autos = Autos.objects.create(
        title = 'coche nuevo', 
        description = 'unidad de preentrega', 
        author = 'ford oficial'
        )
    context = {
        'new_autos':new_autos
    }
    return render(request, 'preentrega.html', context=context)
