from enum import auto
from itertools import product
from multiprocessing import context
from tkinter.tix import AUTO
from django.shortcuts import redirect, render 
from autos.forms import Formularios_productos
from autos.models import Autos


def inicio (self):
    return render(self, "inicio.html")


def create_autos(request):

    if request.method == "POST" :
        form = Formularios_productos(request.POST)

        if form.is_valid():
            Autos.objects.create(
                name = form.cleaned_data["type"]+" "+form.cleaned_data["name"],
                price = form.cleaned_data ["price"],
                description = form.cleaned_data["description"],
                stock = form.cleaned_data["stock"]
            )
            return redirect(list_autos)



    elif request.method == "GET":
        form = Formularios_productos()
        context = {"form": form }    
        return render(request, "new_product.html", context=context)

def list_autos(request):
    products = Autos.objects.all()
    context = {
        "products": products
    } 
    return render(request, "products_list.html", context=context)

def servicio (self):
    return render(self, "servicio.html")



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

def primer_formulario(request):
    print(request.method)
    if request.method == "POST":
        Autos.objects.create(name = request.POST["name"])
    return render (request, "formulario.html", context = {})

def search_products(request):
    search = request.GET["search"]
    products = Autos.objects.filter(name__icontains=search)
    context = {"products" :products}
    return render(request,"search_products.html", context=context)

def delete_product(request, pk):
    if request.method == "GET":
        product = Autos.objects.get(id=pk)
        context = {"product":product}
        return render(request, "delete_product.html", context=context)
    elif request.method == "POST":
        product = Autos.objects.get(id=pk)
        product.delete()
        return redirect(list_autos)

def update_product(request, pk):
    if request.method == "POST":
        form = Formularios_productos(request.POST)
        if form.is_valid():
                product = Autos.objects.get(id=pk)
                product.name = form.cleaned_data["name"]
                product.price = form.cleaned_data ["price"]
                product.description = form.cleaned_data["description"]
                product.stock = form.cleaned_data["stock"]
                product.save()
                return redirect(list_autos)
    elif request.method == "GET":
        product = Autos.objects.get(id=pk)
        form = Formularios_productos(initial = {
                                    "name" :product.name,
                                    "price" :product.price,
                                    "description" :product.description, 
                                    "stock" :product.stock,
                                    })
        context = {"form":form}    
        return render(request, "update_product.html", context=context)
