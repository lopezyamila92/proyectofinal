from django.db import models

class Autos(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='cars_image/', blank=True, verbose_name='Imagen')

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

class Categorias(models.Model):
    name = models.CharField(max_length=50)

class servicio(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)