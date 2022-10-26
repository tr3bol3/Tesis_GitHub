from django.contrib import admin
from core.erp.models import *
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Trabajador)
admin.site.register(Guardia_Trabajador)
admin.site.register(Guardia_Estudiante)
admin.site.register(Ausencia_Estudiante)
admin.site.register(Ausencia_Trabajador)
admin.site.register(Corte_Estudiante)
admin.site.register(Corte_Trabajador)
admin.site.register(Reporte_Mensual)