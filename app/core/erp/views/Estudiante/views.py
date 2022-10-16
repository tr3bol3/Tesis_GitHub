from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from core.erp.forms import EstudianteForm
from core.erp.models import Estudiante

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiante/list.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Estudiante'
        #lista = []
        #for i in Estudiante.objects.filter():
        #    lista.append(i.ausencia_estudiante_set.count())
        #context['ausencias'] = lista
        #context['n'] = 0
        return context


class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'Estudiante/create.html'
    success_url = reverse_lazy('erp:estudiante_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Añadir un nuevo Estudiante'
        return context

