from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import CorteEstudianteForm
from core.erp.models import Corte_Estudiante

class CorteEstudianteListView(ListView):
    model = Corte_Estudiante
    template_name = 'corte_estudiante/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cortes de Estudiantes'
        context['create_url'] = reverse_lazy('erp:corte_estudiante_create')
        context['list_url'] = reverse_lazy('erp:corte_estudiante_list')
        context['entity'] = 'Cortes Estudiantes'
        return context

class CorteEstudianteCreateView(CreateView):
    model = Corte_Estudiante
    form_class = CorteEstudianteForm
    template_name = 'Corte_Estudiante/create.html'
    success_url = reverse_lazy('erp:corte_estudiante_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Corte a un Estudiante'
        context['create_url'] = reverse_lazy('erp:corte_estudiante_create')
        context['list_url'] = reverse_lazy('erp:corte_estudiante_list')
        context['entity'] = 'Cortes Estudiantes'
        return context

class CorteEstudianteUpdateView(UpdateView):
    model = Corte_Estudiante
    form_class = CorteEstudianteForm
    template_name = 'corte_estudiante/create.html'
    success_url = reverse_lazy('erp:corte_estudiante_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Corte de un Estudiante'
        context['entity'] = 'Corte Estudiante'
        context['list_url'] = reverse_lazy('erp:corte_estudiante_list')
        context['action'] = 'edit'
        return context


class CorteEstudianteDeleteView(DeleteView):
    model = Corte_Estudiante
    template_name = 'corte_estudiante/delete.html'
    success_url = reverse_lazy('erp:corte_estudiante_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Corte Estudiante'
        context['entity'] = 'Corte Estudiante'
        context['list_url'] = reverse_lazy('erp:corte_estudiante_list')
        return context

