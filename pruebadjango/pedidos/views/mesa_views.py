from django.shortcuts import redirect, render

from pedidos.models import Mesa
from pedidos.forms import MesaForm


def mesa_list(request):
    mesas = Mesa.objects.all()
    return render(
        request,
        "pedido/mesas/list.html",
        {"mesas": mesas}
    )


def mesa_create(request):
    form = MesaForm()

    if request.method == "POST":
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mesa_list")

    return render(
        request,
        "pedido/mesas/form.html",
        {"form": form}
    )


def mesa_edit(request, id):
    mesa = Mesa.objects.get(id=id)
    if request.method == "POST":
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect("mesa_list")

    form = MesaForm(instance=mesa)
    return render(
        request,
        "pedido/mesas/form.html",
        {"form": form}
    )


def mesa_delete(request, id):
    mesa = Mesa.objects.get(id=id)
    mesa.delete()
    return redirect("mesa_list")
