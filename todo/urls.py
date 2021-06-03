# -*- coding: utf-8 -*-
from django.urls import path
from .  import views

urlpatterns=[
    path("", views.home, name="home"),
    path("homei", views.home, name="homei"),
    path("home/<int:arbol_nodo>", views.homen, name="homen"),
    path("respuesta/<int:arbol_nodo>", views.respuesta, name="respuesta"),
    path("agregar_nodo/<int:arbol_nodo>", views.agregar_nodo, name="agregar_nodo"),
    path("homsi/<int:arbol_nodo>", views.homsi, name="homsi"),
    path("homno/<int:arbol_nodo>", views.homno, name="homno"),
    path("hompsi/<int:arbol_nodo>", views.hompsi, name="hompsi"),
    path("hompno/<int:arbol_nodo>", views.hompno, name="hompno"),
    path("homnose/<int:arbol_nodo>", views.homnose, name="homnose"),
    path("oportunidad/<int:arbol_nodo>", views.oportunidad, name="oportunidad"),
    
    path("agregar/", views.agregar, name="agregar"),
    path("eliminar/<int:tarea_id>/", views.eliminar, name="eliminar"),
    path("editar/<int:tarea_id>/", views.editar, name="editar"),
]