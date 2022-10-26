from django.urls import path

from core.erp.views.Ausencia_Estudiante.views import AusenciaEstudiantesListView, AusenciasEstudiantesCreateView, \
    AusenciaEstudianteUpdateView, AusenciaEstudianteDeleteView
from core.erp.views.Ausencia_Trabajador.views import AusenciaTrabajadoresListView, AusenciasTrabajadorCreateView, \
    AusenciaTrabajadorUpdateView, AusenciaTrabajadorDeleteView
from core.erp.views.Aviso_Corte_Estudiante.views import AvisoCorteEstudianteListView, AvisoCorteEstudianteCreateView, \
    AvisoCorteEstudianteUpdateView, AvisoCorteEstudianteDeleteView
from core.erp.views.Aviso_Corte_Trabajador.views import AvisoCorteTrabajadorListView, AvisoCorteTrabajadorCreateView, \
    AvisoCorteTrabajadorUpdateView, AvisoCorteTrabajadorDeleteView
from core.erp.views.Corte_Estudiante.views import CorteEstudianteListView, CorteEstudianteCreateView, \
    CorteEstudianteUpdateView, CorteEstudianteDeleteView
from core.erp.views.Corte_Trabajador.views import CorteTrabajadorDeleteView, CorteTrabajadorUpdateView, \
    CorteTrabajadorCreateView, CorteTrabajadorListView
from core.erp.views.Estudiante.views import EstudianteListView, EstudianteCreateView, EstudianteUpdateView, \
    EstudianteDeleteView
from core.erp.views.Guardia_Estudiante_Externo_Diurno.views import GuardiaEstudianteExternoDiurnoListView
from core.erp.views.Guardia_Estudiante_Femenina_Diurno.views import GuardiaEstudianteFemeninaDiurnoListView
from core.erp.views.Guardia_Estudiante_Femenina_Nocturno.views import GuardiaEstudianteNocturnoFemeninaListView
from core.erp.views.Guardia_Estudiante_Maculino_Nocturno.views import GuardiaEstudianteNocturnoMasculinoListView
from core.erp.views.Guardia_General_Estudiante.views import GuardiaGeneralEstudianteListView, \
    GuardiaGeneralEstudianteUpdateView, GuardiaGeneralEstudianteDeleteView, GuardiaGeneralEstudianteCreateView
from core.erp.views.Guardia_General_Trabajador.views import GuardiaGeneralTrabajadorCreateView, \
    GuardiaGeneralTrabajadorListView, GuardiaGeneralTrabajadorUpdateView, GuardiaGeneralTrabajadorDeleteView
from core.erp.views.Guardia_Trabajador_Diurno.views import GuardiaTrabajadorDiurnoListView
from core.erp.views.Guardia_Trabajador_Nocturno.views import GuardiaTrabajadorNocturnoListView
from core.erp.views.Reporte_Mensual.views import ReporteMensualListView, ReporteMensualCreateView, \
    ReporteMensualUpdateView, ReporteMensualDeleteView
from core.erp.views.Reporte_Semanal.views import ReporteSemanalListView, ReporteSemanalCreateView, \
    ReporteSemanalUpdateView, ReporteSemanalDeleteView
from core.erp.views.Trabajador.views import TrabajadorListView, TrabajadorUpdateView, \
    TrabajadorDeleteView, TrabajadorCreateView

app_name = 'erp'

urlpatterns = [
    path('estudiante/list', EstudianteListView.as_view(), name='estudiante_list'),
    path('trabajador/list', TrabajadorListView.as_view(), name='trabajador_list'),
    path('ausencia_trabajador/list', AusenciaTrabajadoresListView.as_view(), name='ausencia_trabajador_list'),
    path('ausencia_estudiante/list', AusenciaEstudiantesListView.as_view(), name='ausencia_estudiante_list'),
    path('corte_estudiante/list', CorteEstudianteListView.as_view(), name='corte_estudiante_list'),
    path('corte_trabajador/list', CorteTrabajadorListView.as_view(), name='corte_trabajador_list'),
    path('reporte_mensual/list', ReporteMensualListView.as_view(), name='reporte_mensual_list'),
    path('reporte_semanal/list', ReporteSemanalListView.as_view(), name='reporte_semanal_list'),

    path('aviso_corte_estudiante/list', AvisoCorteEstudianteListView.as_view(), name='aviso_corte_estudiante_list'),
    path('aviso_corte_trabajador/list', AvisoCorteTrabajadorListView.as_view(), name='aviso_corte_trabajador_list'),

    path('guardia_general_trabajador/list', GuardiaGeneralTrabajadorListView.as_view(),
         name='guardia_general_trabajador_list'),

    path('guardia_general_estudiante/list', GuardiaGeneralEstudianteListView.as_view(),
         name='guardia_general_estudiante_list'),

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

    path('guardia_general_estudiante/add', GuardiaGeneralEstudianteCreateView.as_view(),
         name='guardia_general_estudiante_create'),
    path('guardia_general_trabajador/add', GuardiaGeneralTrabajadorCreateView.as_view(),
         name='guardia_general_trabajador_create'),

    path('estudiante/add', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('ausencia_estudiante/add', AusenciasEstudiantesCreateView.as_view(), name='ausencia_estudiante_create'),
    path('ausencia_trabajador/add', AusenciasTrabajadorCreateView.as_view(), name='ausencia_trabajador_create'),
    path('corte_estudiante/add', CorteEstudianteCreateView.as_view(), name='corte_estudiante_create'),
    path('corte_trabajador/add', CorteTrabajadorCreateView.as_view(), name='corte_trabajador_create'),
    path('reporte_mensual/add', ReporteMensualCreateView.as_view(), name='reporte_mensual_create'),
    path('reporte_semanal/add', ReporteSemanalCreateView.as_view(), name='reporte_semanal_create'),
    path('trabajador/add', TrabajadorCreateView.as_view(), name='trabajador_create'),

    path('aviso_corte_estudiante/add', AvisoCorteEstudianteCreateView.as_view(), name='aviso_corte_estudiante_create'),
    path('aviso_corte_trabajador/add', AvisoCorteTrabajadorCreateView.as_view(), name='aviso_corte_trabajador_create'),
    path('estudiante/edit/<int:pk>/', EstudianteUpdateView.as_view(), name='estudiante_update'),
    path('estudiante/delete/<int:pk>/', EstudianteDeleteView.as_view(), name='estudiante_delete'),
    path('ausencia_estudiante/edit/<int:pk>/', AusenciaEstudianteUpdateView.as_view(),
         name='ausencia_estudiante_update'),
    path('ausencia_estudiante/delete/<int:pk>/', AusenciaEstudianteDeleteView.as_view(),
         name='ausencia_estudiante_delete'),
    path('ausencia_trabajador/edit/<int:pk>/', AusenciaTrabajadorUpdateView.as_view(),
         name='ausencia_trabajador_update'),
    path('ausencia_trabajador/delete/<int:pk>/', AusenciaTrabajadorDeleteView.as_view(),
         name='ausencia_trabajador_delete'),
    path('corte_estudiante/edit/<int:pk>/', CorteEstudianteUpdateView.as_view(), name='corte_estudiante_update'),
    path('corte_trabajador/edit/<int:pk>/', CorteTrabajadorUpdateView.as_view(), name='corte_trabajador_update'),
    path('corte_estudiante/delete/<int:pk>/', CorteEstudianteDeleteView.as_view(), name='corte_estudiante_delete'),
    path('corte_trabajador/delete/<int:pk>/', CorteTrabajadorDeleteView.as_view(), name='corte_trabajador_delete'),
    path('reporte_mensual/edit/<int:pk>/', ReporteMensualUpdateView.as_view(), name='reporte_mensual_update'),
    path('reporte_mensual/delete/<int:pk>/', ReporteMensualDeleteView.as_view(), name='reporte_mensual_delete'),
    path('reporte_semanal/edit/<int:pk>/', ReporteSemanalUpdateView.as_view(), name='reporte_semanal_update'),
    path('reporte_semanal/delete/<int:pk>/', ReporteSemanalDeleteView.as_view(), name='reporte_semanal_delete'),
    path('trabajador/edit/<int:pk>/', TrabajadorUpdateView.as_view(), name='trabajador_update'),
    path('trabajador/delete/<int:pk>/', TrabajadorDeleteView.as_view(), name='trabajador_delete'),

    path('aviso_corte_estudiante/edit/<int:pk>/', AvisoCorteEstudianteUpdateView.as_view(),
         name='aviso_corte_estudiante_update'),
    path('aviso_corte_estudiante/delete/<int:pk>/', AvisoCorteEstudianteDeleteView.as_view(),
         name='aviso_corte_estudiante_delete'),
    path('aviso_corte_trabajador/edit/<int:pk>/', AvisoCorteTrabajadorUpdateView.as_view(),
         name='aviso_corte_trabajador_update'),
    path('aviso_corte_trabajador/delete/<int:pk>/', AvisoCorteTrabajadorDeleteView.as_view(),
         name='aviso_corte_trabajador_delete'),

    path('guardia_general_estudiante/edit/<int:pk>/', GuardiaGeneralEstudianteUpdateView.as_view(),
         name='guardia_general_estudiante_update'),
    path('guardia_general_estudiante/delete/<int:pk>/', GuardiaGeneralEstudianteDeleteView.as_view(),
         name='guardia_general_estudiante_delete'),
    path('guardia_general_trabajador/edit/<int:pk>/', GuardiaGeneralTrabajadorUpdateView.as_view(),
         name='guardia_general_trabajador_update'),
    path('guardia_general_trabajador/delete/<int:pk>/', GuardiaGeneralTrabajadorDeleteView.as_view(),
         name='guardia_general_trabajador_delete'),

]
