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

def index(request):
    return render(request, 'inicio.html') #cuando no ponemo nada, que sea local host solamente


