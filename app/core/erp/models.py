from django.db import models
from datetime import datetime

from core.erp.choices import gender_choices


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=11, unique=True, verbose_name='CI', primary_key=True)
    becado = models.BooleanField(verbose_name='Becado')
    limitaciones = models.BooleanField(verbose_name='Limitaciones')
    anno = models.IntegerField(default=1, verbose_name='Año')
    carrera = models.CharField(max_length=50, verbose_name='Carrera')
    sex = models.CharField(max_length=1, verbose_name='Sexo')
    facultad = models.CharField(max_length=150, verbose_name='Facultad')
    user = models.CharField(max_length=50, verbose_name='Usuario')
    password = models.CharField(max_length=50, verbose_name='Contraseña')



    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiante'
        db_table = 'estudiante'
        ordering = ['lastName']


class Trabajador(models.Model):
    ci = models.CharField(max_length=11, unique=True, verbose_name='CI', primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    area = models.CharField(max_length=150, verbose_name='Área de Trabajo')
    user = models.CharField(max_length=50, verbose_name='Usuario')
    password = models.CharField(max_length=50, verbose_name='Contraseña')



    def __str__(self):
        return self.ci


    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        db_table = 'trabajador'
        ordering = ['lastName']


class Guardia_Trabajador(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING)
    day = models.DateField(verbose_name='Fecha')
    turno = models.CharField(max_length=1, verbose_name='Turno')
    diurno = models.BooleanField(verbose_name='Diurno')


    class Meta:
        verbose_name = 'Guardia_Trabajador'
        verbose_name_plural = 'Guardia_Trabajadores'
        db_table = 'guardia_trabajador'
        ordering = ['day']


class Guardia_Estudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.DO_NOTHING)
    day = models.DateField(verbose_name='Fecha')
    turno = models.CharField(max_length=1, verbose_name='Turno')
    diurno = models.BooleanField(verbose_name='Diurno')


    class Meta:
        verbose_name = 'Guardia_Estudiante'
        verbose_name_plural = 'Guardia_Estudiantes'
        db_table = 'guardia_estudiante'
        ordering = ['day']



class Ausencia_Estudiante(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'Ausencia_Estudiante'
        db_table = 'Ausencia_estudiante'
        ordering = ['fecha']

class Ausencia_Trabajador(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    trabajador = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Ausencia_Trabajador'
        db_table = 'ausencia_trabajador'
        ordering = ['fecha']

class Corte(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.DO_NOTHING)
    justifiacion = models.CharField(max_length=300,verbose_name='Justificación')
    replanificacion = models.DateField(verbose_name='Fecha de replanificación')


    class Meta:
        verbose_name = 'Corte'
        verbose_name_plural = 'Cortes'
        db_table = 'cortes'
        ordering = ['fecha']


class Reporte_Mensual(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    plan_est = models.IntegerField(verbose_name='Plan de Estudiante')
    real_est = models.IntegerField(verbose_name='Real Estudiante')

    plan_trab = models.IntegerField(verbose_name='Plan Trabajador')
    real_trab = models.IntegerField(verbose_name='Real de Trabajador')

    total_ausencias = models.IntegerField(verbose_name='Total de Ausencias')
    porciento_cumplimiento = models.CharField(max_length=4, verbose_name='Cumplimiento de Trabajador')

    reporte_mensual = models.BooleanField(verbose_name='Reporte Mensual')

    class Meta:
        verbose_name = 'Reporte'
        db_table = 'reporte_mensual'


