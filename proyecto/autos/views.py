from enum import auto
from hashlib import new
from itertools import product
from multiprocessing import context
from django.shortcuts import render
from autos.models import Autos


def create_autos(request):
    create_autos = Autos.objects.create(name = "ford falcon", price = 100, stock = 15)
    context = {
        "new_product": create_autos
    }
    return render(request, "new_product.html", context=context)

def list_autos(request):
    autos = Autos.objects.all()
    context = {
        "autos": autos
    } 
    return render(request, "products_list.html", context=context)


