from django.db import models

class Boxeador(models.Model):
    nome = models.CharField(max_length=100)
    categoria_de_peso = models.CharField(max_length=100)
    registro = models.CharField(max_length=100)
    postura = models.CharField(max_length=100)

class Luta(models.Model):
    boxeador1 = models.ForeignKey(Boxeador, on_delete=models.CASCADE, related_name='luta_boxeador1')
    boxeador2 = models.ForeignKey(Boxeador, on_delete=models.CASCADE, related_name='luta_boxeador2')
    data = models.DateField()
    local = models.CharField(max_length=100)
    vencedor = models.ForeignKey(Boxeador, on_delete=models.SET_NULL, related_name='luta_vencedor', null=True, blank=True)