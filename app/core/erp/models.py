from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from core.erp.choices import gender_choices


class Estudiante(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=11, unique=True, verbose_name='CI', primary_key=True)
    becado = models.BooleanField(verbose_name='Becado')
    limitaciones = models.CharField(max_length=500, null=True,blank=True, verbose_name='Limitaciones')
    anno = models.IntegerField(verbose_name='Año')
    carrera = models.CharField(max_length=50, verbose_name='Carrera')
    sex = models.CharField(max_length=10, choices=gender_choices,default='male', verbose_name='Sexo')
    facultad = models.CharField(max_length=150, verbose_name='Facultad')
    user = models.CharField(max_length=50, verbose_name='Usuario')
    password = models.CharField(max_length=50, verbose_name='Contraseña')



    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiante'
        db_table = 'estudiante'
        ordering = ['lastName']


class Trabajador(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    lastName = models.CharField(max_length=150, verbose_name='Apellidos')
    ci = models.CharField(max_length=11, unique=True, verbose_name='CI', primary_key=True)
    sex = models.CharField(max_length=1,  choices=gender_choices, default='male', verbose_name='Sexo')
    becado = models.BooleanField(verbose_name='Becado')
    limitaciones = models.CharField(max_length=500, null=True,blank=True,  verbose_name='Limitaciones')
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
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
    turno = models.CharField(max_length=1, verbose_name='Turno')
    diurno = models.BooleanField(verbose_name='Diurno')


    class Meta:
        verbose_name = 'Guardia_Trabajador'
        verbose_name_plural = 'Guardia_Trabajadores'
        db_table = 'guardia_trabajador'
        ordering = ['fecha']


class Guardia_Estudiante(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
    turno = models.CharField(max_length=1, verbose_name='Turno')
    diurno = models.BooleanField(verbose_name='Diurno')


    class Meta:
        verbose_name = 'Guardia_Estudiante'
        verbose_name_plural = 'Guardia_Estudiantes'
        db_table = 'guardia_estudiante'
        ordering = ['fecha']



class Ausencia_Estudiante(models.Model):
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def toJSON(self):
        item = model_to_dict(self)
        return item


    class Meta:
        verbose_name = 'Ausencia_Estudiante'
        db_table = 'Ausencia_estudiante'
        ordering = ['fecha']

class Ausencia_Trabajador(models.Model):
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ausencia_Trabajador'
        db_table = 'ausencia_trabajador'
        ordering = ['fecha']

class Corte_Estudiante(models.Model):
    fecha = models.DateField( verbose_name='Fecha')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    justificacion = models.CharField(max_length=300,verbose_name='Justificación')
    replanificacion = models.DateField(default=datetime.now, verbose_name='Fecha de replanificación')
    causales = models.CharField(max_length=50, default='Injustificado', choices= [
                    ('Injustificado', 'Injustificado'),
                    ('Problemas Personales', 'Problemas Personales'),
                    ('Enfermo con Certificado', 'Enfermo con Certificado'),
                    ('Enfermo sin Certificado', 'Enfermo sin Certificado'),
                    ('Movilizado', 'Movilizado'),
                    ('Trabajador en otra Provincia', 'Trabajador en otra Provincia'),
                    ('En el Extranjero', 'En el Extranjero'),
                    ('Citado con poco tiempo de antelación', 'Citado con poco tiempo de antelación'),
                    ('No Citado', 'No Citado'),
                    ('Baja', 'Baja')], verbose_name='Causales')


    class Meta:
        verbose_name = 'Corte_Estudiante'
        verbose_name_plural = 'Cortes_Estudiantes'
        db_table = 'cortes_estudiantes'
        ordering = ['fecha']

class Corte_Trabajador(models.Model):
    fecha = models.DateField(default=datetime.now,verbose_name='Fecha')
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    justificacion = models.CharField(max_length=300,verbose_name='Justificación')
    replanificacion = models.DateField(default=datetime.now,verbose_name='Fecha de replanificación')
    causales = models.CharField(max_length=50,default='Injustificado', choices= [
                    ('Injustificado', 'Injustificado'),
                    ('Problemas Personales', 'Problemas Personales'),
                    ('Enfermo con Certificado', 'Enfermo con Certificado'),
                    ('Enfermo sin Certificado', 'Enfermo sin Certificado'),
                    ('Movilizado', 'Movilizado'),
                    ('Trabajador en otra Provincia', 'Trabajador en otra Provincia'),
                    ('En el Extranjero', 'En el Extranjero'),
                    ('Citado con poco tiempo de antelación', 'Citado con poco tiempo de antelación'),
                    ('No Citado', 'No Citado'),
                    ('Baja', 'Baja')], verbose_name='Causales')


    class Meta:
        verbose_name = 'Corte_Trabajador'
        verbose_name_plural = 'Cortes_Trabajadores'
        db_table = 'cortes_trabajadores'
        ordering = ['fecha']


class Reporte_Mensual(models.Model):
    fecha = models.DateField(default=datetime.now,verbose_name='Fecha')
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


class Aviso_Corte_Estudiante(models.Model):
    fecha_aviso = models.DateField(default=datetime.now,verbose_name='Fecha de Aviso')
    fecha_citacion = models.DateField(default=datetime.now,verbose_name='Fecha de Citación')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aviso_Corte_Trabajador'
        db_table = 'aviso_corte_estudiante'
        ordering = ['fecha_aviso']

class Aviso_Corte_Trabajador(models.Model):
    fecha_aviso = models.DateField(default=datetime.now, verbose_name='Fecha de Aviso')
    fecha_citacion = models.DateField(default=datetime.now, verbose_name='Fecha de Citación')
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aviso_Corte_Estudiante'
        db_table = 'aviso_corte_trabajador'
        ordering = ['fecha_aviso']

