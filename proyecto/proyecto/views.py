from lib2to3.pgen2.token import GREATER
from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render


def inicio (self):
    return render(self, "inicio.html")

def categorias (request):
    context = {
        "lista":["SUV", "Pick-ups", "Sedan", "Deportivos"]
    }
    return render(request, "categorias.html", context=context)

def servicio (self):
    return render(self, "servicio.html")


