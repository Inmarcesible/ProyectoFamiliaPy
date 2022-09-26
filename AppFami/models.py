from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    rutpersona = models.IntegerField(unique='true')
    genero = models.CharField(max_length=40)
    fecnacimiento = models.CharField(max_length=40)

    def __str__(self):
        return f"Persona: {self.nombre}, Rut: {self.rutpersona}, Genero: {self.genero}, Fecha Nacimiento: {self.fecnacimiento}"

class Hijo(models.Model):
    rutperosna = models.IntegerField()
    ruthijo = models.IntegerField()

    def __str__(self):
        return f"Rut Perona: {self.rutperosna}, Rut Hijo: {self.ruthijo}"

class Padre(models.Model):
    rutperosna = models.IntegerField()
    rutpadre = models.IntegerField()

    def __str__(self):
        return f"Rut Perona: {self.rutperosna}, Rut Padre: {self.rutpadre}"
