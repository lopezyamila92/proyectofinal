from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


from django.contrib.auth.forms import AuthenticationForm
from users.forms import User_registration_form
from django.http import HttpResponse


# Create your views here.

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:        #loguea al usuario
                login(request, user)    #funcion importada de django
                
                context = {'message':f'Bienvenido {username}!! :D'}         #hacemos un mje de bienvenida
                return render(request, 'inicio.html', context = context)    #y lo mandamos al inicio

        form = AuthenticationForm()     #como si estuviera el else
        return render(request, 'users/login.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})   #pasamos el fomulario por el context


def show_profile(request):  
    if request.user.is_authenticated:
        context = {
        "profile":request.user.profile
    }
        #print(request.user.profile)
        return render (request, 'users/details.html', context=context)
        