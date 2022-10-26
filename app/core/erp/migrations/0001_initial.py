# Generated by Django 4.1.1 on 2022-10-24 13:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('ci', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='CI')),
                ('becado', models.BooleanField(verbose_name='Becado')),
                ('limitaciones', models.BooleanField(verbose_name='Limitaciones')),
                ('anno', models.IntegerField(verbose_name='Año')),
                ('carrera', models.CharField(max_length=50, verbose_name='Carrera')),
                ('sex', models.CharField(choices=[('male', 'Masculino'), ('female', 'Femenino')], default='male', max_length=10, verbose_name='Sexo')),
                ('facultad', models.CharField(max_length=150, verbose_name='Facultad')),
                ('user', models.CharField(max_length=50, verbose_name='Usuario')),
                ('password', models.CharField(max_length=50, verbose_name='Contraseña')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiante',
                'db_table': 'estudiante',
                'ordering': ['lastName'],
            },
        ),
        migrations.CreateModel(
            name='Reporte_Mensual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('plan_est', models.IntegerField(verbose_name='Plan de Estudiante')),
                ('real_est', models.IntegerField(verbose_name='Real Estudiante')),
                ('plan_trab', models.IntegerField(verbose_name='Plan Trabajador')),
                ('real_trab', models.IntegerField(verbose_name='Real de Trabajador')),
                ('total_ausencias', models.IntegerField(verbose_name='Total de Ausencias')),
                ('porciento_cumplimiento', models.CharField(max_length=4, verbose_name='Cumplimiento de Trabajador')),
                ('reporte_mensual', models.BooleanField(verbose_name='Reporte Mensual')),
            ],
            options={
                'verbose_name': 'Reporte',
                'db_table': 'reporte_mensual',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('lastName', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('ci', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='CI')),
                ('sex', models.CharField(max_length=1, verbose_name='Sexo')),
                ('becado', models.BooleanField(verbose_name='Becado')),
                ('limitaciones', models.BooleanField(verbose_name='Limitaciones')),
                ('area', models.CharField(max_length=150, verbose_name='Área de Trabajo')),
                ('user', models.CharField(max_length=50, verbose_name='Usuario')),
                ('password', models.CharField(max_length=50, verbose_name='Contraseña')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
                'db_table': 'trabajador',
                'ordering': ['lastName'],
            },
        ),
        migrations.CreateModel(
            name='Guardia_Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('turno', models.CharField(max_length=1, verbose_name='Turno')),
                ('diurno', models.BooleanField(verbose_name='Diurno')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.trabajador')),
            ],
            options={
                'verbose_name': 'Guardia_Trabajador',
                'verbose_name_plural': 'Guardia_Trabajadores',
                'db_table': 'guardia_trabajador',
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='Guardia_Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('turno', models.CharField(max_length=1, verbose_name='Turno')),
                ('diurno', models.BooleanField(verbose_name='Diurno')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.estudiante')),
            ],
            options={
                'verbose_name': 'Guardia_Estudiante',
                'verbose_name_plural': 'Guardia_Estudiantes',
                'db_table': 'guardia_estudiante',
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='Corte_Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('justifiacion', models.CharField(max_length=300, verbose_name='Justificación')),
                ('replanificacion', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de replanificación')),
                ('causales', models.CharField(max_length=50, verbose_name='Causales')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.trabajador')),
            ],
            options={
                'verbose_name': 'Corte_Trabajador',
                'verbose_name_plural': 'Cortes_Trabajadores',
                'db_table': 'cortes_trabajadores',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Corte_Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('justifiacion', models.CharField(max_length=300, verbose_name='Justificación')),
                ('replanificacion', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de replanificación')),
                ('causales', models.CharField(max_length=50, verbose_name='Causales')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.estudiante')),
            ],
            options={
                'verbose_name': 'Corte_Estudiante',
                'verbose_name_plural': 'Cortes_Estudiantes',
                'db_table': 'cortes_estudiantes',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Aviso_Corte_Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aviso', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Aviso')),
                ('fecha_citacion', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Citación')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.trabajador')),
            ],
            options={
                'verbose_name': 'Aviso_Corte_Estudiante',
                'db_table': 'aviso_corte_trabajador',
                'ordering': ['fecha_aviso'],
            },
        ),
        migrations.CreateModel(
            name='Aviso_Corte_Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_aviso', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Aviso')),
                ('fecha_citacion', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Citación')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.estudiante')),
            ],
            options={
                'verbose_name': 'Aviso_Corte_Trabajador',
                'db_table': 'aviso_corte_estudiante',
                'ordering': ['fecha_aviso'],
            },
        ),
        migrations.CreateModel(
            name='Ausencia_Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.trabajador')),
            ],
            options={
                'verbose_name': 'Ausencia_Trabajador',
                'db_table': 'ausencia_trabajador',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Ausencia_Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.estudiante')),
            ],
            options={
                'verbose_name': 'Ausencia_Estudiante',
                'db_table': 'Ausencia_estudiante',
                'ordering': ['fecha'],
            },
        ),
    ]
