from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import AusenciasTrabajadorForm
from core.erp.models import Ausencia_Trabajador

class AusenciaTrabajadoresListView(ListView):
    model = Ausencia_Trabajador
    template_name = 'ausencia_trabajador/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ausencias de Trabajadores'
        context['create_url'] = reverse_lazy('erp:ausencia_trabajador_create')
        context['list_url'] = reverse_lazy('erp:ausencia_trabajador_list')
        context['entity'] = 'Ausencias de Trabajadores'
        return context

class AusenciasTrabajadorCreateView(CreateView):
    model = Ausencia_Trabajador
    form_class = AusenciasTrabajadorForm
    template_name = 'Ausencia_Trabajador/create.html'
    success_url = reverse_lazy('erp:ausencia_trabajador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Ausencia de Trabajador'
        context['create_url'] = reverse_lazy('erp:ausencia_trabajador_create')
        context['list_url'] = reverse_lazy('erp:ausencia_trabajador_list')
        context['entity'] = 'Ausencias de Trabajadores'
        return context

class AusenciaTrabajadorUpdateView(UpdateView):
    model = Ausencia_Trabajador
    form_class = AusenciasTrabajadorForm
    template_name = 'ausencia_trabajador/create.html'
    success_url = reverse_lazy('erp:ausencia_trabajador_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Ausencia'
        context['entity'] = 'Ausencia de Trabajador'
        context['list_url'] = reverse_lazy('erp:ausencia_trabajador_list')
        context['action'] = 'edit'
        return context


class AusenciaTrabajadorDeleteView(DeleteView):
    model = Ausencia_Trabajador
    template_name = 'ausencia_trabajador/delete.html'
    success_url = reverse_lazy('erp:ausencia_trabajador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una Ausencia'
        context['entity'] = 'Ausencia de Trabajador'
        context['list_url'] = reverse_lazy('erp:ausencia_trabajador_list')
        return context

