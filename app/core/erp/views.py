from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def miprimeravista(request):
    return HttpResponse('Hola esta es mi primera URL')
