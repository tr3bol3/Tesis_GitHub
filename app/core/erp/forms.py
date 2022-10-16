from django.forms import ModelForm

from core.erp.models import Estudiante, Ausencia_Estudiante


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class AusenciasEstudianteForm(ModelForm):
    class Meta:
        model = Ausencia_Estudiante
        fields = '__all__'