from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from core.erp.forms import GuardiaGeneralTrabajadorForm
from core.erp.models import Guardia_Trabajador


class GuardiaGeneralTrabajadorListView(ListView):
    model = Guardia_Trabajador
    template_name = 'guardia_general_trabajador/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Guardia General de Trabajadores'
        context['create_url'] = reverse_lazy('erp:guardia_general_trabajador_create')
        return context


class GuardiaGeneralTrabajadorCreateView(CreateView):
    model = Guardia_Trabajador
    form_class = GuardiaGeneralTrabajadorForm
    template_name = 'Guardia_General_Trabajador/create.html'
    success_url = reverse_lazy('erp:guardia_general_trabajador_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir una nueva Guardia para un Trabajador'
        context['entity'] = 'Guardia Trabajador'
        context['list_url'] = reverse_lazy('erp:guardia_general_trabajador_list')
        context['action'] = 'add'
        return context


class GuardiaGeneralTrabajadorUpdateView(UpdateView):

    model = Guardia_Trabajador
    form_class = GuardiaGeneralTrabajadorForm
    template_name = 'Guardia_General_Trabajador/create.html'
    success_url = reverse_lazy('erp:guardia_general_trabajador_list')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Guardia de Trabajador'
        context['entity'] = 'Guardia General de Trabajador'
        context['list_url'] = reverse_lazy('erp:guardia_general_trabajador_list')
        context['action'] = 'edit'
        return context


class GuardiaGeneralTrabajadorDeleteView(DeleteView):

    model = Guardia_Trabajador
    template_name = 'guardia_general_trabajador/delete.html'
    success_url = reverse_lazy('erp:guardia_general_trabajador_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Guardia de Trabajador'
        context['entity'] = 'Guardia General de Trabajador'
        context['list_url'] = reverse_lazy('erp:guardia_general_trabajador_list')
        return context