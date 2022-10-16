from django.views.generic import ListView

from core.erp.models import Trabajador, Ausencia_Trabajador


class TrabajadorListView(ListView):
    model = Trabajador
    print(model)
    template_name = 'trabajador/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Trabajadores'
        return context
