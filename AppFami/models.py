from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    rutpersona = models.IntegerField()
    genero = models.CharField(max_length=40)
    fecnacimiento = models.CharField(max_length=40)

class Hijo(models.Model):
    rutperosna = models.IntegerField()
    ruthijo = models.IntegerField()

class Padre(models.Model):
    rutperosna = models.IntegerField()
    rutpadre = models.IntegerField()
