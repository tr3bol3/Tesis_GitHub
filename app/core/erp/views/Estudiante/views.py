from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import EstudianteForm
from core.erp.models import Estudiante

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiante/list.html'


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Estudiantes'
        context['create_url'] = reverse_lazy('erp:estudiante_create')
        context['list_url'] = reverse_lazy('erp:estudiante_list')
        context['entity'] = 'Estudiantes'

        # lista = []
        # for i in Estudiante.objects.filter():
        #    lista.append(i.ausencia_estudiante_set.count())
        # context['ausencias'] = lista
        # context['n'] = 0
        return context



class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'Estudiante/create.html'
    success_url = reverse_lazy('erp:estudiante_list')




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un nuevo Estudiante'
        context['entity'] = 'Estudiantes'
        context['list_url'] = reverse_lazy('erp:estudiante_list')
        context['action'] = 'add'
        return context



class EstudianteUpdateView(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'estudiante/create.html'
    success_url = reverse_lazy('erp:estudiante_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un Estudiante'
        context['entity'] = 'Estudiante'
        context['list_url'] = reverse_lazy('erp:estudiante_list')
        context['action'] = 'edit'
        return context


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'estudiante/delete.html'
    success_url = reverse_lazy('erp:estudiante_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Estudiante'
        context['entity'] = 'Estudiante'
        context['list_url'] = reverse_lazy('erp:estudiante_list')
        return context

