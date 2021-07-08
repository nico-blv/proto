from django.db import models

# Create your models here.

class Vaca(models.Model):
    id = models.BigAutoField(primary_key=True)
    peso = models.TextField(verbose_name="Peso")
    raza = models.TextField(verbose_name="Raza", default="Vaca")
    sexo = models.TextField(verbose_name="Sexo")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created"]

    def __str__(self):
        texto = "{0} ({1})"
        text = "Vacano "
        return texto.format(text, self.id)



class Lote(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipoAlimen = models.TextField(verbose_name="Tipo alimento")
    raza = models.TextField(verbose_name="Raza")
    cantVacuno = models.IntegerField(verbose_name="Cantidad de vacuno", default=1)
    precioReal = models.FloatField(verbose_name="Precio real")
    precioActual = models.FloatField(verbose_name="Precio actual")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created"]

    def __str__(self):
        texto = "{0} ({1})"
        text = "Lote "
        return texto.format(text, self.id)