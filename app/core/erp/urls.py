from django.urls import path

from core.erp.views.Corte.views import CorteListView
from core.erp.views.Estudiante.views import EstudianteListView, EstudianteCreateView
from core.erp.views.Guardia_Estudiante_Externo_Diurno.views import GuardiaEstudianteExternoDiurnoListView
from core.erp.views.Guardia_Estudiante_Femenina_Nocturno.views import GuardiaEstudianteNocturnoFemeninaListView
from core.erp.views.Guardia_Estudiante_Femenina_Diurno.views import GuardiaEstudianteFemeninaDiurnoListView
from core.erp.views.Guardia_Estudiante_Maculino_Nocturno.views import GuardiaEstudianteNocturnoMasculinoListView
from core.erp.views.Guardia_Trabajador_Diurno.views import GuardiaTrabajadorDiurnoListView
from core.erp.views.Guardia_Trabajador_Nocturno.views import GuardiaTrabajadorNocturnoListView
from core.erp.views.Reporte_Mensual.views import ReporteMensualListView
from core.erp.views.Reporte_Semanal.views import ReporteSemanalListView
from core.erp.views.Trabajador.views import TrabajadorListView
from core.erp.views.Ausencia_Trabajador.views import AusenciaTrabajadoresListView
from core.erp.views.Ausencia_Estudiante.views import AusenciaEstudiantesListView, AusenciasEstudiantesCreateView

app_name = 'erp'

urlpatterns = [
    path('estudiante/list', EstudianteListView.as_view(), name='estudiante_list'),
    path('trabajador/list', TrabajadorListView.as_view(), name='trabajador_list'),
    path('ausencia_trabajador/list', AusenciaTrabajadoresListView.as_view(), name='ausencia_trabajador_list'),
    path('ausencia_estudiante/list', AusenciaEstudiantesListView.as_view(), name='ausencia_estudiante_list'),
    path('corte/list', CorteListView.as_view(), name='corte_list'),
    path('reporte_mensual/list', ReporteMensualListView.as_view(), name='reporte_mensual_list'),
    path('reporte_semanal/list', ReporteSemanalListView.as_view(), name='reporte_semanal_list'),
    path('guardia_trabajador_diurno/list', GuardiaTrabajadorDiurnoListView.as_view(),
         name='guardia_trabajador_diurno_list'),

    path('guardia_trabajador_nocturno/list', GuardiaTrabajadorNocturnoListView.as_view(),
         name='guardia_trabajador_nocturno_list'),

    path('guardia_estudiante_externo_diurno/list', GuardiaEstudianteExternoDiurnoListView.as_view(),
         name='guardia_estudiante_femenina_nocturna_list'),

    path('guardia_estudiante_femenina_nocturno/list', GuardiaEstudianteNocturnoFemeninaListView.as_view(),
         name='guardia_estudiante_femenina_nocturno_list'),

    path('guardia_estudiante_masculino_nocturno/list', GuardiaEstudianteNocturnoMasculinoListView.as_view(),
         name='guardia_estudiante_masculino_nocturno_list'),

    path('guardia_estudiante_femenina_diurno/list', GuardiaEstudianteFemeninaDiurnoListView.as_view(),
         name='guardia_estudiante_femenina_diurno_list'),

    path('estudiante/add', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('ausencia_estudiante/add', AusenciasEstudiantesCreateView.as_view(), name='ausencia_estudiante_create')

]
