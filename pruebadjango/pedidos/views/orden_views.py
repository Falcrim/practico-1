from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from pedidos.models import Orden, Plato, DetalleOrden
from pedidos.forms import OrdenForm, ClienteForm

def orden_list(request):
    ordenes = Orden.objects.all().order_by('-fecha_hora')
    return render(request, 'pedido/ordenes/list.html', {'ordenes': ordenes})


def orden_create(request):
    platos = Plato.objects.all()

    if request.method == 'POST':
        form = OrdenForm(request.POST)
        try:
            if form.is_valid():
                orden = form.save(commit=False)
                orden.estado = 'abierto'
                orden.save()

                for plato in platos:
                    cantidad = int(request.POST.get(f'cantidad_{plato.id}', 0))
                    if cantidad > 0:
                        DetalleOrden.objects.create(
                            orden=orden,
                            plato=plato,
                            cantidad=cantidad
                        )

                return redirect('orden_list')

        except ValidationError as e:
            messages.error(request, e.messages[0])
    else:
        form = OrdenForm()

    return render(request, 'pedido/ordenes/form.html', {
        'form': form,
        'platos': platos
    })


def orden_edit(request, id):
    orden = get_object_or_404(Orden, id=id)

    if orden.estado == 'cerrado':
        messages.error(request, "No se puede editar una orden cerrada")
        return redirect('orden_list')

    platos = Plato.objects.all()
    detalles = {str(d.plato.id): d.cantidad for d in orden.detalleorden_set.all()}

    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        try:
            if form.is_valid():
                orden = form.save(commit=False)
                orden.save()

                for plato in platos:
                    cantidad = int(request.POST.get(f'cantidad_{plato.id}', 0))

                    if cantidad > 0:
                        DetalleOrden.objects.update_or_create(
                            orden=orden,
                            plato=plato,
                            defaults={'cantidad': cantidad}
                        )
                    else:
                        DetalleOrden.objects.filter(orden=orden, plato=plato).delete()

                messages.success(request, "Orden actualizada correctamente")
                return redirect('orden_list')

        except ValidationError as e:
            messages.error(request, e.messages[0])

    else:
        form = OrdenForm(instance=orden)

    return render(request, 'pedido/ordenes/form.html', {
        'form': form,
        'platos': platos,
        'detalles': detalles,
        'editing': True
    })

def orden_close(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            orden.cliente = cliente
            orden.estado = 'cerrado'
            orden.save()
            return redirect('orden_list')
    else:
        form = ClienteForm()
    return render(request, 'pedido/ordenes/close.html', {'orden': orden, 'form': form})

def orden_delete(request, id):
    orden = get_object_or_404(Orden, id=id)
    orden.delete()
    return redirect('orden_list')