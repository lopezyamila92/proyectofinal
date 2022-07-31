from enum import auto
from hashlib import new
from itertools import product
from multiprocessing import context
from django.shortcuts import render
from autos.models import Autos


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


