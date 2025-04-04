from django import forms

from pedidos.models import Mesero


class MeseroForm(forms.ModelForm):
    nombre = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    apellido = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    telefono = forms.CharField(
        label="Telefono",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Mesero
        fields = ["nombre", "apellido", "telefono"]
