from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from users.forms import Edit_profile_form, Password_change_form
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from users.models import User_profile
from users.forms import User_registration_form



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None: 
                print('login request estoy aca 002')       
                login(request, user)    
                
                context = {'message':f'Bienvenido {username}!! :D'}         
                return render(request, 'inicio.html', context = context)    

        form = AuthenticationForm()     
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
        return render(request, 'users/register.html', {'form': form})  


@login_required
def my_profile(request):    
    if request.user.is_authenticated: 
        print('estoy aca1')                                                    
        try:            
            user = User_profile.objects.get(user=request.user)
        except:            
            user = User_profile.objects.create(user=request.user)
        user.save()     
    if request.method == "POST":  
            print('estoy aca2')                 
            form = Edit_profile_form(request.POST, request.FILES) 
              
            if form.is_valid():  
                print('estoy aca3')   
                print("Image:")
                print(form.cleaned_data['image'])                                                              
                user.name = form.cleaned_data['name']                           
                user.last_name = form.cleaned_data ['last_name']
                user.description = form.cleaned_data['description']
                
                if form.cleaned_data['image'] != None:
                    user.image = form.cleaned_data['image']
                user.website = form.cleaned_data['website']
                user.save()    
                context = {'form':form,'user':user}             
                return render(request, 'users/my_profile.html', context=context)
            
    elif request.method == "GET":
            print('estoy aca4')                   
            form = Edit_profile_form(initial = {
                                    'name':user.name,
                                    'last_name':user.last_name,
                                    'description':user.description,
                                    'image': user.image,
                                    'website':user.website,
                                    })
            context = {'form':form,'user':user}    
            return render(request, 'users/my_profile.html', context=context)
print('estoy aca5')       
    
@login_required
def password_user(request):
    if  request.user.is_authenticated:
        if request.method == 'POST':
            form = Password_change_form(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('inicio')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = Password_change_form(request.user)
        return render(request, 'users/change_password.html', {'form': form})
        


@login_required
def delete_account(request):                       #pk es lo mismo que id
    if request.user.is_authenticated:
        print('delete user estoy aca 001')
        if request.method == 'GET':
            print('delete user estoy aca 002')
            userProfile = User_profile.objects.get(user=request.user)  #trae el objeto que cumplea la condición .get(id=1). el get solamente trae una sola cosa
            context = {'userProfile':userProfile}
            return render(request, 'users/delete_account.html', context=context)     #html de confirmacion de borrado
        elif request.method == 'POST':
            print('delete user estoy aca 003')
            userProfile = User_profile.objects.get(user=request.user)
            userProfile.delete()
            request.user.delete()
            print('delete user estoy aca 004')
    print('delete user estoy aca 005')
    return redirect('login')
    