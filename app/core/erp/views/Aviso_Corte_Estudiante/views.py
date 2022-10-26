from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import EstudianteForm, AvisoCorteEstudianteForm
from core.erp.models import Estudiante, Aviso_Corte_Estudiante


class AvisoCorteEstudianteListView(ListView):
    model = Aviso_Corte_Estudiante
    template_name = 'aviso_corte_estudiante/list.html'


    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Estudiantes citados a Corte'
        context['create_url'] = reverse_lazy('erp:aviso_corte_estudiante_create')
        context['list_url'] = reverse_lazy('erp:aviso_corte_estudiante_list')
        context['entity'] = 'Aviso Corte estudiante'
        return context


class AvisoCorteEstudianteCreateView(CreateView):

    model = Aviso_Corte_Estudiante
    form_class = AvisoCorteEstudianteForm
    template_name = 'Aviso_Corte_Estudiante/create.html'
    success_url = reverse_lazy('erp:aviso_corte_estudiante_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un nuevo Aviso de Corte para Estudiante'
        context['entity'] = 'Aviso Corte Estudiantes'
        context['list_url'] = reverse_lazy('erp:aviso_corte_estudiante_list')
        context['action'] = 'add'
        return context


class AvisoCorteEstudianteUpdateView(UpdateView):

    model = Aviso_Corte_Estudiante
    form_class = AvisoCorteEstudianteForm
    template_name = 'aviso_corte_estudiante/create.html'
    success_url = reverse_lazy('erp:aviso_corte_estudiante_list')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un Aviso de Corte de Estudiante'
        context['entity'] = 'Aviso Corte Estudiante'
        context['list_url'] = reverse_lazy('erp:aviso_corte_estudiante_list')
        context['action'] = 'edit'
        return context


class AvisoCorteEstudianteDeleteView(DeleteView):

    model = Aviso_Corte_Estudiante
    template_name = 'aviso_corte_estudiante/delete.html'
    success_url = reverse_lazy('erp:aviso_corte_estudiante_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Aviso de Corte de Estudiante'
        context['entity'] = 'Aviso Corte Estudiante'
        context['list_url'] = reverse_lazy('erp:aviso_corte_estudiante_list')
        return context

