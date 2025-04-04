from django.urls import path

from . import views

urlpatterns = [

    path("clientes", views.cliente_list, name="cliente_list"),
    path("clientes/create", views.cliente_create, name="cliente_create"),
    path("clientes/<int:id>", views.cliente_edit, name="cliente_edit"),
    path("clientes/<int:id>/delete", views.cliente_delete, name="cliente_delete"),

    path("platos", views.plato_list, name="plato_list"),
    path("platos/create", views.plato_create, name="plato_create"),
    path("platos/<int:id>", views.plato_edit, name="plato_edit"),
    path("platos/<int:id>/delete", views.plato_delete, name="plato_delete"),

    path("meseros", views.mesero_list, name="mesero_list"),
    path("meseros/create", views.mesero_create, name="mesero_create"),
    path("meseros/<int:id>", views.mesero_edit, name="mesero_edit"),
    path("meseros/<int:id>/delete", views.mesero_delete, name="mesero_delete"),

    path("mesas", views.mesa_list, name="mesa_list"),
    path("mesas/create", views.mesa_create, name="mesa_create"),
    path("mesas/<int:id>", views.mesa_edit, name="mesa_edit"),
    path("mesas/<int:id>/delete", views.mesa_delete, name="mesa_delete"),

    path("ordenes", views.orden_list, name="orden_list"),
    path("ordenes/create", views.orden_create, name="orden_create"),
    path("ordenes/<int:id>/edit", views.orden_edit, name="orden_edit"),
    path("ordenes/<int:id>", views.orden_close, name="orden_close"),
    path("ordenes/<int:id>/delete", views.orden_delete, name="orden_delete"),
]
