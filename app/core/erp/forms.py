from django.contrib.admin.helpers import checkbox
from django.forms import *
from django.forms.widgets import Input
from django.utils.datetime_safe import datetime

from core.erp.models import Estudiante, Ausencia_Estudiante, Ausencia_Trabajador, Corte_Estudiante, Corte_Trabajador, \
    Reporte_Mensual, Trabajador, Guardia_Estudiante, Guardia_Trabajador, Aviso_Corte_Estudiante, Aviso_Corte_Trabajador


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'style' : 'width : 400px',
                    'class' : 'form-control',
                    'onkeydown' : "return /[a-z, ]/i.test(event.key)"

                }
            ),
            'lastName': TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos',
                    'style': 'width : 400px',
                    'class': 'form-control',
                    'onkeydown': "return /[a-z, ]/i.test(event.key)"
                }
            ),
            'ci': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el Carnet de Identidad',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'becado': CheckboxInput(
                attrs={
                    'style': 'width : 50px',
                    'class': 'form-control'
                }
            ),
            'limitaciones': Textarea(
                attrs={
                    'placeholder': 'De no presentar ninguna limitacion no escriba nada en este campo',
                    'style': 'width : 400px',
                    'class': 'form-control',
                    'rows': 3,
                    'cols': 3,
                }
            ),
            'anno': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el año',
                    'value' : 1,
                    'min' : 1,
                    'max' : 5,
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'carrera': TextInput(
                attrs={
                    'placeholder': 'Ingrese la Carrera',
                    'style': 'width : 400px',
                    'class': 'form-control',
                    'onkeydown': "return /[a-z, ]/i.test(event.key)"
                }
            ),
            'sex': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'facultad': TextInput(
                attrs={
                    'placeholder': 'Ingrese la Facultad',
                    'style': 'width : 400px',
                    'class': 'form-control',
                    'onkeydown': "return /[a-z, ]/i.test(event.key)"
                }
            ),
            'user': TextInput(
                attrs={
                    'placeholder': 'Ingrese el Usuario',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'placeholder': 'Ingrese la Contraseña',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
        }

class TrabajadorForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    'style' : 'width : 400px',
                    'class' : 'form-control',
                    'onkeydown': "return /[a-z, ]/i.test(event.key)"

                }
            ),
            'lastName': TextInput(
                attrs={
                    'placeholder': 'Ingrese los apellidos',
                    'style': 'width : 400px',
                    'class': 'form-control',
                    'onkeydown': "return /[a-z, ]/i.test(event.key)"
                }
            ),
            'ci': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el Carnet de Identidad',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'becado': CheckboxInput(
                attrs={
                    'style': 'width : 50px',
                    'class': 'form-control'
                }
            ),
            'limitaciones': Textarea(
                attrs={
                    'placeholder': 'De no presentar ninguna limitacion no escriba nada en este campo',
                    'style': 'width : 400px',
                    'class': 'form-control',
                    'rows': 3,
                    'cols': 3
                }
            ),
            'area': TextInput(
                attrs={
                    'placeholder': 'Ingrese el Área de Trabajao',
                    'value' : 1,
                    'min' : 1,
                    'max' : 5,
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'sex': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'user': TextInput(
                attrs={
                    'placeholder': 'Ingrese el Usuario',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'password': PasswordInput(
                attrs={
                    'placeholder': 'Ingrese la Contraseña',
                    'style': 'width : 400px',
                    'class': 'form-control'
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
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'estudiante': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
        }

class AusenciasTrabajadorForm(ModelForm):
    class Meta:
        model = Ausencia_Trabajador
        fields = '__all__'
        widgets = {
            'fecha': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date'
                }
            ),
            'trabajador': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
        }

class CorteEstudianteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Corte_Estudiante
        fields = '__all__'
        widgets = {
            'fecha': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'estudiante': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'replanificacion': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'justificacion': Textarea(
                attrs={
                    'placeholder': 'Ingrese la Justificación',
                    'rows': 3,
                    'cols': 3,
                    'class': 'form-control'
                }
            ),
            'causales': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class CorteTrabajadorForm(ModelForm):
    class Meta:
        model = Corte_Trabajador
        fields = '__all__'
        widgets = {
            'fecha': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'trabajador': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'replanificacion': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'justificacion': Textarea(
                attrs={
                    'placeholder': 'Ingrese la Justificación',
                    'rows': 3,
                    'cols': 3,
                    'class': 'form-control',
                }
            ),
            'causales': Select(
                attrs={
                    'class': 'form-control'
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

class GuardiaGeneralEstudianteForm(ModelForm):
    class Meta:
        model = Guardia_Estudiante
        fields = '__all__'
        widgets = {
            'estudiante': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'fecha': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'turno': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el año',
                    'value': 1,
                    'min': 1,
                    'max': 6,
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'diurno': CheckboxInput(
                attrs={
                    'style': 'width : 50px',
                    'class': 'form-control'
                }
            ),

        }

class GuardiaGeneralTrabajadorForm(ModelForm):
    class Meta:
        model = Guardia_Trabajador
        fields = '__all__'
        widgets = {
            'trabajador': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'fecha': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'turno': NumberInput(
                attrs={
                    'placeholder': 'Ingrese el año',
                    'value': 1,
                    'min': 1,
                    'max': 6,
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'diurno': CheckboxInput(
                attrs={
                    'style': 'width : 50px',
                    'class': 'form-control'
                }
            ),
        }

class AvisoCorteEstudianteForm(ModelForm):
    class Meta:
        model = Aviso_Corte_Estudiante
        fields = '__all__'
        widgets = {
            'fecha_aviso': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'fecha_citacion': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'estudiante': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
        }

class AvisoCorteTrabajadorForm(ModelForm):
    class Meta:
        model = Aviso_Corte_Trabajador
        fields = '__all__'
        widgets = {
            'fecha_aviso': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'fecha_citacion': DateInput(
                attrs={
                    'autocomplete': 'off',
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'type': 'date',
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),
            'trabajador': Select(
                attrs={
                    'style': 'width : 400px',
                    'class': 'form-control'
                }
            ),

        }