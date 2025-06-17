from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.pais})"

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    ingredientes = models.TextField()
    pasos = models.TextField()

    def __str__(self):
        return self.titulo