from django.shortcuts import redirect, render

from pedidos.models import Plato
from pedidos.forms import PlatoForm


def plato_list(request):
    platos = Plato.objects.all()
    return render(
        request,
        "pedido/platos/list.html",
        {"platos": platos}
    )


def plato_create(request):
    form = PlatoForm()

    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plato_list")

    return render(
        request,
        "pedido/platos/form.html",
        {"form": form}
    )


def plato_edit(request, id):
    plato = Plato.objects.get(id=id)
    if request.method == "POST":
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect("plato_list")

    form = PlatoForm(instance=plato)
    return render(
        request,
        "pedido/platos/form.html",
        {"form": form}
    )


def plato_delete(request, id):
    plato = Plato.objects.get(id=id)
    plato.delete()
    return redirect("plato_list")
