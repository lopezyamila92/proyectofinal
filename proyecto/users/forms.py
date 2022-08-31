from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


from django import forms

class User_registration_form(UserCreationForm): 
    username = forms.CharField(label='Nombre de Usuario:')
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña:', widget=forms.PasswordInput)  
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

       

class Edit_profile_form(forms.Form):
    
    name = forms.CharField (required=False, label='Nombre', widget=forms.TextInput(attrs={'placeholder':'Ingresa tu Nombre'}))
    last_name = forms.CharField(required=False, label='Apellido', widget=forms.TextInput(attrs={'placeholder':'Ingresa tu Apellido'}))
    description = forms.CharField(required=False, label='Descripción', widget=forms.TextInput(attrs={'placeholde': 'Contanos algo de vos'}))
    image = forms.ImageField(required=False, label='Imagen/Foto')
    website = forms.CharField(required=False, label='WebSite', widget=forms.TextInput(attrs={'placeholder':'Ingresa tu website'}))

class Password_change_form(PasswordChangeForm): 
    pass