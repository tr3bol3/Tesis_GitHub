from django.urls import path
from core.erp.views import miprimeravista, misegundavista

urlpatterns = [
    path('uno', miprimeravista),
    path('dos', misegundavista)
]