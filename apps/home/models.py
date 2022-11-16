# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proveedores (models.Model):
    nombre = models.CharField(max_length=200)
    Rut = models.CharField(max_length=10)
    contacto = models.CharField(max_length=200, null=True)

class Convenio (models.Model):
    anual = "Anual"
    semestral = "Semestral"
    trimestral = "Trimestral"
    Frecuencias = [anual,semestral,trimestral]
    tag = models.CharField(max_length=200)
    idconvenio = models.CharField(max_length=10)
    nombre = models.CharField(max_length=400)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.DO_NOTHING)
    resolucion = models.CharField(max_length=10)
    fechaInicio = models.DateField()
    duracion = models.IntegerField(default=24)
    extension = models.IntegerField(default=0)
    fechaTermino = models.DateField()
    montoTotal = models.IntegerField()
    frecMP = models.CharField(max_length=20, choices=Frecuencias)
    valorCuota = models.IntegerField()
