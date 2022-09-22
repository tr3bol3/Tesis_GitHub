from django.db import models

# Create your models here.
from django.db import models

class Estudiante(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombre(s)')
    #El unique es para que sea unico
    ci = models.CharField(max_length=11, unique=True, verbose_name='CI')
    age = models.PositiveIntegerField(default=18)

def __str__(self):
    return self.names

class Meta:
    verbose_name = 'Estudiante'
    verbose_name_plural = 'Estudiantes'
    db_table = 'Estudiante'
