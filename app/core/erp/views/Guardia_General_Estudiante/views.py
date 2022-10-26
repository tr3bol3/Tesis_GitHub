from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from core.erp.forms import GuardiaGeneralEstudianteForm
from core.erp.models import Guardia_Estudiante


class GuardiaGeneralEstudianteListView(ListView):
    model = Guardia_Estudiante
    template_name = 'Guardia_General_Estudiante/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Guardia General de Estudiantes'
        context['create_url'] = reverse_lazy('erp:guardia_general_estudiante_create')
        return context

class GuardiaGeneralEstudianteCreateView(CreateView):
    model = Guardia_Estudiante
    form_class = GuardiaGeneralEstudianteForm
    template_name = 'Guardia_General_Estudiante/create.html'
    success_url = reverse_lazy('erp:guardia_general_estudiante_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una nueva guardia para un Estudiante'
        context['entity'] = 'Guardia General Estudiante'
        context['list_url'] = reverse_lazy('erp:guardia_general_estudiante_list')
        return context


class GuardiaGeneralEstudianteUpdateView(UpdateView):

    model = Guardia_Estudiante
    form_class = GuardiaGeneralEstudianteForm
    template_name = 'Guardia_General_Estudiante/create.html'
    success_url = reverse_lazy('erp:guardia_general_estudiante_list')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Guardia de Estudiante'
        context['entity'] = 'Guardia General de Estudiante'
        context['list_url'] = reverse_lazy('erp:guardia_general_estudiante_list')
        context['action'] = 'edit'
        return context

class GuardiaGeneralEstudianteDeleteView(DeleteView):

    model = Guardia_Estudiante
    template_name = 'guardia_general_estudiante/delete.html'
    success_url = reverse_lazy('erp:guardia_general_estudiante_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Guardia de Estudiante'
        context['entity'] = 'Guardia General de Estudiante'
        context['list_url'] = reverse_lazy('erp:guardia_general_estudiante_list')
        return context