from django import forms
from about.models import messageContactUs


class contactUsForm(forms.ModelForm):
    subject = forms.CharField(label='Asunto', widget=forms.TextInput(attrs={'placeholder':'Asunto'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Ingresa tu email'}))
    message = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={'placeholder':'Escríbenos un mensaje'}))

    class Meta:
        model = messageContactUs
        fields = ['subject', 'email', 'message']