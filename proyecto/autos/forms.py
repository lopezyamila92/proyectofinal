from django import forms

CHOICES= [
    ('SUV', 'SUV'),
    ('Deportivos', 'Deportivos'),
    ('Pick-ups', 'Pick-ups'),
    ('Sedan', 'Sedan'),
    ]

class Formularios_productos(forms.Form):
    type= forms.CharField(label='Tipo de Vehículo', widget=forms.Select(choices=CHOICES))
    name = forms.CharField(max_length=40, label='Nombre')
    price = forms.FloatField(label='Precio')
    description = forms.CharField(max_length=200, label='Descripción')
    stock = forms.IntegerField(label='Stock')
    image = forms.ImageField(required=False, label='Imagen/Foto')