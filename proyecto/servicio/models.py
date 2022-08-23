from django.db import models


class Servicios(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'