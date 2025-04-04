from django import forms

from pedidos.models import Mesa


class MesaForm(forms.ModelForm):
    numero = forms.IntegerField(
        label="Número",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Mesa
        fields = ["numero"]
