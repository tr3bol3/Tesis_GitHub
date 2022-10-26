import psycopg2
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import TrabajadorForm
from core.erp.models import Trabajador


class TrabajadorListView(ListView):
    model = Trabajador
    template_name = 'trabajador/list.html'


    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    @method_decorator(login_required)
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Trabajador'
        context['entity'] = 'Trabajador'
        context['list_url'] = reverse_lazy('erp:trabajador_list')
        return context