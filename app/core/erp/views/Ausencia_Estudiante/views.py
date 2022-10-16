from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from core.erp.forms import AusenciasEstudianteForm
from core.erp.models import Ausencia_Estudiante

class AusenciaEstudiantesListView(ListView):
    model = Ausencia_Estudiante
    template_name = 'ausencia_estudiante/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ausencias de Estudiante'
        return context

class AusenciasEstudiantesCreateView(CreateView):
    model = Ausencia_Estudiante
    form_class = AusenciasEstudianteForm
    template_name = 'Ausencia_Estudiante/create.html'
    success_url = reverse_lazy('ausencia_estudiante_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir una nueva Ausencia'
        return context


