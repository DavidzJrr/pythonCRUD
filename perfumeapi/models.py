from django.db import models


# Create your models here.

class Perfumes(models.Model):
    nome = models.CharField(max_length=100)
    familiaOlfativa = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    volumetria = models.IntegerField()