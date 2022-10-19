from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import AusenciasEstudianteForm
from core.erp.models import Ausencia_Estudiante

class AusenciaEstudiantesListView(ListView):
    model = Ausencia_Estudiante
    template_name = 'ausencia_estudiante/list.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Ausencia_Estudiante.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        print(request.POST)
        return JsonResponse(data)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ausencias de Estudiante'
        context['create_url'] = reverse_lazy('erp:ausencia_estudiante_create')
        context['list_url'] = reverse_lazy('erp:ausencia_estudiante_list')
        context['entity'] = 'Ausencias de Estudiantes'
        return context

class AusenciasEstudiantesCreateView(CreateView):
    model = Ausencia_Estudiante
    form_class = AusenciasEstudianteForm
    template_name = 'Ausencia_Estudiante/create.html'
    success_url = reverse_lazy('erp:ausencia_estudiante_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir Ausencia de Estudiante'
        context['create_url'] = reverse_lazy('erp:ausencia_estudiante_create')
        context['list_url'] = reverse_lazy('erp:ausencia_estudiante_list')
        context['entity'] = 'Ausencias de Estudiantes'
        return context


class AusenciaEstudianteUpdateView(UpdateView):
    model = Ausencia_Estudiante
    form_class = AusenciasEstudianteForm
    template_name = 'ausencia_estudiante/create.html'
    success_url = reverse_lazy('erp:ausencia_estudiante_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una Ausencia'
        context['entity'] = 'Ausencia de Estudiante'
        context['list_url'] = reverse_lazy('erp:ausencia_estudiante_list')
        context['action'] = 'edit'
        return context


class AusenciaEstudianteDeleteView(DeleteView):
    model = Ausencia_Estudiante
    template_name = 'ausencia_estudiante/delete.html'
    success_url = reverse_lazy('erp:ausencia_estudiante_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar una Ausencia'
        context['entity'] = 'Ausencia de Estudiante'
        context['list_url'] = reverse_lazy('erp:ausencia_estudiante_list')
        return context


