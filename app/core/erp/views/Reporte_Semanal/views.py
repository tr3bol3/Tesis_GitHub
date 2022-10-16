from django.views.generic import ListView

from core.erp.models import Reporte_Mensual

class ReporteSemanalListView(ListView):
    model = Reporte_Mensual
    template_name = 'reporte_semanal/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Reportes Semanal'
        return context