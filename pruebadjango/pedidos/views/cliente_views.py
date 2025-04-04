from django.shortcuts import redirect, render

from pedidos.models import Cliente
from pedidos.forms import ClienteForm


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(
        request,
        "pedido/clientes/list.html",
        {"clientes": clientes}
    )


def cliente_create(request):
    form = ClienteForm()

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")

    return render(
        request,
        "pedido/clientes/form.html",
        {"form": form}
    )


def cliente_edit(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("cliente_list")

    form = ClienteForm(instance=cliente)
    return render(
        request,
        "pedido/clientes/form.html",
        {"form": form}
    )


def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("cliente_list")
