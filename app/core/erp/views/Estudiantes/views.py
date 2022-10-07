from django.shortcuts import render

from core.erp.models import Estudiante


def estudiante_list(request):
    data = {
        'title' : 'Listado de Estudiantes',
        'estudiante' : Estudiante.objects.all()
    }
    return render(request, 'estudiante/list.html', data)