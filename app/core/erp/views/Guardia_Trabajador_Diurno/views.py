from django.views.generic import ListView

from core.erp.models import Guardia_Trabajador

class GuardiaTrabajadorDiurnoListView(ListView):
    model = Guardia_Trabajador
    template_name = 'guardia_trabajador_diurno/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trabajadores GOE Diurna'
        return context