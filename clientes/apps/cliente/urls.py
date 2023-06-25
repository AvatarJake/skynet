from django.contrib import admin
from django.urls import path
from .views import ClienteView

urlpatterns = [
    path('clientes/',ClienteView.as_view(),name='clientes_list'),
    path('clientes/<str:id>',ClienteView.as_view(),name='clientes_process'),
    path('clientes/<str:id>/change/',ClienteView.as_view(),name='clientes_puts'),
]
