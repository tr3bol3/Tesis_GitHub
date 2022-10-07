from django.urls import path

from core.erp.views.Estudiantes.views import estudiante_list

app_name = 'erp'

urlpatterns = [
    path('estudiante/list', estudiante_list, name='estudiante_list')
]
