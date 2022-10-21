from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.erp.models import Guardia_Trabajador

class GuardiaTrabajadorDiurnoListView(ListView):
    model = Guardia_Trabajador
    template_name = 'guardia_trabajador_diurno/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Trabajadores GOE Diurna'
        return context