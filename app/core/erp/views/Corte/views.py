from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import CorteForm
from core.erp.models import Corte

class CorteListView(ListView):
    model = Corte
    template_name = 'corte/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cortes'
        context['create_url'] = reverse_lazy('erp:corte_create')
        context['list_url'] = reverse_lazy('erp:corte_list')
        context['entity'] = 'Cortes'
        return context

class CorteCreateView(CreateView):
    model = Corte
    form_class = CorteForm
    template_name = 'Corte/create.html'
    success_url = reverse_lazy('erp:corte_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir una Corte'
        context['create_url'] = reverse_lazy('erp:corte_create')
        context['list_url'] = reverse_lazy('erp:corte_list')
        context['entity'] = 'Cortes'
        return context

class CorteUpdateView(UpdateView):
    model = Corte
    form_class = CorteForm
    template_name = 'corte/create.html'
    success_url = reverse_lazy('erp:corte_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Corte'
        context['entity'] = 'Corte'
        context['list_url'] = reverse_lazy('erp:corte_list')
        context['action'] = 'edit'
        return context


class CorteDeleteView(DeleteView):
    model = Corte
    template_name = 'corte/delete.html'
    success_url = reverse_lazy('erp:corte_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Corte'
        context['entity'] = 'Corte'
        context['list_url'] = reverse_lazy('erp:corte_list')
        return context

