from django.views.generic import ListView

from core.erp.models import Guardia_Trabajador

class GuardiaTrabajadorNocturnoListView(ListView):
    model = Guardia_Trabajador
    template_name = 'guardia_trabajador_nocturno/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trabajadores GOE Nocturna'
        return context