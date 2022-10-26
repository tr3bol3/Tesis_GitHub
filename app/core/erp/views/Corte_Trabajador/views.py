from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import CorteTrabajadorForm
from core.erp.models import Corte_Trabajador

class CorteTrabajadorListView(ListView):
    model = Corte_Trabajador
    template_name = 'corte_trabajador/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cortes de Trabajadores'
        context['create_url'] = reverse_lazy('erp:corte_trabajador_create')
        context['list_url'] = reverse_lazy('erp:corte_trabajador_list')
        context['entity'] = 'Cortes Trabajador'
        return context

class CorteTrabajadorCreateView(CreateView):
    model = Corte_Trabajador
    form_class = CorteTrabajadorForm
    template_name = 'Corte_Trabajador/create.html'
    success_url = reverse_lazy('erp:corte_trabajador_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Corte a un Trabajador'
        context['create_url'] = reverse_lazy('erp:corte_trabajador_create')
        context['list_url'] = reverse_lazy('erp:corte_trabajador_list')
        context['entity'] = 'Cortes Trabajador'
        return context

class CorteTrabajadorUpdateView(UpdateView):
    model = Corte_Trabajador
    form_class = CorteTrabajadorForm
    template_name = 'corte_trabajador/create.html'
    success_url = reverse_lazy('erp:corte_trabajador_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Corte de un Trabajador'
        context['entity'] = 'Corte_Trabajador'
        context['list_url'] = reverse_lazy('erp:corte_trabajador_list')
        context['action'] = 'edit'
        return context


class CorteTrabajadorDeleteView(DeleteView):
    model = Corte_Trabajador
    template_name = 'corte_trabajador/delete.html'
    success_url = reverse_lazy('erp:corte_trabajador_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Corte_Trabajador'
        context['entity'] = 'Corte_Trabajador'
        context['list_url'] = reverse_lazy('erp:corte_trabajador_list')
        return context

