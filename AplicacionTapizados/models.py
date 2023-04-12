from django.db import models

class Usuario(models.Model):
    Usuario = models.CharField(max_length=30)
    Clave = models.CharField(max_length=30)

class Administrador(models.Model):
    Usuario = models.CharField(max_length=30)
    Clave = models.CharField(max_length=30)