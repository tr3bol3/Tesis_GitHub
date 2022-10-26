from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import AvisoCorteTrabajadorForm
from core.erp.models import Aviso_Corte_Trabajador


class AvisoCorteTrabajadorListView(ListView):
    model = Aviso_Corte_Trabajador
    template_name = 'aviso_corte_trabajador/list.html'


    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Trabajadores citados a Corte'
        context['create_url'] = reverse_lazy('erp:aviso_corte_trabajador_create')
        context['list_url'] = reverse_lazy('erp:aviso_corte_trabajador_list')
        context['entity'] = 'Aviso Corte Trabajador'
        return context


class AvisoCorteTrabajadorCreateView(CreateView):
    model = Aviso_Corte_Trabajador
    form_class = AvisoCorteTrabajadorForm
    template_name = 'Aviso_Corte_Trabajador/create.html'
    success_url = reverse_lazy('erp:aviso_corte_trabajador_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un nuevo Aviso de Corte para Trabajador'
        context['entity'] = 'Aviso Corte Trabajador'
        context['list_url'] = reverse_lazy('erp:aviso_corte_trabajador_list')
        context['action'] = 'add'
        return context


class AvisoCorteTrabajadorUpdateView(UpdateView):

    model = Aviso_Corte_Trabajador
    form_class = AvisoCorteTrabajadorForm
    template_name = 'aviso_corte_trabajador/create.html'
    success_url = reverse_lazy('erp:aviso_corte_trabajador_list')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un Aviso de Corte de Trabajador'
        context['entity'] = 'Aviso Corte Trabajador'
        context['list_url'] = reverse_lazy('erp:aviso_corte_trabajador_list')
        context['action'] = 'edit'
        return context


class AvisoCorteTrabajadorDeleteView(DeleteView):

    model = Aviso_Corte_Trabajador
    template_name = 'aviso_corte_trabajador/delete.html'
    success_url = reverse_lazy('erp:aviso_corte_trabajador_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Aviso de Corte de trabajador'
        context['entity'] = 'Aviso Corte Trabajador'
        context['list_url'] = reverse_lazy('erp:aviso_corte_trabajador_list')
        return context

