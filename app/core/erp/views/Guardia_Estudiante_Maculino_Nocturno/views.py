from django.views.generic import ListView

from core.erp.models import Guardia_Estudiante

class GuardiaEstudianteNocturnoMasculinoListView(ListView):
    model = Guardia_Estudiante
    template_name = 'guardia_estudiante_masculino_nocturno/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estudiante Masculinos GOE Nocturna'
        return context