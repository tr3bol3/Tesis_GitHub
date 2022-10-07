from django.db import models
from datetime import datetime

from core.erp.choices import gender_choices


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=11, unique=True, verbose_name='CI', primary_key=True)
    becado = models.BooleanField(verbose_name='Becado')
    limitaciones = models.CharField(max_length=300, verbose_name='Limitaciones')
    anno = models.IntegerField(default=1, verbose_name='Año')
    carrera = models.CharField(max_length=50, verbose_name='Carrera')
    sex = models.CharField(max_length=9, verbose_name='Sexo')
    facultad = models.CharField(max_length=150, verbose_name='Facultad')
    user = models.CharField(max_length=50, verbose_name='Usuario')
    password = models.CharField(max_length=50, verbose_name='Contraseña')



    def __str__(self):
        return self.ci

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        db_table = 'estudiante'
        ordering = ['lastName']


class Trabajador(models.Model):
    ci = models.CharField(max_length=5, unique=True, verbose_name='CI')
    name = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    area = models.CharField(max_length=150, verbose_name='Área de Trabajo')
    user = models.CharField(max_length=50, verbose_name='Usuario')
    password = models.CharField(max_length=50, verbose_name='Contraseña')


    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        db_table = 'trabajador'
        ordering = ['id']


class Guardia_Trabajador(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    day_turn = models.CharField(max_length=5, verbose_name='Dia y turno')
    diurna = models.BooleanField(verbose_name='Diurna o Nocturna')

    def __str__(self):
        return self.lastName

    class Meta:
        verbose_name = 'Guardia_Trabajador'
        verbose_name_plural = 'Guardia_Trabajadores'
        db_table = 'guardia_trabajador'
        ordering = ['lastName']


class Guardia_Estudiante(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    carrera = models.CharField(max_length=150, verbose_name='Carrera')
    day_turn = models.CharField(max_length=5, verbose_name='Dia y turno')
    diurna = models.BooleanField(verbose_name='Diurna o Nocturna')

    def __str__(self):
        return self.lastName

    class Meta:
        verbose_name = 'Guardia_Estudiante'
        verbose_name_plural = 'Guardia_Estudiantes'
        db_table = 'guardia_estudiante'
        ordering = ['carrera']



class Guardia_Estudiante_Externo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    carrera = models.CharField(max_length=150, verbose_name='Carrera')
    day_turn = models.CharField(max_length=5, verbose_name='Dia y turno')
    diurna = models.BooleanField(verbose_name='Diurna o Nocturna')

    def __str__(self):
        return self.lastName

    class Meta:
        verbose_name = 'Guardia_Estudiante_Externo'
        verbose_name_plural = 'Guardia_Estudiantes_Externo'
        db_table = 'guardia_estudiante_externo'
        ordering = ['carrera']

class Ausencia_Estudiante(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    ci = models.ForeignKey(Estudiante, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name = 'Ausencia_Estudiante'
        db_table = 'ausencia_estudiante'
        ordering = ['fecha']

class Ausencia_Trabajador(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    ci = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name = 'Ausencia_Trabajador'
        db_table = 'ausencia_trabajador'
        ordering = ['fecha']

class Corte(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    name = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=11, unique=True, verbose_name='CI')

    justifiacion = models.CharField(max_length=300,verbose_name='Justu=ificación')
    replanificacion = models.DateField(verbose_name='Fecha de replanificación')

    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name = 'Corte'
        verbose_name_plural = 'Cortes'
        db_table = 'cortes'
        ordering = ['fecha']


class Reporte_Mensual(models.Model):
    real_est = models.IntegerField(verbose_name='Real Estudiantes')
    plan_est = models.IntegerField(verbose_name='Plan Estudiantes')
    ausencia_est = models.IntegerField(verbose_name='Ausencia Estudiantes')

    plan_trab = models.IntegerField(verbose_name='Plan Trabajador')
    real_trab = models.IntegerField(verbose_name='Real Trabajador')
    ausencia_trab = models.IntegerField(verbose_name='Ausencia Estudiantes')

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        db_table = 'reporte_mensual'


