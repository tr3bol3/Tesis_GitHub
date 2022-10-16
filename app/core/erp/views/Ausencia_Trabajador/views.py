from django.views.generic import ListView

from core.erp.models import Ausencia_Trabajador

class AusenciaTrabajadoresListView(ListView):
    model = Ausencia_Trabajador
    template_name = 'ausencia_trabajador/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ausencias de Trabajadores'
        return context

