from django.urls import path
from django.views.generic import DeleteView

from core.erp.views.Corte.views import CorteListView, CorteCreateView, CorteUpdateView, CorteDeleteView
from core.erp.views.Estudiante.views import EstudianteListView, EstudianteCreateView, EstudianteUpdateView, \
    EstudianteDeleteView
from core.erp.views.Guardia_Estudiante_Externo_Diurno.views import GuardiaEstudianteExternoDiurnoListView
from core.erp.views.Guardia_Estudiante_Femenina_Nocturno.views import GuardiaEstudianteNocturnoFemeninaListView
from core.erp.views.Guardia_Estudiante_Femenina_Diurno.views import GuardiaEstudianteFemeninaDiurnoListView
from core.erp.views.Guardia_Estudiante_Maculino_Nocturno.views import GuardiaEstudianteNocturnoMasculinoListView
from core.erp.views.Guardia_Trabajador_Diurno.views import GuardiaTrabajadorDiurnoListView
from core.erp.views.Guardia_Trabajador_Nocturno.views import GuardiaTrabajadorNocturnoListView
from core.erp.views.Reporte_Mensual.views import ReporteMensualListView, ReporteMensualCreateView, \
    ReporteMensualUpdateView, ReporteMensualDeleteView
from core.erp.views.Reporte_Semanal.views import ReporteSemanalListView, ReporteSemanalCreateView, \
    ReporteSemanalUpdateView, ReporteSemanalDeleteView
from core.erp.views.Trabajador.views import TrabajadorListView, TrabajadorCreateView, TrabajadorUpdateView, \
    TrabajadorDeleteView
from core.erp.views.Ausencia_Trabajador.views import AusenciaTrabajadoresListView, AusenciasTrabajadorCreateView, \
    AusenciaTrabajadorUpdateView, AusenciaTrabajadorDeleteView
from core.erp.views.Ausencia_Estudiante.views import AusenciaEstudiantesListView, AusenciasEstudiantesCreateView, \
    AusenciaEstudianteUpdateView, AusenciaEstudianteDeleteView

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
    path('ausencia_estudiante/add', AusenciasEstudiantesCreateView.as_view(), name='ausencia_estudiante_create'),
    path('ausencia_trabajador/add', AusenciasTrabajadorCreateView.as_view(), name='ausencia_trabajador_create'),
    path('corte/add', CorteCreateView.as_view(), name='corte_create'),
    path('reporte_mensual/add', ReporteMensualCreateView.as_view(), name='reporte_mensual_create'),
    path('reporte_semanal/add', ReporteSemanalCreateView.as_view(), name='reporte_semanal_create'),
    path('trabajador/add', TrabajadorCreateView.as_view(), name='trabajador_create'),

    path('estudiante/edit/<int:pk>/', EstudianteUpdateView.as_view(), name='estudiante_update'),
    path('estudiante/delete/<int:pk>/', EstudianteDeleteView.as_view(), name='estudiante_delete'),
    path('ausencia_estudiante/edit/<int:pk>/', AusenciaEstudianteUpdateView.as_view(), name='ausencia_estudiante_update'),
    path('ausencia_estudiante/delete/<int:pk>/', AusenciaEstudianteDeleteView.as_view(), name='ausencia_estudiante_delete'),
    path('ausencia_trabajador/edit/<int:pk>/', AusenciaTrabajadorUpdateView.as_view(), name='ausencia_trabajador_update'),
    path('ausencia_trabajador/delete/<int:pk>/', AusenciaTrabajadorDeleteView.as_view(), name='ausencia_trabajador_delete'),
    path('corte/edit/<int:pk>/', CorteUpdateView.as_view(), name='corte_update'),
    path('corte/delete/<int:pk>/', CorteDeleteView.as_view(), name='corte_delete'),
    path('reporte_mensual/edit/<int:pk>/', ReporteMensualUpdateView.as_view(), name='reporte_mensual_update'),
    path('reporte_mensual/delete/<int:pk>/', ReporteMensualDeleteView.as_view(), name='reporte_mensual_delete'),
    path('reporte_semanal/edit/<int:pk>/', ReporteSemanalUpdateView.as_view(), name='reporte_semanal_update'),
    path('reporte_semanal/delete/<int:pk>/', ReporteSemanalDeleteView.as_view(), name='reporte_semanal_delete'),
    path('trabajador/edit/<int:pk>/', TrabajadorUpdateView.as_view(), name='trabajador_update'),
    path('trabajador/delete/<int:pk>/', TrabajadorDeleteView.as_view(), name='trabajador_delete'),

]
