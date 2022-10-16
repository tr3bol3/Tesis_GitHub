from django.views.generic import ListView

from core.erp.models import Guardia_Estudiante

class GuardiaEstudianteFemeninaDiurnoListView(ListView):
    model = Guardia_Estudiante
    template_name = 'guardia_estudiante_femenina_diurno/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estudiante Femeninas GOE Diurna'
        return context