from django.views.generic import ListView

from core.erp.models import Guardia_Estudiante

class GuardiaEstudianteExternoDiurnoListView(ListView):
    model = Guardia_Estudiante
    template_name = 'guardia_estudiante_externo_diurno/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estudiante Externos GOE Diurna'
        return context