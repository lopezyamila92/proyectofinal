from lib2to3.pgen2.token import GREATER
from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render


def template (request):
    context = {
        "lista":["volkswagen","gol","diesel"]
    }
    return render(request, "template.html", context=context)