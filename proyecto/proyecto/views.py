from django.shortcuts import render, redirect, HttpResponse

def inicio (self):
    return render(self, "inicio.html")

def categorias (request):
    context = {
        "lista":["SUV", "Pick-ups", "Sedan", "Deportivos"]
    }
    return render(request, "categorias.html", context=context)

def servicio (self):
    return render(self, "servicio.html")




