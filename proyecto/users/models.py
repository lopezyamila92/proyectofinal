from django.db import models


class User_profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    is_active=models.BooleanField(default=True)
    name = models.CharField(max_length=50, blank=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Apellido',default='')
    email = models.EmailField(blank=False)
    description = models.CharField(max_length=350, blank=True, verbose_name='Descripción')
    image = models.ImageField(upload_to='profile_image/', blank=True, verbose_name='Imagen')
    website = models.CharField(max_length=300, blank=True,null=True)

    def __str__(self):
        return self.user.username + ' - profile'
