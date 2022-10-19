from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ReporteMensualForm
from core.erp.models import Reporte_Mensual

class ReporteMensualListView(ListView):
    model = Reporte_Mensual
    template_name = 'reporte_mensual/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Reportes Mensuales'
        context['create_url'] = reverse_lazy('erp:reporte_mensual_create')
        context['list_url'] = reverse_lazy('erp:reporte_mensual_list')
        context['entity'] = 'Reportes Mensuales'
        return context

class ReporteMensualCreateView(CreateView):
    model = Reporte_Mensual
    form_class = ReporteMensualForm
    template_name = 'Reporte_Mensual/create.html'
    success_url = reverse_lazy('erp:reporte_mensual_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un nuevo Reporte Mensual'
        context['create_url'] = reverse_lazy('erp:reporte_mensual_create')
        context['list_url'] = reverse_lazy('erp:reporte_mensual_list')
        context['entity'] = 'Reportes Mensuales'
        return context

class ReporteMensualUpdateView(UpdateView):
    model = Reporte_Mensual
    form_class = ReporteMensualForm
    template_name = 'reporte_mensual/create.html'
    success_url = reverse_lazy('erp:reporte_mensual_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Reporte Mensual'
        context['entity'] = 'Reporte Mensual'
        context['list_url'] = reverse_lazy('erp:reporte_mensual_list')
        context['action'] = 'edit'
        return context


class ReporteMensualDeleteView(DeleteView):
    model = Reporte_Mensual
    form_class = ReporteMensualForm
    template_name = 'reporte_mensual/delete.html'
    success_url = reverse_lazy('erp:reporte_mensual_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Reporte Mensual'
        context['entity'] = 'Reporte Mensual'
        context['list_url'] = reverse_lazy('erp:reporte_mensual_list')
        return context