from django import forms
from .models import Auditoria, Hallazgo

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = ['plan', 'proceso', 'normas', 'auditor_lider', 'fecha_programada', 'estado']
        widgets = {
            'fecha_programada': forms.DateInput(attrs={'type': 'date'}),
            'normas': forms.CheckboxSelectMultiple(),
        }

class HallazgoForm(forms.ModelForm):
    class Meta:
        model = Hallazgo
        fields = ['norma_relacionada', 'tipo', 'descripcion', 'evidencia_objetiva']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'evidencia_objetiva': forms.Textarea(attrs={'rows': 3}),
        }
