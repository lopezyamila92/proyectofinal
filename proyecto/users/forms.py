from django.contrib.auth.forms import UserCreationForm  #UserCreationForm es el mismo que usamos en url
from django.contrib.auth.models import User


from django import forms

class User_registration_form(UserCreationForm): #creamos un formulario nuevo en base al que ya trae django
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)  #widget es lo que hace que cuando escribamos la contraseña aparezca los asterisco para que no se vea

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {k:'' for k in fields} # Saca los comentarios de ayuda