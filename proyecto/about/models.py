from django.db import models

# Create your models here.
class Developer(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nombre

class messageContactUs(models.Model):
    subject = models.CharField('Asunto:', max_length=255)
    email = models.EmailField('Email:')
    message = models.CharField('Mensaje:', max_length=500)

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.subject