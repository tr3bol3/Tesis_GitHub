from django.urls import path
from core.erp.views import miprimeravista

urlpatterns = [
    path('uno', miprimeravista),
    path('dos', miprimeravista)
]