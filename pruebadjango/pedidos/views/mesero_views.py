from django.shortcuts import redirect, render

from pedidos.models import Mesero
from pedidos.forms import MeseroForm


def mesero_list(request):
    meseros = Mesero.objects.all()
    return render(
        request,
        "pedido/meseros/list.html",
        {"meseros": meseros}
    )


def mesero_create(request):
    form = MeseroForm()

    if request.method == "POST":
        form = MeseroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mesero_list")

    return render(
        request,
        "pedido/meseros/form.html",
        {"form": form}
    )


def mesero_edit(request, id):
    mesero = Mesero.objects.get(id=id)
    if request.method == "POST":
        form = MeseroForm(request.POST, instance=mesero)
        if form.is_valid():
            form.save()
            return redirect("mesero_list")

    form = MeseroForm(instance=mesero)
    return render(
        request,
        "pedido/meseros/form.html",
        {"form": form}
    )


def mesero_delete(request, id):
    mesero = Mesero.objects.get(id=id)
    mesero.delete()
    return redirect("mesero_list")
