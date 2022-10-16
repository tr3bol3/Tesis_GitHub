from django.views.generic import ListView

from core.erp.models import Corte

class CorteListView(ListView):
    model = Corte
    template_name = 'corte/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cortes'
        return context

