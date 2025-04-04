from django import forms

from pedidos.models import Plato


class PlatoForm(forms.ModelForm):
    nombre = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    descripcion = forms.CharField(
        label="Descripcion",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Plato
        fields = ["nombre", "descripcion"]
