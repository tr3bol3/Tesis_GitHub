from django.views.generic import ListView

from core.erp.models import Reporte_Mensual

class ReporteMensualListView(ListView):
    model = Reporte_Mensual
    template_name = 'reporte_mensual/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Reportes Mensuales'
        return context