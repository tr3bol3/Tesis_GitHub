from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import TrabajadorForm
from core.erp.models import Trabajador, Ausencia_Trabajador


class TrabajadorListView(ListView):
    model = Trabajador
    print(model)
    template_name = 'trabajador/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Trabajadores'
        context['create_url'] = reverse_lazy('erp:trabajador_create')
        context['list_url'] = reverse_lazy('erp:trabajador_list')
        context['entity'] = 'Trabajadores'
        return context


class TrabajadorCreateView(CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'Trabajador/create.html'
    success_url = reverse_lazy('erp:trabajador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un nuevo Trabajador'
        context['create_url'] = reverse_lazy('erp:trabajador_create')
        context['list_url'] = reverse_lazy('erp:trabajador_list')
        context['entity'] = 'Trabajadores'
        return context

class TrabajadorUpdateView(UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('erp:trabajador_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un Trabajador'
        context['entity'] = 'Trabajador'
        context['list_url'] = reverse_lazy('erp:trabajador_list')
        context['action'] = 'edit'
        return context


class TrabajadorDeleteView(DeleteView):
    model = Trabajador
    template_name = 'trabajador/delete.html'
    success_url = reverse_lazy('erp:trabajador_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Trabajador'
        context['entity'] = 'Trabajador'
        context['list_url'] = reverse_lazy('erp:trabajador_list')
        return context