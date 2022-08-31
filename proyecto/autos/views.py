from django.shortcuts import redirect, render 
from django.contrib.auth.decorators import login_required

from autos.forms import Formularios_productos
from autos.models import Autos
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio (self):
    return render(self, "inicio.html")

@login_required
def create_autos(request):
    if request.user.is_superuser:
        if request.method == "POST" :
            form = Formularios_productos(request.POST, request.FILES)
            if form.is_valid():
                Autos.objects.create(
                    name = form.cleaned_data["type"]+" "+form.cleaned_data["name"],
                    price = form.cleaned_data ["price"],
                    description = form.cleaned_data["description"],
                    stock = form.cleaned_data["stock"],
                    image = form.cleaned_data['image']
                )
                return redirect(list_autos)

        elif request.method == "GET":
            form = Formularios_productos()
            context = {"form": form }    
            return render(request, "new_product.html", context=context)
    return redirect ('login')


@login_required
def list_autos(request):
    if request.user.is_authenticated:
            products = Autos.objects.all()
            context = {
                "products": products
            } 

            print(products)
            return render(request, "products_list.html", context=context)
    return redirect("login")

@login_required
def servicio (self):
    return render(self, "service_list.html")

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

@login_required
def delete_product(request, pk):
    if request.user.is_superuser:
        if request.method == "GET":
            product = Autos.objects.get(id=pk)
            context = {"product":product}
            return render(request, "delete_product.html", context=context)
        elif request.method == "POST":
            product = Autos.objects.get(id=pk)
            product.delete()
    return redirect('inicio')


@login_required
def update_product(request, pk):
    print (request.user.is_superuser)
    if request.user.is_superuser:   
        if request.method == "POST":
            form = Formularios_productos(request.POST, request.FILES)
            if form.is_valid():
                    product = Autos.objects.get(id=pk)
                    product.name = form.cleaned_data["name"]
                    product.price = form.cleaned_data ["price"]
                    product.description = form.cleaned_data["description"]
                    product.stock = form.cleaned_data["stock"]
                    
                    if form.cleaned_data['image'] !=None:
                        product.image = form.cleaned_data["image"]
                    product.save()
                    return redirect(list_autos)
        elif request.method == "GET":
            product = Autos.objects.get(id=pk)
            form = Formularios_productos(initial = {
                                    "name" :product.name,
                                    "price" :product.price,
                                    "description" :product.description, 
                                    "stock" :product.stock,
                                    "image" : product.image
                                    })
            context = {"form":form}    
            return render(request, "update_product.html", context=context)
    return redirect('login')

class List_articles(LoginRequiredMixin, ListView):
    model = Autos
    template_name = "products_list.html"

def compras (self):
    return render(self, "compras.html")

def conoce_mas (request):
    search = request.GET["id"]
    products = Autos.objects.filter(id__iexact=search)
    context = {"products" :products}
    return render(request,"conoce_mas.html", context=context)
