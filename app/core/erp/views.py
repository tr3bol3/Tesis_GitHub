from django.shortcuts import render
from core.erp.models import Type, Estudiante


# Create your views here.
def miprimeravista(request):
    data = {
        'name' : 'William',
        'tipo' : Type.objects.all()
    }

    return render(request,'index.html', data)

def misegundavista(request):
    data = {
        'name' : 'William',
        'estudiante' : Estudiante.objects.all()
    }

    return render(request,'second.html', data)