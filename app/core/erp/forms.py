from django.contrib.admin.helpers import checkbox
from django.forms import ModelForm, TextInput, Textarea, DateInput

from core.erp.models import Estudiante, Ausencia_Estudiante, Ausencia_Trabajador, Corte, Reporte_Mensual, Trabajador


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),

        }




class TrabajadorForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

class AusenciasEstudianteForm(ModelForm):
    class Meta:
        model = Ausencia_Estudiante
        fields = '__all__'
        widgets = {
            'fecha': DateInput(
                attrs={
                    'placeholder': 'Ingrese un fecha',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

class AusenciasTrabajadorForm(ModelForm):
    class Meta:
        model = Ausencia_Trabajador
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

class CorteForm(ModelForm):
    class Meta:
        model = Corte
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

class ReporteMensualForm(ModelForm):
    class Meta:
        model = Reporte_Mensual
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

class ReporteSemanalForm(ModelForm):
    class Meta:
        model = Reporte_Mensual
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

