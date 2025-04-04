from django import forms
from pedidos.models import Orden

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['mesero', 'mesa']
        widgets = {
            'mesero': forms.Select(attrs={'class': 'form-control'}),
            'mesa': forms.Select(attrs={'class': 'form-control'})
        }