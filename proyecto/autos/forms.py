from django import forms

CHOICES= [
    ('SUV', 'SUV'),
    ('Deportivos', 'Deportivos'),
    ('Pick-ups', 'Pick-ups'),
    ('Sedan', 'Sedan'),
    ]

class Formularios_productos(forms.Form):
    type= forms.CharField(label='Tipo de vehiculo', widget=forms.Select(choices=CHOICES))
    name = forms.CharField(max_length=40)
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    stock = forms.IntegerField()