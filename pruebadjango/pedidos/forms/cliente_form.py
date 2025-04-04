from django import forms

from pedidos.models import Cliente


class ClienteForm(forms.ModelForm):
    nombre = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    nit = forms.IntegerField(
        label="Nit",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Cliente
        fields = ["nombre", "nit"]
