from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

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
