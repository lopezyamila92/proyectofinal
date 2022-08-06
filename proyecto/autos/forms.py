from django import forms

class Formularios_productos(forms.Form):

    name = forms.CharField(max_length=40)
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    stock = forms.IntegerField()
    categoria = forms.CharField(max_length=30)