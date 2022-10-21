from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ReporteSemanalForm
from core.erp.models import Reporte_Mensual

class ReporteSemanalListView(ListView):
    model = Reporte_Mensual
    template_name = 'reporte_semanal/list.html'
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Reportes Semanal'
        context['create_url'] = reverse_lazy('erp:reporte_semanal_create')
        context['list_url'] = reverse_lazy('erp:reporte_semanal_list')
        context['entity'] = 'Reportes Semanales'
        return context


class ReporteSemanalCreateView(CreateView):
    model = Reporte_Mensual
    form_class = ReporteSemanalForm
    template_name = 'Reporte_Semanal/create.html'
    success_url = reverse_lazy('erp:reporte_semanal_list')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un nuevo Reporte Semanal'
        context['create_url'] = reverse_lazy('erp:reporte_semanal_create')
        context['list_url'] = reverse_lazy('erp:reporte_semanal_list')
        context['entity'] = 'Reportes Semanales'
        return context

class ReporteSemanalUpdateView(UpdateView):
    model = Reporte_Mensual
    form_class = ReporteSemanalForm
    template_name = 'reporte_semanal/create.html'
    success_url = reverse_lazy('erp:reporte_semanal_list')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Reporte Semanal'
        context['entity'] = 'Reporte Semanal'
        context['list_url'] = reverse_lazy('erp:reporte_semanal_list')
        context['action'] = 'edit'
        return context


class ReporteSemanalDeleteView(DeleteView):
    model = Reporte_Mensual
    template_name = 'reporte_semanal/delete.html'
    success_url = reverse_lazy('erp:reporte_semanal_list')


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar un Reporte Semanal'
        context['entity'] = 'Reporte Semanal'
        context['list_url'] = reverse_lazy('erp:reporte_semanal_list')
        return context