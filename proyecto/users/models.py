from django.db import models
from django.utils.text import slugify   #importo la libreria slugify

# Create your models here.
class User_profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=False, verbose_name='Nombre Completo')
    email = models.EmailField(blank=False)
    description = models.CharField(max_length=350, blank=False, verbose_name='Descripción')
    image = models.ImageField(upload_to='profile_image/', blank=True, verbose_name='Imagen')
    website = models.CharField(max_length=300, blank=True,null=True)

    def __str__(self):
        return self.user.username + ' - profile'